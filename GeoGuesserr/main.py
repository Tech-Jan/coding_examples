import turtle
import pandas
from writer import writer

answer = pandas.read_csv("50_states.csv")
# print(answer)
state_list = answer["state"]
screen = turtle.Screen()
screen.title("Guess what bru")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
score_writer = writer()


def check_answer():
    for state in state_list:
        if answer_state.lower() == state.lower()  and answer_state.lower() not in answered_states:
            answered_states.append(answer_state.title())
            guessed_state = answer[answer["state"] == answer_state.title()]
            x, y = int(guessed_state.x), guessed_state["y"].item()
            score_writer.increase_score((x, y), guessed_state["state"].item())
            screen.title(f"{score_writer.points}/50 Guess what bru")



answered_states=[]
while len(set(answered_states)) < 50:
    answer_state = screen.textinput(f"{score_writer.points}/50 guess the sate", "what u say")
    check_answer()
    if answer_state == "exit":
        break

print("WINWINWIN")
print(answered_states)

list_of_not=answer["state"][~answer[("state")].isin(answered_states)]
print(f"these were missing {list(list_of_not)}")
list_of_not.to_csv("notknowstates.csv")
screen.exitonclick()
