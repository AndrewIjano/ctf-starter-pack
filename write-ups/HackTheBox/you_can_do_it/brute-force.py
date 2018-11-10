text = input()
A = ord('A')
for i in range(25):
    print('shift', i,': ', end = '')
    for c in text:
        print(chr((ord(c) + i - A)%26 + A), end='')
    print()
