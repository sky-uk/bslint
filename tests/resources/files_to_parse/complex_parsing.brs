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
        c = 3
    end if

    if requiresUpdate then showRequiresUpdateScreen()

    return requiresUpdate

end function
