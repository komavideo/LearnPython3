from turtle import *

color("green")
shape("turtle")

speed(5) # 慢
# speed(10) # 最快
# speed(0) # 极速(取消动画效果)

def star(size):
    for i in range(5):
        forward(size)
        right(180 - 180/5)

color('red')
begin_fill()
star(80)
end_fill()

up()
goto(100,100)
down()
color('green')
begin_fill()
star(80)
end_fill()

done()
