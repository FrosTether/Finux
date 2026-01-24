#include "FrostProtocolCore.h"

namespace FrostOS {
    void executeSovereignTransfer(string recipientAddress, double amountFNR) {
        // 1. Verify the Ledger Status
        if (!FrostProtocol::isLedgerSynced()) {
            throw HardwareException("Protocol Desync: Ensure AWS Swarm is active.");
        }

        // 2. Bypass Centralized Rails (The "Free Market" Hook)
        Transaction tx;
        tx.sender = "Jacob_Frost_Genesis_Node";
        tx.recipient = recipientAddress; // Kelsee's Frost Wallet
        tx.amount = amountFNR;
        tx.fee = 0.0001; // Minimal market-driven fee

        // 3. Sign with the Biometric Key we built earlier
        if (BiometricVault::signTransaction(tx)) {
            FrostProtocol::Broadcast(tx);
            cout << "Sovereign Transfer Complete. 💕 Sent via Free Market Rails." << endl;
        }
    }
}
