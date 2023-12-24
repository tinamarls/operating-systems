import random
import os
import time

operators = ['+', '-', '*' , '/']
N = random.randint(120, 180)


for i in range(N):
        X = random.randint(1, 9)
        O = operators[random.randint(0, 3)]
        Y = random.randint(1, 9)
        print(str(X) + ' ' + O + ' ' + str(Y), flush=True)
        time.sleep(1)