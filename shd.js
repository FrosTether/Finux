import ReactNativeBiometrics from 'react-native-biometrics';

const rnBiometrics = new ReactNativeBiometrics();

async function initializeHardwareWallet() {
  // 1. Check if a key already exists
  const { keysExist } = await rnBiometrics.biometricKeysExist();

  if (!keysExist) {
    // 2. Create a new key pair that requires biometric authentication
    const { publicKey } = await rnBiometrics.createKeys();
    
    // 3. Register this Public Key with your backend
    const response = await fetch('https://your-backend.com/register-wallet', {
      method: 'POST',
      body: JSON.stringify({
        userId: 'Jacob_Frost', // Using your identifier for the bridge
        publicKey: publicKey,
      }),
    });
    
    console.log('Public Key Registered:', publicKey);
  }
}
