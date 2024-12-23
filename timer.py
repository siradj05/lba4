from time import time
import changer1, schedule_lib, re_shedule


def timer(func, n):
    """За сколько времени функция func выполнится n раз"""
    st = time()
    for _ in range(n):
        func()
    return time() - st


if __name__ == '__main__':
    for name, pars in [('changer1', changer1), ('schedule_lib', schedule_lib),('re_shedule', re_shedule)]:
        print(f'{name}: {timer(pars.main, 100)} s')