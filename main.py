import turtle

import pandas

from dealer import Dealer

csv = Dealer()

screen = turtle.Screen()
screen.title('U.S States Game')
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_is_on = True
record_list = []

downy = turtle.Turtle()
downy.penup()
downy.hideturtle()

while game_is_on:
    score = len(record_list)
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        missing_states = [temp for temp in csv.name if temp not in record_list]

        # for temp in csv.names:
        #     if temp not in record_list:
        #         missing_states.append(temp)

        remaining_answers = pandas.DataFrame(missing_states)
        remaining_answers.to_csv('remained_answers.csv')
        break
    elif csv.check(answer_state):
        if answer_state not in record_list:
            downy.goto(csv.x_y)
            downy.write(answer_state, True, align="center")
            record_list.append(answer_state)
        if score == 49:
            game_is_on = False
            game_prompt = screen.textinput(title="YOU WIN ! ! !",
                                           prompt="CONGRATULATIONS You Win The Game! \nWould You Like To Play Again? Type Yes/No").lower()
            if game_prompt == 'yes':
                record_list = []
                downy.clear()
                game_is_on = True


