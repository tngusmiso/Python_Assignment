import turtle

n = int(input("몇각형을 그릴까요? "))
length = float(input("한 변의 길이는 얼마인가요? "))

t = turtle.Pen()
t.pencolor("black")

for i in range(n):
    t.forward(length)
    t.left(360/n)
