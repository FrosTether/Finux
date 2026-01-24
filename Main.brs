sub Main()
    screen = CreateObject("roSGScreen")
    m.port = CreateObject("roMessagePort")
    screen.SetMessagePort(m.port)

    scene = screen.CreateScene("FrostScene")
    screen.show()

    ' Simple Menu Setup
    menu = scene.findNode("frostMenu")
    menu.content = createObject("RoSGNode", "ContentNode")
    
    ' Adding "Frost" styled menu items
    items = ["NETWORK STATUS", "CRYPTO WALLET", "REMOTE RESTART", "TERMINAL"]
    for each item in items
        node = menu.content.createChild("ContentNode")
        node.title = item
    end for

    menu.setFocus(true)

    while(true)
        msg = wait(0, m.port)
        if type(msg) = "roSGScreenEvent"
            if msg.isScreenClosed() then return
        end if
    end while
end sub
