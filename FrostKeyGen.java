package com.frostprotocol.core.crypto;

import java.security.MessageDigest;
import java.security.SecureRandom;
import java.util.UUID;

public class FrostKeyGen {

    // 1. Generate a Brand New Wallet
    public static FrostWallet createNewWallet() {
        String privateKey = generatePrivateKey();
        String publicKey = generatePublicKey(privateKey);
        String address = generateFrostAddress(publicKey);
        
        return new FrostWallet(privateKey, publicKey, address);
    }

    // --- Helper Functions ---

    private static String generatePrivateKey() {
        // Generates a 64-character hex string (Standard 256-bit key)
        SecureRandom random = new SecureRandom();
        byte[] bytes = new byte[32];
        random.nextBytes(bytes);
        return bytesToHex(bytes);
    }

    private static String generatePublicKey(String privateKey) {
        // Simulates deriving a public key (In prod, use Elliptic Curve secp256k1)
        // For this prototype, we hash the private key to get a unique public identifier
        return sha256(privateKey);
    }

    private static String generateFrostAddress(String publicKey) {
        // Creates a vanity address starting with "fr1" (Frost Layer 1)
        String hash = sha256(publicKey);
        // Take the first 40 chars and add checksum/prefix
        return "fr1" + hash.substring(0, 38); 
    }

    private static String sha256(String input) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            byte[] hash = digest.digest(input.getBytes("UTF-8"));
            return bytesToHex(hash);
        } catch (Exception e) {
            throw new RuntimeException("Crypto Error", e);
        }
    }

    private static String bytesToHex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (byte b : bytes) {
            sb.append(String.format("%02x", b));
        }
        return sb.toString();
    }

    // --- Inner Class for the Wallet Object ---
    public static class FrostWallet {
        public final String privateKey; // KEEP SECRET (Save to EncryptedSharedPreferences)
        public final String publicKey;  // Share with network
        public final String address;    // Share with friends

        public FrostWallet(String priv, String pub, String addr) {
            this.privateKey = priv;
            this.publicKey = pub;
            this.address = addr;
        }
    }
}
