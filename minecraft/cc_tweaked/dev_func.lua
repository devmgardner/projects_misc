local function newLine(mon)
    local _, cY= mon.getCursorPos()
    mon.setCursorPos(1,cY+1)
end

local function clearMon(mon)
    mon.setCursorPos(1,1)
    for var1=1,38,1 do
        for var2=1,36,1 do
            mon.write(" ")
        end
        newLine(mon)
    end
    mon.setCursorPos(1,1)
end

local function showHelp(mon)
    mon.write("usage:")  -- 1
    newLine(mon)
    mon.write("enter a sequence of space-separated ")  -- 2
    newLine(mon)
    mon.write("1s (on) and 0s (off) for:")  -- 3
    newLine(mon)
    newLine(mon)  -- 4
    mon.setTextColor(4096)
    mon.write("fans on/off")  -- 5
    newLine(mon)
    mon.setTextColor(16)
    mon.write("masher on/off")  -- 6
    newLine(mon)
    mon.setTextColor(16384)
    mon.write("skeleton on/off")  -- 7
    newLine(mon)
    mon.setTextColor(1024)
    mon.write("zombie on/off")  -- 8
    newLine(mon)
    mon.setTextColor(1)
    mon.write("spider on/off")  -- 9
    newLine(mon)
    --mon.setTextColor(128)
    --mon.write("shulker on/off")  -- 10
    --newLine(mon)
    mon.setTextColor(8192)
    mon.write("enderman on/off")  -- 11
    newLine(mon)
    mon.setTextColor(64)
    mon.write("wither skeleton on/off")  -- 12
    newLine(mon)
    newLine(mon)  -- 13
    mon.setTextColor(1)
    mon.write("for example, to run the fans and")  -- 14
    newLine(mon)
    mon.write("masher and only spawn spiders:")  -- 15
    newLine(mon)
    newLine(mon)  -- 16
    mon.write("spawner 1 1 0 0 1 0 0")  -- 17
    rs.setBundledOutput("right", 4112)
    return
end

return { newLine = newLine, clearMon = clearMon, showHelp = showHelp }