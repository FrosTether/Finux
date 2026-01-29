package com.frostprotocol.core;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.Build;
import android.os.IBinder;
import android.util.Log;
import androidx.core.app.NotificationCompat;

import java.security.MessageDigest;
import java.util.Random;

public class FrostMinerService extends Service {

    private static final String TAG = "FrostMiner";
    private static final String CHANNEL_ID = "FrostMinerChannel";
    private boolean isMining = false;
    private Thread miningThread;
    
    // Thermal Tuning: Throttle mining to prevent overheating
    // 0ms = Max Power, 100ms = Cool/Efficient
    private long thermalDelayMs = 50; 

    @Override
    public void onCreate() {
        super.onCreate();
        createNotificationChannel();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        String action = intent.getAction();
        
        if ("STOP".equals(action)) {
            stopMining();
            stopSelf();
            return START_NOT_STICKY;
        }

        // Start the service in the foreground (Persistent Notification)
        Intent notificationIntent = new Intent(this, MainActivity.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, notificationIntent, PendingIntent.FLAG_IMMUTABLE);

        Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
                .setContentTitle("Frost Protocol Active")
                .setContentText("FrostMiner is securing the network...")
                .setSmallIcon(android.R.drawable.ic_menu_compass) // Replace with your icon
                .setContentIntent(pendingIntent)
                .setPriority(NotificationCompat.PRIORITY_LOW)
                .build();

        startForeground(1, notification);

        if (!isMining) {
            startMining();
        }

        return START_STICKY;
    }

    private void startMining() {
        isMining = true;
        miningThread = new Thread(() -> {
            Log.d(TAG, "[❄️] Miner Started. Thermal Delay: " + thermalDelayMs + "ms");
            
            try {
                MessageDigest digest = MessageDigest.getInstance("SHA-256");
                Random random = new Random();
                byte[] buffer = new byte[32];
                long hashes = 0;
                long startTime = System.currentTimeMillis();

                while (isMining) {
                    // 1. Generate Random Data (Simulating Nonce)
                    random.nextBytes(buffer);
                    
                    // 2. Perform Hash (The Work)
                    byte[] hash = digest.digest(buffer);
                    hashes++;

                    // 3. Status Report (every 1000 hashes)
                    if (hashes % 1000 == 0) {
                        long now = System.currentTimeMillis();
                        double seconds = (now - startTime) / 1000.0;
                        if (seconds > 0) {
                            Log.i(TAG, String.format("[⛏️] Speed: %.2f H/s | Last Hash: %02x%02x...", (hashes / seconds), hash[0], hash[1]));
                        }
                    }

                    // 4. Thermal Throttle (Sleep to cool down CPU)
                    if (thermalDelayMs > 0) {
                        Thread.sleep(thermalDelayMs);
                    }
                }
            } catch (Exception e) {
                Log.e(TAG, "Mining Error", e);
            }
        });
        miningThread.start();
    }

    private void stopMining() {
        isMining = false;
        if (miningThread != null) {
            miningThread.interrupt();
        }
        Log.d(TAG, "[❄️] Miner Stopped.");
    }

    private void createNotificationChannel() {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel serviceChannel = new NotificationChannel(
                    CHANNEL_ID,
                    "Frost Miner Service",
                    NotificationManager.IMPORTANCE_LOW
            );
            NotificationManager manager = getSystemService(NotificationManager.class);
            if (manager != null) {
                manager.createNotificationChannel(serviceChannel);
            }
        }
    }

    @Override
    public IBinder onBind(Intent intent) {
        return null; // We don't need binding for this simple service
    }
}
