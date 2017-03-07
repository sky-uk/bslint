function init()
	m.top.visible = false
	m.grid = m.top.findNode("grid")
	m.grid.focusBitmapUri = StyleConstants().PIXEL_IMG_TRANSPARENT
	m.top.observeField("focusedChild", "_onFocus")
	m.pageNumber = m.top.findNode("pageNumber")
end function

function _onFocus() as Void
    if nodeHasFocus(m.top)
    	forceFocus(m.grid)
    end if
end function

function generate()
	if m.top.content.data <> Invalid
		m.grid.horizFocusAnimationStyle = m.top.horizFocusAnimationStyle
		m.grid.focusColumn = m.top.focusColumn
		m.grid.focusBitmapUri = m.top.focusRectangle
		m.titleYvalue = 75 - m.top.titleFontSize
		calculateWidth()
		checkLogo()
		checkPagination()

		positionGrid()

		checkItems()
	end if

	m.top.visible = true
	m.top.generate = false
end function

function checkLogo()
	m.title = m.top.findNode("title")
	m.title.font.size = m.top.titleFontSize

	if m.top.showLogo = true
		m.top.findNode("logo").uri = m.top.logo
		m.title.text = "| " + m.top.title
		m.title.translation= "[150," + m.titleYvalue.toStr() + "]"
	else
		m.title.text = m.top.title
		m.title.translation="[15," + m.titleYvalue.toStr() + "]"
	end if
end function

function positionGrid()
	if m.title.text <> ""
		m.grid.translation = "[0," + (m.titleYvalue + 50).toStr() + "]"
	else
		m.grid.translation = "[0, 0]"
		m.pageNumber.translation = "[" + (m.top.width - 142).toStr()+ ",0]"
	end if
end function

function checkPagination()
	if m.top.showPagination = true and (m.top.hidePaginationIfNoItems = false or (m.top.hidePaginationIfNoItems = true and m.top.content.data.count() > 0))
		m.pageNumber.font.size = m.top.titleFontSize
		m.arrayCount = ""
		m.pageNumber.translation = "[" + (m.top.width - 122).toStr()+ "," + m.titleYvalue.toStr() + "]"
		m.arrayCount = m.top.content.data.count().toStr()
		m.pageNumber.text =  "1 " + getTextById("grid.label.pageNumber") + " " + m.arrayCount
	end if
end function

function onItemFocused()
	if m.top.content <> Invalid and m.top.content.data <> Invalid

		focusedChild = m.grid.content.getChild(m.grid.itemFocused)
		if focusedChild <> Invalid
			focusedChild.resizeFactor = m.top.focusedResizeFactor
			if m.top.showPagination = true and (m.top.hidePaginationIfNoItems = false or (m.top.hidePaginationIfNoItems = true and m.top.content.data.count() > 0))
				m.pageNumber.text = (m.grid.itemFocused + 1).toStr()  + " " + getTextById("grid.label.pageNumber") + " " + m.arrayCount
			end if
		end if
	end if
	m.top.itemChanged = m.top.itemFocused
end function

function onItemUnfocused()
	if m.grid.itemUnfocused <> -1
		unfocusedChild = m.grid.content.getChild(m.grid.itemUnfocused)
		unfocusedChild.resizeFactor = 1
	end if
end function

function checkItems()
	items = m.top.content.data

	catalogueContentNode = createObject("RoSGNode", "ContentNode")
	for each item in items
		newNode = catalogueContentNode.createChild("ItemInterface")
		newNode.itemContent = item
		newNode.resizeFactor = 1
		newNode.focusedResizeFactor = m.top.focusedResizeFactor
		newNode.width = m.top.gridItemWidth
		newNode.height = m.top.gridItemHeight
		newNode.staticText = m.top.staticText
		newNode.theme = m.top.theme
	end for
	m.grid.content = catalogueContentNode

	m.grid.itemSize = "[" + (m.top.gridItemWidth * m.top.focusedResizeFactor).ToStr() + "," + (m.top.gridItemHeight * m.top.focusedResizeFactor).ToStr() +"]"
end function

function calculateWidth()
	m.top.width = m.top.numColumns * (m.top.gridItemWidth + Int(m.top.itemSpacing[0]))
end function
