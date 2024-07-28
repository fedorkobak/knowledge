from time import sleep

f = open("check_file", "r")

with open('check_file', 'r') as f:
    check_numer = int(f.read())

if check_numer < 5:
    print("Слишком мало ты пытался меня запустить! ХА")
else:
    check_numer = 0
    while(True):
        sleep(10)
with open('check_file', 'w') as f:
    f.write(str(check_numer + 1))

f.close()