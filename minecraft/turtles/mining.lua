turtle.refuel()
print("Refueled turtle!")
print("Enter how far you would like the first tunnel to be")
first_tunnel = read()
print("Enter how long you would like each branch to be")
each_branch = read()
print("Enter how many branches you would like to dig")
total_branches = read()

for var=1,first_tunnel do
    turtle.dig()
    turtle.turnRight()
    turtle.forward()
    turtle.turnLeft()
    turtle.dig()
    turtle.down()
    turtle.dig()
    turtle.turnLeft()
    turtle.forward()
    turtle.turnRight()
    turtle.dig()
    turtle.up()
    turtle.forward()
end
for var=1,first_tunnel do
    turtle.back()
end

turtle.back()

for var=1,total_branches do
    turtle.turnLeft()
    for var=1,each_branch do
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        --inventory check
        if turtle.getItemCount(16)>0 then
            turtle.select(1)
            turtle.back()
            if turtle.detectDown() then
                turtle.digDown()
            end
            turtle.placeDown()
            for var=2,16 do
                turtle.select(var)
                turtle.dropDown()
            end
            turtle.forward()
        --end inventory check
        turtle.turnRight()
        turtle.forward()
        turtle.turnLeft()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        --inventory check
        if turtle.getItemCount(16)>0 then
            turtle.select(1)
            turtle.back()
            if turtle.detectDown() then
                turtle.digDown()
            end
            turtle.placeDown()
            for var=2,16 do
                turtle.select(var)
                turtle.dropDown()
            end
            turtle.forward()
        --end inventory check
        turtle.down()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        --inventory check
        if turtle.getItemCount(16)>0 then
            turtle.select(1)
            turtle.back()
            if turtle.detectDown() then
                turtle.digDown()
            end
            turtle.placeDown()
            for var=2,16 do
                turtle.select(var)
                turtle.dropDown()
            end
            turtle.forward()
        --end inventory check
        turtle.turnLeft()
        turtle.forward()
        turtle.turnRight()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        --inventory check
        if turtle.getItemCount(16)>0 then
            turtle.select(1)
            turtle.back()
            if turtle.detectDown() then
                turtle.digDown()
            end
            turtle.placeDown()
            for var=2,16 do
                turtle.select(var)
                turtle.dropDown()
            end
            turtle.forward()
        --end inventory check
        turtle.up()
        turtle.forward()
    end
    for var=1,each_branch do
        turtle.back()
    end
    turtle.turnLeft()
    turtle.turnLeft()
    turtle.forward()
    turtle.forward()
    for var=1,each_branch do
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        --inventory check
        if turtle.getItemCount(16)>0 then
            turtle.select(1)
            turtle.back()
            if turtle.detectDown() then
                turtle.digDown()
            end
            turtle.placeDown()
            for var=2,16 do
                turtle.select(var)
                turtle.dropDown()
            end
            turtle.forward()
        --end inventory check
        turtle.turnLeft()
        turtle.forward()
        turtle.turnRight()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        --inventory check
        if turtle.getItemCount(16)>0 then
            turtle.select(1)
            turtle.back()
            if turtle.detectDown() then
                turtle.digDown()
            end
            turtle.placeDown()
            for var=2,16 do
                turtle.select(var)
                turtle.dropDown()
            end
            turtle.forward()
        --end inventory check
        turtle.down()
        while turtle.detect() do
            turtle.dig()
        end
        turtle.turnRight()
        turtle.forward()
        turtle.turnLeft()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        --inventory check
        if turtle.getItemCount(16)>0 then
            turtle.select(1)
            turtle.back()
            if turtle.detectDown() then
                turtle.digDown()
            end
            turtle.placeDown()
            for var=2,16 do
                turtle.select(var)
                turtle.dropDown()
            end
            turtle.forward()
        --end inventory check
        turtle.up()
        turtle.forward()
    end
    for var=1,each_branch do
        turtle.back()
    end
    turtle.back()
    turtle.back()
    turtle.turnLeft()
    turtle.forward()
    turtle.forward()
    turtle.forward()
    turtle.forward()
end
--while turtle.detectDown() do
--    print("Digging down!")
--    turtle.digDown()
--    print("Going down!")
--    turtle.down()
--    print("Digging forward!")
--    turtle.dig()
--    print("Going forward!")
--    turtle.forward()
--end