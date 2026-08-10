from itertools import groupby

s = input("Enter:")

for digit, group in groupby(s):
    print((len(list(group)), int(digit)), end = " ")