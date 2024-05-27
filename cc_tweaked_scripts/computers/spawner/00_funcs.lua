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

local function cleanUp()
    rs.setBundledOutput("right", 4112)
    sleep(5)
    rs.setBundledOutput("right", 0)
end

local function processVals(num)
    local allVals = {
        [1] = 32768,
        [2] = 16384,
        [3] = 8192,
        [4] = 4096,
        [5] = 1024,
        [6] = 512,
        [7] = 64,
        [8] = 32,
        [9] = 16,
        [10] = 8,
        [11] = 4
    }
    local returnVal = 0
    local calcVal = num
    while(calcVal > 4) do
        for _, minusVal in ipairs(allVals) do
            if calcVal >= minusVal then
                returnVal = returnVal + minusVal
                calcVal = calcVal - minusVal
            end
        end
    end
    if calcVal == 3 then
        return {
            [1] = "cleanup"
        }
    elseif calcVal == 2 then
        return {
            [1] = "cleanup"
        }
    else
        return {
            [1] = "start",
            [2] = returnVal
        }
    end
end

return { newLine = newLine, clearMon = clearMon, cleanUp = cleanUp, processVals = processVals }