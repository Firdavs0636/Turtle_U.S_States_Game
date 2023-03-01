import pandas


class Dealer():

    def __init__(self):
        self.data = pandas.read_csv('50_states.csv')
        self.names = self.data.state.to_list()
        self.x_y = ()

    def check(self, guess):
        for i, state in enumerate(self.names):
            if state == guess:
                x = (self.data['x'].iloc[i])
                y = (self.data['y'].iloc[i])
                self.x_y = x, y
                return True

