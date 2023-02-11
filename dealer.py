import pandas


class Dealer():

    def __init__(self):
        self.data = pandas.read_csv('50_states.csv')
        self.names = self.data['state'].to_list()
        self.x_y = ()

    def check(self, guess):
        id = 0
        for state in self.names:
            if state == guess:
                x = (self.data['x'].iloc[id])
                y = (self.data['y'].iloc[id])
                self.x_y = x, y
                return True
            id += 1

