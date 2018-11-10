text = input()
A = ord('a')
for i in range(25):
    print('shift', i,': ', end = '')
    for c in text:
        if ord('a') <= ord(c) and ord(c) <= ord('z'):
            print(chr((ord(c) + i - A)%26 + A), end='')
        else:
            print(c,end='')
    print()
