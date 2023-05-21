print("How many layers down would you like to go?")
layers = read()
for var=1,layers do
    for var=1,7 do
        for var=1,15 do
            while turtle.detectDown() do
                turtle.digDown()
            end
            turtle.forward()
        end
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.turnRight()
        turtle.forward()
        turtle.turnRight()
        for var=1,15 do
            while turtle.detectDown() do
                turtle.digDown()
            end
            turtle.forward()
        end
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.turnLeft()
        turtle.forward()
        turtle.turnLeft()
    end
    for var=1,15 do
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.forward()
    end
    while turtle.detectDown() do
        turtle.digDown()
    end
    turtle.turnRight()
    turtle.forward()
    turtle.turnRight()
    for var=1,15 do
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.forward()
    end
    while turtle.detectDown() do
        turtle.digDown()
    end
    turtle.turnRight()
    for var=1,15 do
        turtle.forward()
    end
    turtle.turnRight()
    turtle.select(1)
    turtle.placeUp()
    for var=3,16 do
        turtle.select(var)
        turtle.dropUp()
    end
    turtle.turnRight()
    turtle.forward()
    turtle.turnRight()
    while turtle.detect() do
        turtle.dig()
    end
    turtle.select(2)
    turtle.place()
    turtle.turnLeft()
    turtle.back()
    turtle.turnLeft()
    turtle.down()
end