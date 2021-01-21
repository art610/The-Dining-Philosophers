"""
Solution to the "dining philosophers" problem.
"""

import sys
import threading
import time

OUTPUT = []


class DiningPhilosophers(threading.Thread):

    free_forks = [0, 1, 2, 3, 4]

    def __init__(self, philosopher):
        threading.Thread.__init__(self)
        self.philosopher = philosopher  # philosopher id
        self.hold_forks = 0

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: "Callable[[], None]",
        pickRightFork: "Callable[[], None]",
        eat: "Callable[[], None]",
        putLeftFork: "Callable[[], None]",
        putRightFork: "Callable[[], None]",
    ) -> None:

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()

    # всегда первой берем левую вилку
    # взять левую вилку
    def pickLeftFork(self):
        left_fork_number = self.philosopher
        DiningPhilosophers.free_forks.remove(left_fork_number)
        print("Free_forks:", DiningPhilosophers.free_forks)
        self.hold_forks = 1
        print("Pick fork with number:", left_fork_number)

        OUTPUT.append([self.philosopher, 1, 1])

    # если мы пытаемся взять правую вилку, то левую мы уже держим
    # взять правую вилку
    def pickRightFork(self):
        right_fork_number = (self.philosopher + 1) % 5
        DiningPhilosophers.free_forks.remove(right_fork_number)
        print("Free_forks:", DiningPhilosophers.free_forks)
        self.hold_forks = 2
        print("Pick fork with number:", right_fork_number)

        OUTPUT.append([self.philosopher, 2, 1])

    # если едим, то держим обе вилки
    # есть
    def eat(self):
        if self.hold_forks == 2:
            print("OK! I'm eating!")
            OUTPUT.append([self.philosopher, 0, 3])
        else:
            print("I can't! Give me forks!")

    # всегда опускаем первой левую вилку
    # положить левую вилку
    def putLeftFork(self):
        left_fork_number = self.philosopher
        DiningPhilosophers.free_forks.append(left_fork_number)
        print("Free_forks:", DiningPhilosophers.free_forks)
        self.hold_forks = 1
        print("Put fork with number:", left_fork_number)

        OUTPUT.append([self.philosopher, 1, 2])

    # второй опускаем правую вилку
    # положить правую вилку
    def putRightFork(self):
        right_fork_number = (self.philosopher + 1) % 5
        DiningPhilosophers.free_forks.append(right_fork_number)
        print("Free_forks:", DiningPhilosophers.free_forks)
        self.hold_forks = 0
        print("Put fork with number:", right_fork_number)

        OUTPUT.append([self.philosopher, 2, 2])

    def run(self):
        self.wantsToEat(
            self.philosopher,
            self.pickLeftFork,
            self.pickRightFork,
            self.eat,
            self.putLeftFork,
            self.putRightFork,
        )


def main(function_calls):

    k = 5
    philosophers = [DiningPhilosophers(i) for i in range(k)]

    for j in range(k):
        philosophers[j].start()
        # philosophers[j].wantsToEat(
        #     philosophers[j].philosopher,
        #     philosophers[j].pickLeftFork,
        #     philosophers[j].pickRightFork,
        #     philosophers[j].eat,
        #     philosophers[j].putLeftFork,
        #     philosophers[j].putRightFork,
        # )

    print(OUTPUT)


if __name__ == "__main__":
    n = int(input("Please, input n: "))
    main(n)
