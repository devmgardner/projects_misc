---
--- Created by devingardner.
--- DateTime: 3/10/24 10:12 AM
---

monitor = peripheral.find('monitor')
monitor.setTextScale(0.5)
monitor.clear()
monitor.setCursorPos(1,1)
term.redirect(monitor)

function showHelp()
    print('to use the split program:')
    print('replace the top drawer with whatever')
    print('inventory you want to split\n')
    print('then, once the inventory is empty,')
    print('run "split start" to split it out')
end

showHelp()
