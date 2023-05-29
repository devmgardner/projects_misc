--starts at the bottom left of the chunk, and does 16x16xZturtle.back()
print("How many layers down would you like to go?")
layers = read()

function forward()
    while not turtle.forward() do sleep(0.5) end
end

function back()
    while not turtle.back() do sleep(0.5) end
end

for var=1,layers do
    for var=1,7 do
        for var=1,15 do
            while turtle.detectDown() do
                turtle.digDown()
            end
            forward()
        end
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.turnRight()
        forward()
        turtle.turnRight()
        for var=1,15 do
            while turtle.detectDown() do
                turtle.digDown()
            end
            forward()
        end
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.turnLeft()
        forward()
        turtle.turnLeft()
    end
    for var=1,15 do
        while turtle.detectDown() do
            turtle.digDown()
        end
        forward()
    end
    while turtle.detectDown() do
        turtle.digDown()
    end
    turtle.turnRight()
    forward()
    turtle.turnRight()
    for var=1,15 do
        while turtle.detectDown() do
            turtle.digDown()
        end
        forward()
    end
    while turtle.detectDown() do
        turtle.digDown()
    end
    turtle.turnRight()
    for var=1,15 do
        forward()
    end
    turtle.turnRight()
    turtle.select(1)
    turtle.placeUp()
    for var=3,16 do
        turtle.select(var)
        turtle.dropUp()
    end
    turtle.turnRight()
    forward()
    turtle.turnRight()
    while turtle.detect() do
        turtle.dig()
    end
    turtle.select(2)
    turtle.place()
    turtle.turnLeft()
    back()
    turtle.turnLeft()
    turtle.down()
end