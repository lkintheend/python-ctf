def myXOR(x, y):
    return ((x | y) &
            (~x | ~y))


print myXOR(98, 79)

for i in range(65, 91) + range(97, 123):
    for j in range(65, 91) + range(97, 123):
        if i * 2 + myXOR(j, 79) ** 4 == 7890683:
            print chr(i) + ': ' + chr(j)


# flag{123~2~3~4~5~6~7~ez}