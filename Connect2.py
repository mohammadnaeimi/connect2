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
        for i in range(len(n)):
            if i != 0 and i != 7:
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

    def play(self): # calculates the values of each child node based on first move
        listt = []
        listv = []
        movalue, mxvalue, novalue, nxvalue, tovalue, txvalue = 0, 0, 0, 0, 0, 0
        x = self.child_nodes(self.gamestate, 1)
        for i in x:
            m = self.child_nodes(i, -1)
            movalue = movalue + novalue
            mxvalue = mxvalue + nxvalue
            novalue = 0
            nxvalue = 0
            print(mxvalue, movalue)
            for j in m:
                n = self.child_nodes(j, 1)
                novalue = novalue + tovalue
                nxvalue = nxvalue + txvalue
                tovalue = 0
                txvalue = 0
                for k in n:
                    k = [-1 if i == 0 else i for i in k]
                    tovalue = self.value(k)[0]
                    txvalue = self.value(k)[1]
                    listv.append([tovalue, txvalue])
                    listt.append(k)
        return



def main():
    g = Game()
    print(g.play())

if __name__ == '__main__':
    main()
