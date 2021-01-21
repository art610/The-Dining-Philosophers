"""
Module Docstring
"""

import sys
import threading
import time


class DiningPhilosopher(threading.Thread):

    def __init__(self, philosopher):
        threading.Thread.__init__(self)
        self.philosopher = philosopher      # philosopher id
        self.left_fork = philosopher
        self.right_fork = (philosopher+1) % 5

    # взять левую вилку
    def pickLeftFork(self):
        # TODO: implement
        pass

    # взять правую вилку
    def pickRightFork(self):
        pass

    # есть
    def eat(self):
        pass

    # положить левую вилку
    def putLeftFork(self):
        pass

    # положить правую вилку
    def putRightFork(self):
        pass


philosopher_1 = DiningPhilosopher(0)
philosopher_2 = DiningPhilosopher(1)

print(philosopher_1.philosopher, philosopher_2.left_fork, philosopher_2.right_fork)
