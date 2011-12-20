#!/usr/bin/env python
# Run game show simulations with sequential door picks to test monte hall paradox

from random import sample
import string
import timeit

class DoorManage():
    "Door management utilities"
    
    def __init__(self):
        # set up variables - set door related to 0 so outside of operable range
        self.doors = [1,2,3]
        self.result = 0
        self.open = 0
        self.behind = 0
        self.picked = 0
    
    def check(f):
        # check for outcome condition
        def action(self):
            f(self)
            if self.picked == self.behind:
                self.result = 1
            elif self.open == self.behind:
                self.result = -1
        return action
    
    def establish(self):
        # random selection of a door from remaining doors pool
        return sample(self.doors,1)[0]
    
    @check
    def pick(self):
        # initial user pick - random of 3
        self.picked = self.establish()
    
    @check
    def reveal(self):
        # open a door that it's not behind
        self.doors.remove(self.picked)
        self.open = self.establish()
        self.doors.remove(self.open)
        if self.result == 0:
            self.result = -1

    def run(self):
        # hide behind door - random of 3
        self.behind = self.establish()
        self.pick()
        if self.result == 0:
            self.reveal()

class play():
    # Play the game
    
    def __init__(self,iter=10):
        # setup to play
        self.score = {'wins':0,'losses':0}
        self.time = 0
        self.iter = iter
        t = timeit.Timer(self.go)
        print 'Ran %d iterations in %fs' %(self.iter,t.timeit(1)),self.score
    
    def go(self):
        # iterate through games
        for i in xrange(0,self.iter):
            this = DoorManage()
            this.run()
            if this.result == 1:
                self.score['wins'] += 1
            else:
                self.score['losses'] += 1
        return self.score
    