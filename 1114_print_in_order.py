# using semaphore so that second print only executes after the first print sends finish signal
# similar thing applies to the third print
# from threading import Semaphore
class Foo:
    def __init__(self):
        from threading import Semaphore
        self.gates = [Semaphore(0), Semaphore(0)]


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.gates[0].release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.gates[0]:
            printSecond()
            self.gates[1].release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.gates[1]:
            printThird()


# the following solution makes it easy to understand
# however, running time is much slower
# because cpu wastes some cycles for condition checking
# while semaphore has a better signaling mechanism and implementation
class Foo:
    def __init__(self):
        self.f = False
        self.s = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        while not self.f:
            pass
        printSecond()
        self.s = True


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        while not self.s:
            pass
        printThird()
        self.f = False
        self.s = False