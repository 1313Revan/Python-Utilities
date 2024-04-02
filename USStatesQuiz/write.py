from turtle import Turtle


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()

    def write_state(self, state_name, x_coord, y_coord):
        self.goto(x=int(x_coord.iloc[0]), y=int(y_coord.iloc[0]))
        self.write(arg=state_name, align="center")
