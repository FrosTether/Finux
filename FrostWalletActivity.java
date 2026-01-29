package com.frostprotocol.core;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class FrostWalletActivity extends AppCompatActivity {

    private FrostLink frostLink; // The connector we built earlier
    private TextView tvBalance;
    private EditText etRecipient, etAmount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_frost_wallet);

        // 1. Initialize UI Elements
        tvBalance = findViewById(R.id.tvBalance);
        etRecipient = findViewById(R.id.etRecipient);
        etAmount = findViewById(R.id.etAmount);
        Button btnSend = findViewById(R.id.btnSend);

        // 2. Initialize Network Connection
        // NOTE TO AL: Change IP to the server's real IP address
        frostLink = new FrostLink("http://192.168.1.15:5000");
        frostLink.performHandshake();

        // 3. Button Logic
        btnSend.setOnClickListener(v -> {
            String recipient = etRecipient.getText().toString();
            String amountStr = etAmount.getText().toString();

            if (recipient.isEmpty() || amountStr.isEmpty()) {
                Toast.makeText(this, "Error: Missing fields", Toast.LENGTH_SHORT).show();
                return;
            }

            double amount = Double.parseDouble(amountStr);
            
            // Execute the transaction via FrostLink
            frostLink.sendTransaction(recipient, amount);
            
            Toast.makeText(this, "Transaction Broadcasted...", Toast.LENGTH_SHORT).show();
            etAmount.setText(""); // Clear input
        });

        // 4. Update Balance (Simulated for UI demo)
        refreshBalance();
    }

    private void refreshBalance() {
        // In a real scenario, this would ask FrostLink for the current balance
        tvBalance.setText("1,042.50 FNR"); 
    }
}
