---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by devingardner.
--- DateTime: 3/2/24 3:41 PM
---

rs.setBundledOutput("right", 4112)
monitor = peripheral.find("monitor")
monitor.setTextScale(0.5)

function newLine()
    local _, cY= monitor.getCursorPos()
    monitor.setCursorPos(1,cY+1)
end

function clearMon()
    monitor.setCursorPos(1,1)
    for var1=1,38,1 do
        for var2=1,36,1 do
            monitor.write(" ")
        end
        newLine()
    end
    monitor.setCursorPos(1,1)
end

function showHelp()
    monitor.write("usage:")  -- 1
    newLine()
    monitor.write("enter a sequence of space-separated ")  -- 2
    newLine()
    monitor.write("1s (on) and 0s (off) for:")  -- 3
    newLine()
    newLine()  -- 4
    monitor.setTextColor(4096)
    monitor.write("fans on/off")  -- 5
    newLine()
    monitor.setTextColor(16)
    monitor.write("masher on/off")  -- 6
    newLine()
    monitor.setTextColor(16384)
    monitor.write("skeleton on/off")  -- 7
    newLine()
    monitor.setTextColor(1024)
    monitor.write("zombie on/off")  -- 8
    newLine()
    monitor.setTextColor(1)
    monitor.write("spider on/off")  -- 9
    newLine()
    --monitor.setTextColor(128)
    --monitor.write("shulker on/off")  -- 10
    --newLine()
    monitor.setTextColor(8192)
    monitor.write("enderman on/off")  -- 11
    newLine()
    monitor.setTextColor(64)
    monitor.write("wither skeleton on/off")  -- 12
    newLine()
    newLine()  -- 13
    monitor.setTextColor(1)
    monitor.write("for example, to run the fans and")  -- 14
    newLine()
    monitor.write("masher and only spawn spiders:")  -- 15
    newLine()
    newLine()  -- 16
    monitor.write("spawner 1 1 0 0 1 0 0")  -- 17
    rs.setBundledOutput("right", 4112)
    return
end

clearMon()
showHelp()