-- FROST CITADEL XMPP CONFIG
-- Port: 7444
-- Force OTR and No-Logs

VirtualHost "finux.tech"
    ssl = {
        key = "/etc/prosody/certs/finux.key";
        certificate = "/etc/prosody/certs/finux.crt";
    }

-- ENFORCE PRIVACY
modules_enabled = {
    "roster"; "saslauth"; "tls"; "dialback"; "disco";
    "private"; "vcard"; "version"; "uptime"; "time";
    "ping"; "pep"; "register"; "mam"; -- Message Archive (No-storage)
}

-- DISABLE LOGGING (Memory Only)
logging = {
    error = "*syslog";
    "*console";
}

c2s_ports = { 7444 }
allow_registration = false
