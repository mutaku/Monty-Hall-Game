#!/usr/bin/env python
# Run game show simulations with sequential door picks to test monte hall paradox
#
#  #######    #######    #######
#  #     #    #     #    #     #
#  #  1  #    #  2  #    #  3  #
#  #     #    #     #    #     #
#  #######    #######    #######
#

from random import sample
import string
import timeit

class DoorManage():
    "Door management utilities"
    
    def __init__(self):
        # set up variables - set door related to 0 so outside of operable range
        self.doors = [1,2,3]
        self.result = -1
        self.open = 0
        self.behind = 0
        self.picked = 0
    
    def check(f):
        # check for outcome condition
        def action(self):
            f(self)
            if self.picked == self.behind:
                self.result = 1
        return action
    
    def establish(self):
        # random selection of a door from remaining doors pool
        return sample(self.doors,1)[0]
    
    def pick(self):
        # initial user pick - random of 3
        self.picked = self.establish()
    
    @check
    def reveal(self):
        # open a door that it's not behind
        self.doors.remove(self.picked)
        if self.picked != self.behind:        
                self.open = self.doors.remove(self.behind)

    def run(self):
        # hide behind door - random of 3
        self.behind = self.establish()
        self.pick()
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
        i = 0
        while i < self.iter:
            this = DoorManage()
            this.run()
            if this.result == 1:
                self.score['wins'] += 1
            else:
                self.score['losses'] += 1
            i += 1
        return self.score
    
