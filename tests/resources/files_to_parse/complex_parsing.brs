sub Main(args as Dynamic)
    m.port = CreateObject("roMessagePort")
    m.atlasScreen = showScene("AtlasScene")

    _appContext = AppContext()
    _appContext.init(m.AtlasScene, m.port, args)

    messageBus = Atlantis().messageBus
    m.isRunning = true
    while(m.isRunning)
        msg = wait(10, m.port)

        m.messageBus.dispatchEvent(Event(TimerContext().TIMER_TICK))

        msgType = type(msg)

        if msgType = "roSGNodeEvent"
            m.messageBus.dispatchEvent(Event(msg.getNode()+"Event", {property: msg.getField(), data: msg.getData()}))
        else if msgType = "roUrlEvent"
            if msg.GetInt() = 1
                m.messageBus.dispatchEvent( Event("roUrlEvent", {
                                            sourceIdentity: msg.GetSourceIdentity(),
                                            responseCode: msg.GetResponseCode(),
                                            failureReason: msg.GetFailureReason(),
                                            data: msg.getString(),
                                            responseHeadersArray:msg.GetResponseHeadersArray()
                                            }))
            end if
        else if msgType = "roDeviceInfoEvent"
            m.messageBus.dispatchEvent(Event(DeviceInfoContext().NETWORK_CHANGE, msg))
        end if
    end while
end sub

sub closeApp()
    m.isRunning = false
    m.atlasScreen.close()
end sub

function showScene(_sceneName as String) as Object
    screen = CreateObject("roSGScreen")
    screen.setMessagePort(m.port)

    'until Roku fix a bug with being unable to access scene using screen.GetScene()
    m[_sceneName] = screen.CreateScene(_sceneName)

    screen.show()

    m[_sceneName].id = _sceneName

    return screen
end function

function closeScreen(_screenName as String, _sceneName as String) as Void
    m[_screenName] = Invalid

    'until Roku fix a bug with being unable to access scene using screen.GetScene()
    m[_sceneName] = Invalid
end function

function firmwareRequiresUpdate() as boolean
    'First firmware release with SceneGraph SDK2.0 support is 6.0.
    majorRequirement = 6
    minorRequirement = 0
    buildRequirement = 0

    version = CreateObject("roDeviceInfo").GetVersion()

    print("Firmware Version Found: " + version)

    major = Mid(version, 3, 1)
    minor = Mid(version, 5, 2)
    build = Mid(version, 8, 5)

    print("Major Version: " + major + " Minor Version: " + minor + " Build Number: " + build)

    requiresUpdate = false
    if Val(major) < majorRequirement then
        requiresUpdate = true
    else if Val(major) = majorRequirement then
        if Val(minor) < minorRequirement then
            requiresUpdate = true
        else if Val(minor) = minorRequirement then
            if Val(build) < buildRequirement
                requiresUpdate = true
            end if
        end if
    end if

    if requiresUpdate then showRequiresUpdateScreen()

    return requiresUpdate

end function

sub showRequiresUpdateScreen()
    port = CreateObject("roMessagePort")
    screen = CreateObject("roParagraphScreen")
    screen.SetMessagePort(port)
    screen.AddHeaderText("Roku software update required")
    screen.AddParagraph("In order to use this channel, you must update the software on your Roku player.  To update your software:")
    screen.AddParagraph("1.  Select " + chr(34) + "settings" + chr(34) + " from the Roku home screen.")
    screen.AddParagraph("2.  Select " + chr(34) + "player info." + chr(34))
    screen.AddParagraph("3.  Select " + chr(34) + "check for update." + chr(34))
    screen.AddParagraph("4.  Select " + chr(34) + "yes." + chr(34))
    screen.AddParagraph("5. Once your Roku player has finished updating, you may use this channel.")
    screen.AddButton(1, "back")
    screen.Show()

    while true
        msg = wait(0, screen.GetMessagePort())
        if type(msg) = "roParagraphScreenEvent"
            if msg.isScreenClosed()
                print "Screen closed"
            else if msg.isButtonPressed()
                print "Button pressed: "; msg.GetIndex(); " ";msg.GetData()
            else
                print "Unknown event: "; msg.GetType(); " msg: "; msg.GetMessage()
            endif
            exit while
        endif
    end while
end sub
