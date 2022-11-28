






import sys, time

print('Ninety-Nine Bottles of Beer')
print()
print('(Press Ctrl-C to quit.)')

time.sleep(2)

bottles = 99 
PAUSE = 2 

try:
    while bottles > 1:
        print(bottles, 'bottles of beer on the wall,')
        time.sleep(PAUSE) 
        print(bottles, 'bottles of beer,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        bottles = bottles - 1
        print(bottles, 'bottles of beer on the wall!')
        time.sleep(PAUSE)
        print()


    print('1 bottle of beer on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of beer,')
    time.sleep(PAUSE)
    print('Take it down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of beer on the wall!')
except KeyboardInterrupt:
    sys.exit()