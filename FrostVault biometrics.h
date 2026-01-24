#ifndef FROST_VAULT_BIOMETRICS_H
#define FROST_VAULT_BIOMETRICS_H

#include <vector>
#include <string>

namespace FrostOS {
    enum class AuthStatus { SUCCESS, FAILED, TIMEOUT, HARDWARE_ERR };

    class FrostVaultAuth {
    public:
        // Initialize the TEE (TrustZone) Session
        virtual bool initializeEnclave() = 0;

        // Request Fingerprint/Face verification via FOSP HAL
        virtual AuthStatus verifyIdentity(const std::string& userId) = 0;

        // Securely release the Genesis Key from the Vault
        virtual std::vector<uint8_t> releaseGenesisKey(const std::string& authToken) = 0;

        // Thermal Check: Ensure device isn't being tampered with/frozen
        virtual float getEnclaveTemperature() = 0;
    };
}

#endif // FROST_VAULT_BIOMETRICS_H
