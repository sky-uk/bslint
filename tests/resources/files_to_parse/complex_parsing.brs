this = {
    nowNextModel: {typeOf:"NowNextModel"}
    watchLivePageMediator: {typeOf: "WatchLivePageMediator"}

    execute: function (_payload={} as Object) as Void
        nowNextItem = m.nowNextModel.getNowNextItem()

        if nowNextItem <> Invalid
            if _payload.data
                data = nowNextItem.now
            else
                data = nowNextItem.next
            end if

            data.channelLogo = nowNextItem.key.logoUrl

            m.watchLivePageMediator.setField("detailContent", data)
        end if

        m.watchLivePageMediator.setField("detailGenerate", true)
    end function
}
