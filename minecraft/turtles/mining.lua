--starts the first branch one block behind and to the left of where it starts the program
turtle.refuel()end
print("Refueled turtle!")
print("Enter how far you would like the first tunnel to be")
first_tunnel = read()
print("Enter how long you would like each branch to be")
each_branch = read()
print("Enter how many branches you would like to dig")
total_branches = read()

function forward()
    while not turtle.forward() do sleep(0.5) end
end

function back()
    while not turtle.back() do sleep(0.5) end
end

for var=1,first_tunnel do
    while turtle.detect() do
        turtle.dig()
    end
    turtle.turnRight()
    forward()
    turtle.turnLeft()
    while turtle.detect() do
        turtle.dig()
    end
    turtle.down()
    while turtle.detect() do
        turtle.dig()
    end
    turtle.turnLeft()
    forward()
    turtle.turnRight()
    while turtle.detect() do
        turtle.dig()
    end
    turtle.up()
    forward()
end
for var=1,first_tunnel do
    back()
end

back()

for var=1,total_branches do
    turtle.turnLeft()
    for var=1,each_branch do
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        turtle.turnRight()
        forward()
        turtle.turnLeft()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        turtle.down()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        turtle.turnLeft()
        forward()
        turtle.turnRight()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        turtle.up()
        forward()
    end
    for var=1,each_branch do
        back()
    end
    turtle.turnLeft()
    turtle.turnLeft()
    forward()
    --forward()
    for var=1,each_branch do
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        turtle.turnLeft()
        forward()
        turtle.turnRight()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        turtle.down()
        while turtle.detect() do
            turtle.dig()
        end
        turtle.turnRight()
        forward()
        turtle.turnLeft()
        --dig statement
        while turtle.detect() do
            turtle.dig()
        end
        --end dig statement
        turtle.up()
        forward()
    end
    for var=1,each_branch do
        back()
    end
    back()
    --back()
    turtle.select(1)
    turtle.placeDown()
    for var=2,16 do
        turtle.select(var)
        turtle.dropDown()
    end
    turtle.turnLeft()
    forward()
    forward()
    forward()
    forward()
    print("Sanity check! Starting new branch now.")
    --turtle.turnLeft()
    --forward()
    --turtle.turnRight()
end
--while turtle.detectDown() do
--    print("Digging down!")
--    turtle.digDown()
--    print("Going down!")
--    turtle.down()
--    print("Digging forward!")
--    turtle.dig()
--    print("Going forward!")
--    forward()
--end