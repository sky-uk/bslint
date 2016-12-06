function TestClass() as object
    if m.TestClass = invalid then
        obj = CreateObject("roAssociativeArray")
        obj.var = true

        m.TestClass = obj
    end if

    return m.TestClass
end function