import numpy as np
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

    def random_intitla(self): # returns an initial state in random
        intital_state = [0 for i in range(0, 8)]
        indice = random.sample(range(8), 4)
        intital_state[indice[0]] = intital_state[indice[2]] = 1
        intital_state[indice[1]] = intital_state[indice[3]] = -1
        return intital_state

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
        for i in range(0, 8):
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

    def simulation(self, current_state): # Simulates the entire game from the given node and returns the number of wins on each side and the child nodes
        listm, listn, listt = [], [], []
        state = []
        count_step = current_state.count(0)
        if count_step == 4:
            x = self.child_nodes(current_state, 1)
            for i in x:
                m = self.child_nodes(i, -1)
                movalue, mxvalue = 0, 0
                for j in m:
                    n = self.child_nodes(j, 1)
                    novalue, nxvalue = 0, 0
                    for k in n:
                        k = [-1 if i == 0 else i for i in k]
                        tovalue = self.value(k)[0]
                        txvalue = self.value(k)[1]
                        listt.append([tovalue, txvalue])
                        novalue = novalue + tovalue
                        nxvalue = nxvalue + txvalue
                        listt.append([tovalue, txvalue])
                    movalue = movalue + novalue
                    mxvalue = mxvalue + nxvalue
                    listn.append([novalue, nxvalue])
                listm.append([movalue, mxvalue])
            state.append(x)

        if count_step == 3:
            x = self.child_nodes(current_state, -1)
            for i in x:
                movalue, mxvalue = 0, 0
                n = self.child_nodes(i, 1)
                for k in n:
                    k = [-1 if i ==0 else i for i in k]
                    tovalue = self.value(k)[0]
                    txvalue = self.value(k)[1]
                    movalue = tovalue + movalue
                    mxvalue = txvalue + mxvalue
                    listt.append([tovalue, txvalue])
                listm.append([movalue, mxvalue])
            state.append(x)
        if count_step == 2:
            x = self.child_nodes(current_state, 1)
            for k in x:
                k = [-1 if i == 0 else i for i in k]
                tovalue = self.value(k)[0]
                txvalue = self.value(k)[1]
                listm.append([tovalue, txvalue])
            state.append(x)
        if count_step == 1:
            current_state = [-1 if i == 0 else i for i in current_state]
            tovalue = self.value(current_state)[0]
            txvalue = self.value(current_state)[1]
            listm.append([tovalue, txvalue])
            state.append(current_state)
        return listm, state

    def check_winner(self, n):
        for i in range(len(n)):
            if i == 0:
                if n[i] == n[i + 1] == n[i + 2] == -1:
                    return 'the winner is Bob'
                if n[i] == n[i + 1] == n[i + 2] == 1:
                    return 'the winner is Alice'

            if i == 7:
                if n[i - 2] == n[i - 1] == n[i] == -1:
                    return 'the winner is Bob'
                if n[i - 2] == n[i - 1] == n[i] == 1:
                    return 'the winner is Alice'
            else:
                if n[i] == n[i + 1] == n[i + 2] == -1:
                    return 'the winner is Bob'
                if n[i] == n[i + 1] == n[i + 2] == 1:
                    return 'the winner is Alice'
        else:
            return 'the winner is Alice'


    def play(self, intital_state): #for now: starts the game with printing the intitial state, then appends the results into a list
        listx = []
        listx1 = []
        x = intital_state
        print(x)
        print('it Alice turn')
        listvalue, liststate = self.simulation(x)[0], self.simulation(x)[1]
        for i in listvalue:
            listx.append(i[0])
        maxindex = [i for i, j in enumerate(listx) if j == max(listx)]
        next_state = copy.deepcopy(liststate[0][random.choice(maxindex)])
        print(next_state)
        print('its Bob turn')
        next_state1 = self.get_action(next_state, -1)
        print(next_state1)
        print('its Alice turn')
        listvalue, liststate = self.simulation(next_state1)[0], self.simulation(next_state1)[1]
        for i in listvalue:
            listx1.append(i[0])
        maxindex = [i for i , j in enumerate(listx1) if j == max(listx1)]
        next_state2 = copy.deepcopy(liststate[0][maxindex[0]])
        print(next_state2)
        print('its Bob turn')
        print(self.simulation(next_state2)[1])
        result = self.check_winner(next_state2)

        return result




def main():
    g = Game()
    initial_state = g.intial_state()
    print(g.play(initial_state))

if __name__ == '__main__':
    main()
