---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by devin gardner.
--- DateTime: 5/7/2024 8:51 PM
---

local mon = peripheral.find("monitor")
local modem = peripheral.find("modem")
mon.setTextScale(0.5)
modem.open(43)

function newLine(monitor)
    local _, cY = monitor.getCursorPos()
    monitor.setCursorPos(1, cY + 1)
end

function clearMon(monitor)
    monitor.setCursorPos(1,1)
    for var1 = 1, 32, 1 do
        for var2 = 1, 32, 1 do
            monitor.write(" ")
        end
        newLine(monitor)
    end
    monitor.setCursorPos(1, 1)
end

function commas(num)
    assert(type(num) == "number" or type(num) == "string")

    local result = ""

    local sign, before, after = string.match(tostring(num), "^([%+%-]?)(%d*)(%.?.*)$")

    while string.len (before) > 3 do
        result = "," .. string.sub(before, -3, -1) .. result
        before = string.sub(before, 1, -4)
    end

    return result
end

while(true) do
    local event, side, channel, replyChannel, message, distance
    repeat
        event, side, channel, replyChannel, message, distance = os.pullEvent("modem_message")
    until channel == 43
    clearMon(mon)
    mon.write("    Total #    ")
    newLine(mon)
    mon.write("   Enchanted   ")
    local result_num = commas(message)
    local num_spaces = math.floor((15 - string.len(result_num)) / 2)
    local space_string = string.rep(" ", num_spaces)
    local middle_string = (space_string .. result_num)
    local result_string = (middle_string .. space_string)
    mon.write(result_string)
    sleep(0.5)
end
