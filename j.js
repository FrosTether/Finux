import * as LocalAuthentication from 'expo-local-authentication';

async function authenticateAndSign() {
  // 1. Check if the device has biometric hardware (Fingerprint/FaceID)
  const hasHardware = await LocalAuthentication.hasHardwareAsync();
  const isEnrolled = await LocalAuthentication.isEnrolledAsync();

  if (hasHardware && isEnrolled) {
    // 2. Get the "Challenge" (Nonce) from your backend
    const response = await fetch('https://your-backend.com/get-challenge');
    const { challenge } = await response.json();

    // 3. Trigger the Biometric Prompt
    const result = await LocalAuthentication.authenticateAsync({
      promptMessage: 'Authorize Transaction for Grayson\'s Wallet',
      fallbackLabel: 'Use Passcode',
    });

    if (result.success) {
      // 4. If biometric is successful, the Secure Enclave signs the challenge
      // In a real wallet, this is where the hardware-backed key signs the data
      const signature = await signWithSecureKey(challenge);

      // 5. Send the signature back to the backend to complete the bridge
      const verifyResponse = await fetch('https://your-backend.com/verify', {
        method: 'POST',
        body: JSON.stringify({ signature, challenge }),
      });
      
      const finalStatus = await verifyResponse.json();
      console.log("Transaction Status:", finalStatus);
    }
  }
}
