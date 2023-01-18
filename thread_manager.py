import threading


def heavy(n, i, thead):
    for x in range(1, n):
        for y in range(1, n):
            print()
    print(f"Цикл № {i}. Поток {thead}")


def sequential(calc, thead):
    print(f"Запускаем поток № {thead}")
    for i in range(calc):
        heavy(1, i, thead)
    print(f"{calc} циклов вычислений закончены. Поток № {thead}")


def threaded(theads, calc):
    threads = []

    for thead in range(theads):
        t = threading.Thread(target=sequential, args=(calc, thead))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
