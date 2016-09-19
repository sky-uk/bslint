rem TODO ZRV Check fgdfgdfg
sub main()
    screen = CreateObject("roSGScreen")
    port = CreateObject("roMessagePort")
    screen.setMessagePort(port)

    scene = screen.CreateScene("SampleScene")
    screen.show()

    while true
    end while

end sub

' TODO PFU valid