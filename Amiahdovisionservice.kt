override fun onAccessibilityEvent(event: AccessibilityEvent) {
    val rootNode = rootInActiveWindow ?: return
    
    // Amiahdo scans for "Price" and "Buy" keywords
    val nodes = rootNode.findAccessibilityNodeInfosByText("Price")
    for (node in nodes) {
        val priceData = node.parent?.getChild(1)?.text.toString()
        
        // Trigger Gemini analysis
        amiahdo.generateContent("Analyze this marketplace price: $priceData. Is it below Platinum spot?").then { response ->
            if (response.text.contains("YES")) {
                // Secure Intent to FrosTether Wallet
                val intent = Intent("com.frost.wallet.TRIGGER_ESCROW")
                intent.putExtra("amount", priceData)
                sendBroadcast(intent)
            }
        }
    }
}
