import turtle as t

#스크린 객체 생성
screen = t.Screen()

#울타리 그리기
mypen = t.Turtle()
mypen.penup()
mypen.setposition(-300, 300)
mypen.pendown()
mypen.pensize(3)
for x in range(4):
    mypen.forward(600)
    mypen.right(90)
mypen.hideturtle()

#선 그은 횟수를 기록하는 변수
line_count = 0

#Turtle 객체 생성
p = t.Turtle()

#p 객체의 모양을 거북이로 설정
p.shape("turtle")

#거북이 조작 함수 선언
def turnleft():
    p.left(20)
    global line_count
    line_count += 1
def turnright():
    p.right(20)
    global line_count
    line_count += 1
def go():
    p.forward(10)
    global line_count
    line_count += 1
def back():
    p.backward(10)
    global line_count
    line_count += 1
def pendown():
    p.pendown
def penup():
    p.penup

#거북이 조작 
screen.listen()
screen.onkey(turnleft, "Left")
screen.onkey(turnright, "Right")
screen.onkey(go, "Up")
screen.onkey(back, "Down")
screen.onkey(pendown, "d")
screen.onkey(penup, "s")

#점수 매기기
def score():
    if  line_count >= 90:
        grade = 'A등급 입니다! 축하합니다.'
    elif line_count >= 70 and line_count <= 89:
        grade = 'B등급 입니다!'
    elif line_count >= 50 and line_count <= 69:
        grade = 'C등급 입니다.'
    elif line_count  >= 20 and line_count <= 49:
       grade = 'D등급 입니다.'
    else:
        grade = 'E등급 입니다. 분발하세요.'
    print(grade)


screen.onkey(score,"g")
screen.mainloop()
