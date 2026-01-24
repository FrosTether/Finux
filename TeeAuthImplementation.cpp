#include "FrostVaultBiometrics.h"
#include <fosp/hardware/biometrics.h> // Custom FOSP Hardware Abstraction Layer

namespace FrostOS {
    AuthStatus FrostVaultAuthImpl::verifyIdentity(const std::string& userId) {
        // 1. Check if we are in the Secure World (TrustZone)
        if (!is_in_secure_world()) return AuthStatus::HARDWARE_ERR;

        // 2. Call the Biometric HAL
        auto result = fosp_biometric_verify(userId.c_str());

        if (result == BIOMETRIC_MATCH) {
            // Trigger 311Hz Haptic Confirmation
            trigger_haptic_feedback(311.0f);
            return AuthStatus::SUCCESS;
        }
        return AuthStatus::FAILED;
    }
}
