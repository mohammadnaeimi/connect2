import numpy
import random
import time
import copy

class Game():
    def __init__(self):
        self.gamestate = [0, 1, 0, -1, -1, 0, 1, 0] # the state where the games starts
        return

    def intial_state(self):
        listl = [0, 1, 0, -1, -1, 0, 1, 0] # a functions that returns the initial state
        return listl

    def get_value(self, n): # returns the value of each terminal node
        x = 0
        for i in range(len(n)):
            if i == 0:
                if n[i] + n[i + 1] > 1:
                    x = x + 1

            if i == 7:
                if n[i] + n[i - 1] > 1:
                    x = x + 1

            else:
                if n[i] + n[i + 1] > 1 or n[i] + n[i - 1] > 1:
                    x = x + 1
        return x

    def child_nodes(self, n, m): # returns a list of all possible actions (m = 1 for O(Computer) and m = -1 for X(User))
        listl = []
        x = copy.deepcopy(n)
        for i in range(len(n)):
            if n[i] == 0:
                x[i] = m
                listl.append(x)
                x = copy.deepcopy(n)
        return listl

    def value(self, n): # returns the value of the terminal nodes as a tuple (if it is a tie the computer wins)
        O = 0
        X = 0
        for i in range(0, 7):
            if i == 0:
                if n[i] == n[i + 1] == n[i + 2] == -1:
                    X = X + 1
                if n[i] == n[i + 1] == n[i + 2] == 1:
                    O = O + 1
            if i == 7:
                if n[i] == n[i - 1] == n[i - 2] == -1:
                    X = X + 1
                if n[i] == n[i - 1] == n[i - 2] == 1:
                    O = O + 1
            else:
                if n[i - 1] == n[i] == n[i + 1] == -1:
                    X = X + 1
                if n[i - 1] == n[i] == n[i + 1] == 1:
                    O = O + 1
        if O == X:
            O = 1
            X = 0
        if O > X:
            O = 1
            X = 0
        if O < X:
            O = 0
            X = 1
        return O, X

    def get_action(self, n, m): # gets an intiger as the place of m = 1 or -1 and returns the child node
        x = int(input('where do you want to place?'))
        if n[x] == 0:
            n[x] = m
            return n

    def simulation(self, current_state): # Simulates the entire game from the given node and returns the number of wins on each side
        listt = []
        listv = []
        count_step = current_state.count(0)
        movalue, mxvalue, tovalue, txvalue = 0, 0, 0, 0
        if count_step == 4:
            x = self.child_nodes(current_state, 1)
            for i in x:
                m = self.child_nodes(i, -1)
                for j in m:
                    n = self.child_nodes(j, 1)
                    for k in n:
                        k = [-1 if i == 0 else i for i in k]
                        tovalue = self.value(k)[0]
                        txvalue = self.value(k)[1]
                        movalue = tovalue + movalue
                        mxvalue = txvalue + mxvalue
                        listt.append(k)
                        listv.append([tovalue, txvalue])

        if count_step == 3:
            x = self.child_nodes(current_state, -1)
            for i in x:
                n = self.child_nodes(i, 1)
                for k in n:
                    k = [-1 if i ==0 else i for i in k]
                    tovalue = self.value(k)[0]
                    txvalue = self.value(k)[1]
                    movalue = tovalue + movalue
                    mxvalue = txvalue + mxvalue
                    listt.append(k)
                    listv.append([tovalue, txvalue])
        if count_step == 2:
            x = self.child_nodes(current_state, 1)
            for k in x:
                k = [-1 if i == 0 else i for i in k]
                tovalue = self.value(k)[0]
                txvalue = self.value(k)[1]
                movalue = tovalue + movalue
                mxvalue = txvalue + mxvalue
                listt.append(k)
                listv.append([tovalue, txvalue])
        if count_step == 1:
            current_state = [-1 if i == 0 else i for i in current_state]
            tovalue = self.value(current_state)[0]
            txvalue = self.value(current_state)[1]
            movalue = tovalue + movalue
            mxvalue = txvalue + mxvalue
            listt.append(current_state)
            listv.append([tovalue, txvalue])
        return movalue, mxvalue


def main():
    g = Game()
    print(g.play([0, 1, -1, -1, -1, 1, 1, 1]))

if __name__ == '__main__':
    main()
