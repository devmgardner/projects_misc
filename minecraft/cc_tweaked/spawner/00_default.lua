---
--- Generated by EmmyLua(https://github.com/EmmyLua)
--- Created by devin gardner.
--- DateTime: 5/4/2024 1:48 PM
---

-- setting monitor and getting arguments
monitor = peripheral.find("monitor")
monitor.setTextScale(0.5)

local funcs = require("00_funcs")

funcs.clearMon(monitor)
rs.setBundledOutput("right", 4112)

while(true) do
    vals = rs.getBundledInput("left")
    local result = funcs.processVals(vals)
    if result[2] ~= nil then
        rs.setBundledOutput("right", result[2])
    else
        funcs.cleanUp()
    end
    sleep(0.25)
end
