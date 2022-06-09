import numpy as np
import random
from time import sleep
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

    def simulation(self, current_state): # Simulates the entire game from the given node and returns the number of wins on each side and the child nodes (5 moves deep)
        listm, listn, listt, listh, listp = [], [], [], [], []
        state = []
        count_step = current_state.count(0)
        if count_step == 6:
            x = self.child_nodes(current_state, 1)
            for i in x:
                h = self.child_nodes(i, -1)
                hovalue, hxvalue = 0, 0
                for j in h:
                    m = self.child_nodes(j, 1)
                    movalue, mxvalue = 0, 0
                    for k in m:
                        n = self.child_nodes(k, -1)
                        novalue, nxvalue = 0, 0
                        for l in n:
                            p = self.child_nodes(l, 1)
                            povalue, pxvalue = 0, 0
                            for l in p:
                                l = [-1 if i == 0 else i for i in l]
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
            x = self.child_nodes(current_state, -1)
            for i in x:
                h = self.child_nodes(i, 1)
                hovalue, hxvalue = 0, 0
                for j in h:
                    m = self.child_nodes(j, -1)
                    movalue, mxvalue = 0, 0
                    for k in m:
                        n = self.child_nodes(k, 1)
                        novalue, nxvalue = 0, 0
                        for l in n:
                            l = [-1 if i == 0 else i for i in l]
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
                listh.append([movalue, mxvalue])
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
                listh.append([movalue, mxvalue])
            state.append(x)
        if count_step == 2:
            x = self.child_nodes(current_state, 1)
            for k in x:
                k = [-1 if i == 0 else i for i in k]
                tovalue = self.value(k)[0]
                txvalue = self.value(k)[1]
                listh.append([tovalue, txvalue])
            state.append(x)
        if count_step == 1:
            current_state = [-1 if i == 0 else i for i in current_state]
            tovalue = self.value(current_state)[0]
            txvalue = self.value(current_state)[1]
            listh.append([tovalue, txvalue])
            state.append(current_state)
        return listh, state

    def check_winner(self, n): #Bob is -1 and Alice is 1
        check_list = []
        for i in range(len(n)):
            if i != 0 and i != 7:
                if n[i - 1] + n[i] + n[i + 1] == -3:
                    check_list.append(-1)
                if n[i - 1] + n[i] + n[i + 1] == 3:
                    check_list.append(1)
        if sum(check_list) < 0:
            return 'the winner is Bob'
        if sum(check_list) > 0:
            return 'the winner is Alice'
        else:
            return 'it is a tie'

    def play(self, intital_state): #for now: starts the game with printing the intitial state, then appends the results into a list


        return




def main():
    g = Game()
    

if __name__ == '__main__':
    main()
