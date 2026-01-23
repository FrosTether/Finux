import ReactNativeBiometrics from 'react-native-biometrics';

const rnBiometrics = new ReactNativeBiometrics();

async function signWithSecureKey(challenge) {
  try {
    // 1. Trigger the biometric prompt and sign the challenge in one step
    const { success, signature } = await rnBiometrics.createSignature({
      promptMessage: 'Authorize Grayson\'s Wallet Transaction',
      payload: challenge, // This is the 'nonce' from your backend
    });

    if (success) {
      console.log('Biometric Signature Created:', signature);
      return signature; // Send this to your backend for verification
    } else {
      throw new Error('Biometric authorization failed or was canceled.');
    }
  } catch (error) {
    console.error('Signing Error:', error);
    return null;
  }
}
