import sys

input_str = "-1 4 15"
# input_str = ""
#
# for line in sys.stdin:
#     input_str += line

listStr = input_str.split(" ")

a = int(listStr[0])
b = int(listStr[1])
c = int(listStr[2])
count = 0

if a > b:
    tmp = a
    a = b
    b = tmp

if b >= c:
    count = 0
elif b <= 0:
    count = -1
else:
    if a < 0:
        a = a * -1
        tronLen = round(a / b + .5)
        count += tronLen
        a = (b * tronLen) - a
    while a < c and b < c:
        if a < b:
            a += b
            count += 1
        else:
            b += a
            count += 1

print(count)
# div = (c/(a+b).to_f).ceil
# tong = (a+b)*div + (b * ( div -1 ))
# if tong >= c
#     count += div
# else

# end
