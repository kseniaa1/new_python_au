#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import multiprocessing
import random
import math
#считаем интергар от 0 до 10 e^x dx с дроблением на n точек

n = 10000
def random_in_interval(i):
    return (math.exp(1)**random.uniform(i, i+10/n))*10/n


def test_all(pool):
    l = pool.map(random_in_interval,  [i/n*10 for i in range(n)])
    return l


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    s =0
    for i in test_all(pool):
        s +=i
    print("Интеграл экспоненты от 0 до 10: ", s)
    print("Time spent:", time.time() - t0)
else:
    print("__name__:", __name__)
