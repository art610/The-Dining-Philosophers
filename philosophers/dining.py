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
        self.hold_forks = 0


    # всегда первой берем левую вилку
    # взять левую вилку
    def pickLeftFork(self):
        left_fork_number = self.philosopher
        self.hold_forks = 1
        print(left_fork_number)

    # если мы пытаемся взять правую вилку, то левую мы уже держим
    # взять правую вилку
    def pickRightFork(self):
        right_fork_number = (self.philosopher + 1) % 5
        self.hold_forks = 2
        print(right_fork_number)

    # если едим, то держим обе вилки
    # есть
    def eat(self):
        if self.hold_forks == 2:
            print("OK")
        else:
            print("I can't! Give me forks!")


    # всегда опускаем первой левую вилку
    # положить левую вилку
    def putLeftFork(self):
        self.hold_forks = 1

    # второй опускаем правую вилку
    # положить правую вилку
    def putRightFork(self):
        self.hold_forks = 0


philosopher_1 = DiningPhilosopher(0)
philosopher_2 = DiningPhilosopher(1)

print(philosopher_1.philosopher)
philosopher_1.pickLeftFork()
print(philosopher_1.hold_forks)
