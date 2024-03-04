---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by devingardner.
--- DateTime: 3/2/24 11:29 AM
---

-- setting monitor and getting arguments
monitor = peripheral.find("monitor")
monitor.setTextScale(0.5)
local args = {...}

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

if #args == 1 then
    if args[1] == "open" then
        local currentVal = rs.getBundledOutput("right")
        currentVal = currentVal + 8
        rs.setBundledOutput("right", currentVal)
        return
    elseif args[1] == "close" then
        local currentVal = rs.getBundledOutput("right")
        currentVal = currentVal - 8
        rs.setBundledOutput("right", currentVal)
        return
    else
        showHelp()
        return
    end
end

if #args < 7 then
    -- display help message
    showHelp()
    return
else
    -- getting input variables
    val = 4112
    local inp_fans = args[1]
    local inp_masher = args[2]
    local inp_skeleton = args[3]
    local inp_zombie = args[4]
    local inp_spider = args[5]
    --local inp_shulker = args[6]
    local inp_ender = args[6]
    local inp_wither_skeleton = args[7]

    -- fans
    monitor.setTextColor(4096)
    monitor.write("fans: ")
    if inp_fans == "1" then
        val = val - 4096
        monitor.setTextColor(32)
        monitor.write("True")
        monitor.setTextColor(1)
        newLine()
    else
        monitor.setTextColor(16384)
        monitor.write("False")
        monitor.setTextColor(1)
        newLine()
    end

    -- masher
    monitor.setTextColor(16)
    monitor.write("masher: ")
    if inp_masher == "1" then
        val = val - 16
        monitor.setTextColor(32)
        monitor.write("True")
        monitor.setTextColor(1)
        newLine()
    else
        monitor.setTextColor(16384)
        monitor.write("False")
        monitor.setTextColor(1)
        newLine()
    end

    -- skeleton
    monitor.setTextColor(16384)
    monitor.write("skeleton: ")
    if inp_skeleton == "1" then
        val = val + 16384
        monitor.setTextColor(32)
        monitor.write("True")
        monitor.setTextColor(1)
        newLine()
    else
        monitor.setTextColor(16384)
        monitor.write("False")
        monitor.setTextColor(1)
        newLine()
    end

    -- zombie
    monitor.setTextColor(1024)
    monitor.write("zombie: ")
    if inp_zombie == "1" then
        val = val + 1024
        monitor.setTextColor(32)
        monitor.write("True")
        monitor.setTextColor(1)
        newLine()
    else
        monitor.setTextColor(16384)
        monitor.write("False")
        monitor.setTextColor(1)
        newLine()
    end

    -- spider
    monitor.setTextColor(1)
    monitor.write("spider: ")
    if inp_spider == "1" then
        val = val + 32768
        monitor.setTextColor(32)
        monitor.write("True")
        monitor.setTextColor(1)
        newLine()
    else
        monitor.setTextColor(16384)
        monitor.write("False")
        monitor.setTextColor(1)
        newLine()
    end

    -- shulker
    --monitor.setTextColor(128)
    --monitor.write("shulker: ")
    --if inp_shulker == "1" then
    --    val = val + 128
    --    monitor.setTextColor(32)
    --    monitor.write("True")
    --    monitor.setTextColor(1)
    --    newLine()
    --else
    --    monitor.setTextColor(16384)
    --    monitor.write("False")
    --    monitor.setTextColor(1)
    --    newLine()
    --end

    -- enderman
    monitor.setTextColor(8192)
    monitor.write("enderman: ")
    if inp_ender == "1" then
        val = val + 8192
        monitor.setTextColor(32)
        monitor.write("True")
        monitor.setTextColor(1)
        newLine()
    else
        monitor.setTextColor(16384)
        monitor.write("False")
        monitor.setTextColor(1)
        newLine()
    end

    -- wither skeleton
    monitor.setTextColor(64)
    monitor.write("wither skeleton: ")
    if inp_wither_skeleton == "1" then
        val = val + 64
        monitor.setTextColor(32)
        monitor.write("True")
        monitor.setTextColor(1)
        newLine()
    else
        monitor.setTextColor(16384)
        monitor.write("False")
        monitor.setTextColor(1)
        newLine()
    end

    rs.setBundledOutput("right", val)
end
