from threading import Thread


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(f'Child {i}')


print("Main Thread")
t1 = PrintThread()
t1.start()
for i in range(1, 11):
    print(f'Main {i}')
