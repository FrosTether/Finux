// Amiahdo: The Sovereign AI Backend
val config = generationConfig {
    temperature = 0.4f // Lower temperature for "Cold Storage" level precision
    topK = 1
}

val amiahdo = GenerativeModel(
    modelName = "gemini-2.0-flash",
    apiKey = "YOUR_HARDCODED_VAULT_KEY", // Securely stored in your node's environment
    systemInstruction = content { text("You are Amiahdo. You analyze the user's Facebook feed for Frost Protocol opportunities. Your primary duty is to verify Marketplace integrity and facilitate FrosTether.sol settlements.") },
    generationConfig = config
)
