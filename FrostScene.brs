sub init()
    m.priceLabel = m.top.findNode("priceLabel")
    m.refreshTimer = m.top.findNode("refreshTimer")
    m.refreshTimer.observeField("fire", "fetchFrostData")
    m.refreshTimer.control = "start"
    fetchFrostData()
end sub

sub fetchFrostData()
    url = "https://your-api-endpoint.com/frost/status" ' Replace with your real API
    readInternet = CreateObject("roUrlTransfer")
    readInternet.SetUrl(url)
    readInternet.SetCertificatesFile("common:/certs/ca-bundle.crt")
    readInternet.InitClientCertificates()
    
    json = readInternet.GetToString()
    if json <> ""
        data = ParseJson(json)
        m.priceLabel.text = "FROSTCOIN: $" + data.price.ToStr()
    end if
end sub
