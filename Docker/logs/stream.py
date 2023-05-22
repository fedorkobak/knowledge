import random
from sys import stderr
from time import sleep


while True:
    sleep(1)
    if random.random() > 0.5:
        print("Just message")
    else:
        # в поток предназначенный для ошибок
        # выводим импровизированное сообщение об ошибке
        print("Some error", file=stderr)