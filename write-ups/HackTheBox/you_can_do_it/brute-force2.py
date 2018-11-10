text = input()
A = ord('A')
for i in range(126):
    print('shift', i,': ', end = '')
    for c in text:
        print(chr((ord(c) + i)%126), end='')
    print()
