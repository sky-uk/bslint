sub main()
    screen = CreateObject("roSGScreen)
    port = CreateObject("roMessagePort")
    screen.setMessagePort(port)

    scene = screen.CreateScene("SampleScene)
    screen.show()

    while true
        ' do stuff
    end while

end sub