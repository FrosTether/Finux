# 1. Clean the workspace for the new target
rm frosku_viral.zip source/main.brs manifest

# 2. Generate the Manifest
echo "title=FrostBite Viral Edition" > manifest
echo "major_version=1" >> manifest
echo "minor_version=0" >> manifest
echo "build_version=1" >> manifest
echo "mm_icon_focus_hd=pkg:/images/icon.png" >> manifest

# 3. Create the Icon (Critical to prevent install failure)
mkdir -p images
echo "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==" | base64 -d > images/icon.png

# 4. Create the "Blue Menu" Payload
cat << 'EOF' > source/main.brs
sub Main()
    port = CreateObject("roMessagePort")
    screen = CreateObject("roPosterScreen")
    screen.SetMessagePort(port)
    screen.SetListStyle("flat-category")
    
    content = [
        { ShortDescriptionLine1: "⚠️ TARGET LOCKED: 192.168.0.7 ⚠️", ShortDescriptionLine2: "Roku 4 System Compromised." },
        { ShortDescriptionLine1: "INJECTION STATUS", ShortDescriptionLine2: "Payload Active. USB Bypass Unnecessary." }
    ]
    
    screen.SetContentList(content)
    screen.Show()
    
    while true
        msg = wait(0, port)
        if type(msg) = "roPosterScreenEvent" and msg.isScreenClosed() then exit while
    end while
end sub
EOF

# 5. Package and Launch
zip -r frosku_viral.zip manifest source/ images/
curl --user rokudev:jeww --digest -v -F "archive=@frosku_viral.zip" -F "mysubmit=Install" http://192.168.0.7/plugin_install
