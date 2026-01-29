package com.frostprotocol.core;

import android.os.AsyncTask;
import android.util.Log;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.UUID;

public class FrostLink {

    private String serverUrl;
    private String deviceId;
    private String sessionToken;
    private boolean isConnected = false;
    private static final String TAG = "FrostLink";

    // Constructor: Use "http://10.0.2.2:5000" if testing on Emulator
    // Use "http://192.168.x.x:5000" if testing on real device
    public FrostLink(String url) {
        this.serverUrl = url;
        this.deviceId = UUID.randomUUID().toString(); // Generates a unique ID
    }

    // --- 1. Handshake (Register Device) ---
    public void performHandshake() {
        new Thread(() -> {
            try {
                JSONObject payload = new JSONObject();
                payload.put("device_id", deviceId);
                payload.put("type", "FrostGlass-Android");

                String response = sendPostRequest("/device/handshake", payload.toString());
                
                if (response != null) {
                    JSONObject json = new JSONObject(response);
                    this.sessionToken = json.optString("session_token");
                    this.isConnected = true;
                    Log.d(TAG, "[✅] Connected! Session: " + sessionToken);
                }
            } catch (Exception e) {
                Log.e(TAG, "[!] Handshake Failed: " + e.getMessage());
            }
        }).start();
    }

    // --- 2. Send Transaction (Pay FNR) ---
    public void sendTransaction(String recipient, double amount) {
        new Thread(() -> {
            if (!isConnected) {
                Log.e(TAG, "[!] Offline. Cannot transact.");
                return;
            }

            try {
                JSONObject payload = new JSONObject();
                payload.put("sender", deviceId);
                payload.put("recipient", recipient);
                payload.put("amount", amount);

                String response = sendPostRequest("/protocol/transaction", payload.toString());
                Log.d(TAG, "[💸] Transaction Result: " + response);

            } catch (Exception e) {
                Log.e(TAG, "[!] Tx Failed: " + e.getMessage());
            }
        }).start();
    }

    // --- Helper: Network Request ---
    private String sendPostRequest(String endpoint, String jsonInputString) throws Exception {
        URL url = new URL(serverUrl + endpoint);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/json; utf-8");
        conn.setRequestProperty("Accept", "application/json");
        conn.setDoOutput(true);

        try (OutputStream os = conn.getOutputStream()) {
            byte[] input = jsonInputString.getBytes("utf-8");
            os.write(input, 0, input.length);
        }

        int code = conn.getResponseCode();
        if (code == 200 || code == 201) {
            try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "utf-8"))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                return response.toString();
            }
        }
        return null;
    }
}
