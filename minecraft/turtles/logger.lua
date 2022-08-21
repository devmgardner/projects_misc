for h=1,7 do
    turtle.up()
end
for mainloop=1,7 do
    for times=1,8 do
        for length=1,18 do
            while turtle.detectDown() do
                turtle.digDown()
            end
            turtle.forward()
        end
        turtle.turnRight()
        turtle.forward()
        turtle.turnRight()
        for length=1,18 do
            while turtle.detectDown() do
                turtle.digDown()
            end
            turtle.forward()
        end
        turtle.turnLeft()
        turtle.forward()
        turtle.turnLeft()
    end
    for length=1,18 do
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.forward()
    end
    turtle.turnRight()
    turtle.forward()
    turtle.turnRight()
    for length=1,18 do
        while turtle.detectDown() do
            turtle.digDown()
        end
        turtle.forward()
    end
    turtle.turnRight()
    for length=1,18 do
        turtle.forward()
    end
    turtle.turnRight()
    turtle.down()
end
turtle.back()
turtle.back()
for var=2,16 do
    turtle.select(var)
    turtle.dropRight()
end