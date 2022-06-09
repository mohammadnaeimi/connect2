import numpy as np
import random
from time import sleep
import copy

class Game():
    def __init__(self):
        self.gamestate = [0, 0, 0, 0, 0, 0, 0, 0] # the state where the games starts, evolves as the game continues
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

    def child_nodes(self, state, m): # returns a list of all possible actions (m = 1 for (Computer) and m = -1 for (User))
        listl = []
        x = copy.deepcopy(state)
        for i in range(len(state)):
            if state[i] == 0:
                x[i] = m
                listl.append(x)
                x = copy.deepcopy(state)
        return listl

    def value(self, n): # returns the value of the terminal nodes as a tuple
        O, X = 0, 0
        for i in range(len(n)):
            if i != 0 and i != 7:
                if n[i - 1] == n[i] == n[i + 1] == -1:
                    X = X + 1
                if n[i - 1] == n[i] == n[i + 1] == 1:
                    O = O + 1
        if O == X:
            O = 1
            X = 1
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

    def simulation(self, current_state, m): # Simulates the entire game from the given node and returns the value of the terminal state on each side and the parent of the terminal
        listm, listn, listt, listh, listp = [], [], [], [], []
        state = []
        count_step = current_state.count(0)
        if count_step == 6:
            x = self.child_nodes(current_state, m)
            for i in x:
                h = self.child_nodes(i, -1 * m)
                hovalue, hxvalue = 0, 0
                for j in h:
                    m = self.child_nodes(j, m)
                    movalue, mxvalue = 0, 0
                    for k in m:
                        n = self.child_nodes(k, -1 * m)
                        novalue, nxvalue = 0, 0
                        for l in n:
                            p = self.child_nodes(l, m)
                            povalue, pxvalue = 0, 0
                            for l in p:
                                l = [-1 * m if i == 0 else i for i in l]
                                tovalue = self.value(l)[0]
                                txvalue = self.value(l)[1]
                                listt.append([tovalue, txvalue])
                                povalue = povalue + tovalue
                                pxvalue = pxvalue + txvalue
                                listt.append([tovalue, txvalue])
                            novalue = novalue + povalue
                            nxvalue = nxvalue + pxvalue
                            listp.append([povalue, pxvalue])
                        movalue = movalue + novalue
                        mxvalue = mxvalue + nxvalue
                        listn.append([novalue, nxvalue])
                    hovalue = movalue + hovalue
                    hxvalue = mxvalue + hxvalue
                    listm.append([movalue, mxvalue])
                listh.append([hovalue, hxvalue])
            state.append(x)
        if count_step == 5:
            x = self.child_nodes(current_state, -1 * m)
            for i in x:
                h = self.child_nodes(i, m)
                hovalue, hxvalue = 0, 0
                for j in h:
                    m = self.child_nodes(j, -1 * m)
                    movalue, mxvalue = 0, 0
                    for k in m:
                        n = self.child_nodes(k, m)
                        novalue, nxvalue = 0, 0
                        for l in n:
                            l = [-1 * m if i == 0 else i for i in l]
                            tovalue = self.value(l)[0]
                            txvalue = self.value(l)[1]
                            listt.append([tovalue, txvalue])
                            novalue = novalue + tovalue
                            nxvalue = nxvalue + txvalue
                            listt.append([tovalue, txvalue])
                        movalue = movalue + novalue
                        mxvalue = mxvalue + nxvalue
                        listn.append([novalue, nxvalue])
                    hovalue = movalue + hovalue
                    hxvalue = mxvalue + hxvalue
                    listm.append([movalue, mxvalue])
                listh.append([hovalue, hxvalue])
                state.append(x)
        if count_step == 4:
            x = self.child_nodes(current_state, m)
            for i in x:
                m = self.child_nodes(i, -1 * m)
                movalue, mxvalue = 0, 0
                for j in m:
                    n = self.child_nodes(j, m)
                    novalue, nxvalue = 0, 0
                    for k in n:
                        k = [-1 * m if i == 0 else i for i in k]
                        tovalue = self.value(k)[0]
                        txvalue = self.value(k)[1]
                        listt.append([tovalue, txvalue])
                        novalue = novalue + tovalue
                        nxvalue = nxvalue + txvalue
                        listt.append([tovalue, txvalue])
                    movalue = movalue + novalue
                    mxvalue = mxvalue + nxvalue
                    listn.append([novalue, nxvalue])
                listh.append([movalue, mxvalue])
            state.append(x)
        if count_step == 3:
            x = self.child_nodes(current_state, -1 * m)
            for i in x:
                movalue, mxvalue = 0, 0
                n = self.child_nodes(i, m)
                for k in n:
                    k = [-1 * m if i ==0 else i for i in k]
                    tovalue = self.value(k)[0]
                    txvalue = self.value(k)[1]
                    movalue = tovalue + movalue
                    mxvalue = txvalue + mxvalue
                    listt.append([tovalue, txvalue])
                listh.append([movalue, mxvalue])
            state.append(x)
        if count_step == 2:
            x = self.child_nodes(current_state, m)
            for k in x:
                k = [-1 * m if i == 0 else i for i in k]
                tovalue = self.value(k)[0]
                txvalue = self.value(k)[1]
                listh.append([tovalue, txvalue])
            state.append(x)
        if count_step == 1:
            current_state = [-1 * m if i == 0 else i for i in current_state]
            tovalue = self.value(current_state)[0]
            txvalue = self.value(current_state)[1]
            listh.append([tovalue, txvalue])
            state.append(current_state)
        return listh, state

    def check_winner(self, finalstate): #Bob is -1 and Alice is 1
        check_list = []
        for i in range(len(finalstate)):
            if i != 0 and i != 7:
                if finalstate[i - 1] + finalstate[i] + finalstate[i + 1] == -3:
                    check_list.append(-1)
                if finalstate[i - 1] + finalstate[i] + finalstate[i + 1] == 3:
                    check_list.append(1)
        if sum(check_list) < 0:
            return 'the winner is Bob'
        if sum(check_list) > 0:
            return 'the winner is Alice'
        else:
            return 'it is a tie'

    def selection(self, state, m): #selects the best node from a given state => strategy: prevents the user from winning
        list_value = []
        value = self.simulation(state, m)[0]
        state = self.simulation(state, m)[1]
        for i in value:
            list_value.append(i[0])
        return state[0][list_value.index(max(list_value))]

    def play(self): #selects the best first action, gets the user turn and continues the game till the end, you can never win this game
        self.gamestate[random.randint(1, 5)] = 1
        s1 = self.gamestate
        print(s1)
        self.gamestate = self.get_action(s1, -1)
        s2 = self.gamestate
        print(s2)
        s3 = self.selection(s2, 1)
        print(s3)
        self.gamestate = self.get_action(s3, -1)
        s4 = self.gamestate
        print(s4)
        s5 = self.selection(s4, 1)
        print(s5)
        self.gamestate = self.get_action(s5, -1)
        s6 = self.gamestate
        s7 = self.selection(s6, 1)
        print(s7)
        self.gamestate = self.get_action(s7, -1)
        return self.check_winner(self.gamestate)




def main():
    g = Game()
    print(g.play())

if __name__ == '__main__':
    main()
