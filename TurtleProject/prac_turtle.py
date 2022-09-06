# from turtle import Turtle, Screen


# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(50)

# # Screen() 클래스를 통해 screen 이라는 객체를 생성하여 exitonclick() 함수 기능을 사용할 수 있다.
# screen = Screen()
# screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name", ["one","two","three"])
table.add_column("Type", [1,2,3])
table.align = "l"

print(table)