sub function_name()
  bcConfig = Config()
  bcConfig.initTheme()

  screenFacade = CreateObject("roPosterScreen")
  screenFacade.showMessage("Loading...")
  screenFacade.show()

  ' show the title
  screenFacade.SetBreadcrumbText(bcConfig.appName, "")

  if bcConfig.useSmartPlayer
    playlistData = BrightcoveMediaAPI().GetPlaylistConfig()
  else
    playlistData = BrightcovePlayerAPI().GetPlaylistData()
  end if

  if playlistData = invalid
    ShowConnectionFailed()
  else
    print "Found "; playlistData.playlists.count(); " playlists to display"
    HomeScreen(bcConfig.appName, "", playlistData.playlists, playlistData.thumbs)
  end if
  screenFacade.showMessage("")
  sleep(25)
end sub