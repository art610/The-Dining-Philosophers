import threading
import time


class DiningPhilosophers(threading.Thread):

    # идентификаторы философов идут от нуля (при первой инициализации получаем 0)
    philosopher = -1
    # количество свободных вилок
    free_forks = [0, 1, 2, 3, 4]
    # в выходные данные записываем соответствующие действия каждого философаmiin
    output = []

    def __init__(self):
        threading.Thread.__init__(self)
        DiningPhilosophers.philosopher += 1
        self.philosopher = DiningPhilosophers.philosopher
        self.left_fork = self.philosopher
        self.right_fork = (self.philosopher + 1) % 5

    def run(self):
        self.wantsToEat(
            self.philosopher,
            self.pickLeftFork,
            self.pickRightFork,
            self.eat,
            self.putLeftFork,
            self.putRightFork,
        )

    # метод скопирован с leetcode.com
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

    def pickLeftFork(self):
        with self.lock:
            while self.left_fork not in DiningPhilosophers.free_forks:
                self.lock.wait(0.2)
        # если вилка освободилась, то берем её
        DiningPhilosophers.free_forks.remove(self.left_fork)
        # в выходные данные добавляем данное действие
        DiningPhilosophers.output.append([self.philosopher, 1, 1])

    def pickRightFork(self):
        with self.lock:
            while self.right_fork not in DiningPhilosophers.free_forks:
                self.lock.wait(0.2)
        # если вилка освободилась, то берем её
        DiningPhilosophers.free_forks.remove(self.right_fork)
        # в выходные данные добавляем данное действие
        DiningPhilosophers.output.append([self.philosopher, 2, 1])

    def eat(self):
        # едим некоторое время
        time.sleep(1)
        # в выходные данные добавляем данное действие
        DiningPhilosophers.output.append([self.philosopher, 0, 3])

    def putLeftFork(self):
        # возвращаем левую вилку на место
        DiningPhilosophers.free_forks.append(self.left_fork)
        # в выходные данные добавляем данное действие
        DiningPhilosophers.output.append([self.philosopher, 1, 2])

    def putRightFork(self):
        # возвращаем правую вилку на место
        DiningPhilosophers.free_forks.append(self.right_fork)
        # в выходные данные добавляем данное действие
        DiningPhilosophers.output.append([self.philosopher, 2, 2])


def main():
    # input n = 1
    # создаем пять философов
    philosophers_numb = 5
    philosophers = [DiningPhilosophers() for i in range(philosophers_numb)]

    # запускаем
    for i in range(philosophers_numb):
        philosophers[i].start()

    # дожидаемся окончания работы всех потоков
    for i in range(philosophers_numb):
        philosophers[i].join()

    # выводим выходные данные (список совершенных каждым философом действий)
    print(DiningPhilosophers.output)


if __name__ == "__main__":
    main()
