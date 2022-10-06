import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image_url = "blank_states_img.gif"
screen.addshape(image_url)
turtle.shape(image_url)

data = pandas.read_csv("50_states.csv")
all_state_list = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name ?")

    # answer의 답을 "Exit"라고 입력했을 때, 50개의 주에서 맞추지 못한 주 들을 새로운 리스트에 저장
    if answer_state.title() == "Exit":
        remain_state_list = []
        for state in all_state_list:
            if state not in guessed_states:
                remain_state_list.append(state)
        new_data = pandas.DataFrame(remain_state_list)
        new_data.to_csv("remain_state.csv")
        break

    # answer_state 와 data의 state 중에 일치하는 것이 있는지 확인
    if answer_state.title() in all_state_list:
        guessed_states.append(answer_state)
        new_t = turtle.Turtle()
        new_t.hideturtle()
        new_t.penup()
        location = data[data["state"] == answer_state]
        new_t.goto(int(location.x), int(location.y))
        new_t.write(answer_state)

screen.exitonclick()


# def get_mouse_click_coor(x, y):
#     print(x, y)

