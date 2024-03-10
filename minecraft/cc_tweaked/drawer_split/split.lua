---
--- Created by devingardner.
--- DateTime: 3/10/24 07:54 AM
---

--monitor = peripheral.find('monitor')
--monitor.clear()
--monitor.setCursorPos(1,1)
--monitor.setTextScale(0.5)
--term.redirect(monitor)

--local args = {...}

--function showHelp()
--    print('to use the split program:')
--    print('replace the top drawer with whatever')
--    print('inventory you want to split\n')
--    print('then, once the inventory is empty,')
--    print('run "split start" to split it out')
--end

function doSplit()
    local input_inv = peripheral.wrap('storagedrawers:standard_drawers_1_5')
    local input_count = input_inv.getItemDetail(2)['count']
    local move_count = math.floor(input_count / 4)
    local remainder = input_count - (move_count * 3)
    input_inv.pushItems('storagedrawers:standard_drawers_1_7', 2, move_count, 2)
    input_inv.pushItems('storagedrawers:standard_drawers_1_6', 2, move_count, 2)
    input_inv.pushItems('storagedrawers:standard_drawers_1_4', 2, move_count, 2)
    input_inv.pushItems('storagedrawers:standard_drawers_1_3', 2, remainder, 2)
end

--if #args ~= 1 then
--    showHelp()
--elseif args[1] ~= 'start' then
--    showHelp()
--else
--    doSplit()
--end

while true do
    if rs.getAnalogInput("front") > 7 then
        doSplit()
        sleep(5)
    end
end
