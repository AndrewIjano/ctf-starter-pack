import sys

for line in sys.stdin:
    print line

count = { chr(ord('a') + i) : 0 for i in range(26)}

total = 0
for c in text:
    if c in count:
        count[c] += 1
        total += 1

# counts
for i in range(26):
    char = chr(ord('a') + i)
    print(char, count[char], round(count[char]/total*100, 3))

print('\n SORTED:')
for key, value in sorted(count.items(), key=lambda item: (item[1], item[0])):
    print ("%s: %s" % (key, value))

replace = { 'u' : 'z',
            'k' : 'j',
            'm' : 'q',
            'q' : 'x',
            'e' : 'o',
            'l' : 'a',
            'p' : 't',
            's' : 'e'
            }
for c in text:
    if c in replace:
        print(replace[c], end='')
    else:
        print(c,end='')
