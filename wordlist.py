from random import randint
from random import choice

i = 700
while i > 0:
    i -= 1
    xg = ["gmu", "mason", "cyse"]
    nums = ["20", "21", "22", "23", "24"]

    word1 = ''.join(choice((str.upper, str.lower))(c) for c in xg[0])
    word2 = ''.join(choice((str.upper, str.lower))(c) for c in xg[1])
    word3 = ''.join(choice((str.upper, str.lower))(c) for c in xg[2])

    num1 = nums[randint(0,4)]
    num2 = nums[randint(0,4)]
    num3 = nums[randint(0, 4)]

    while num1 == num2 or num2 == num3 or num1 == num3:
        num1 = nums[randint(0, 4)]
        num2 = nums[randint(0, 4)]
        num3 = nums[randint(0, 4)]

    x = randint(0, 3)
    y = randint(0, 3)
    z = randint(0, 3)

    while x == y or y == z or z == x:
        x = randint(0, 3)
        z = randint(0, 3)

    L = []
    LN = []
    LN2 = []
    LN3 = []
    LN4 = []
    LN5 = []
    LN6 = []
    L3 = []

    if x > y > z and x > z:
        num1 += word1
        num2 += word2
        num3 += word3
        LN = ['{}'.format(num1), '{}'.format(num2)]
        LN2 = ['{}'.format(num1), '{}'.format(num3)]
        LN3 = ['{}'.format(num2), '{}'.format(num3)]
        LN4 = ['{}'.format(num2), '{}'.format(num1)]
        LN5 = ['{}'.format(num3), '{}'.format(num2)]
        LN6 = ['{}'.format(num3), '{}'.format(num1)]
        L = ['{}'.format(word1), '{}'.format(word2)]
        L3 = ['{}'.format(word1), '{}'.format(word2), '{}'.format(word3)]
    elif x > z > y and x > y:
        num1 += word1
        num2 += word2
        num3 += word3
        LN = ['{}'.format(num1), '{}'.format(num2)]
        LN2 = ['{}'.format(num1), '{}'.format(num3)]
        LN3 = ['{}'.format(num2), '{}'.format(num3)]
        LN4 = ['{}'.format(num2), '{}'.format(num1)]
        LN5 = ['{}'.format(num3), '{}'.format(num2)]
        LN6 = ['{}'.format(num3), '{}'.format(num1)]
        L = ['{}'.format(word1), '{}'.format(word3)]
        L3 = ['{}'.format(word1), '{}'.format(word2), '{}'.format(word3)]
    elif y > x > z and y > z:
        num1 += word1
        num2 += word2
        num3 += word3
        LN = ['{}'.format(num1), '{}'.format(num2)]
        LN2 = ['{}'.format(num1), '{}'.format(num3)]
        LN3 = ['{}'.format(num2), '{}'.format(num3)]
        LN4 = ['{}'.format(num2), '{}'.format(num1)]
        LN5 = ['{}'.format(num3), '{}'.format(num2)]
        LN6 = ['{}'.format(num3), '{}'.format(num1)]

        L = ['{}'.format(word2), '{}'.format(word1)]
        L3 = ['{}'.format(word1), '{}'.format(word2), '{}'.format(word3)]
    elif y > z > x and y > x:
        num1 += word1
        num2 += word2
        num3 += word3
        LN = ['{}'.format(num1), '{}'.format(num2)]
        LN2 = ['{}'.format(num1), '{}'.format(num3)]
        LN3 = ['{}'.format(num2), '{}'.format(num3)]
        LN4 = ['{}'.format(num2), '{}'.format(num1)]
        LN5 = ['{}'.format(num3), '{}'.format(num2)]
        LN6 = ['{}'.format(num3), '{}'.format(num1)]

        L = ['{}'.format(word2), '{}'.format(word3)]
        L3 = ['{}'.format(word1), '{}'.format(word2), '{}'.format(word3)]
    elif z > x > y and z > y:
        num1 += word1
        num2 += word2
        num3 += word3
        LN = ['{}'.format(num1), '{}'.format(num2)]
        LN2 = ['{}'.format(num1), '{}'.format(num3)]
        LN3 = ['{}'.format(num2), '{}'.format(num3)]
        LN4 = ['{}'.format(num2), '{}'.format(num1)]
        LN5 = ['{}'.format(num3), '{}'.format(num2)]
        LN6 = ['{}'.format(num3), '{}'.format(num1)]

        L = ['{}'.format(word3), '{}'.format(word1)]
        L3 = ['{}'.format(word1), '{}'.format(word2), '{}'.format(word3)]
    else:
        num1 += word1
        num2 += word2
        num3 += word3
        LN = ['{}'.format(num1), '{}'.format(num2)]
        LN2 = ['{}'.format(num1), '{}'.format(num3)]
        LN3 = ['{}'.format(num2), '{}'.format(num3)]
        LN4 = ['{}'.format(num2), '{}'.format(num1)]
        LN5 = ['{}'.format(num3), '{}'.format(num2)]
        LN6 = ['{}'.format(num3), '{}'.format(num1)]

        L = ['{}'.format(word3), '{}'.format(word2)]
        L3 = ['{}'.format(word1), '{}'.format(word2), '{}'.format(word3)]


    print("{}{}2022".format(L[0], L[1]))
    print("{}20{}22".format(L[0], L[1]))
    print("{}22{}20".format(L[0], L[1]))
    print("22{}20{}".format(L[0], L[1]))
    print("2220{}{}".format(L[0], L[1]))
    print("2022{}{}".format(L[0], L[1]))
    print("{}{}2220".format(L[0], L[1]))

    print("{}{}2023".format(L[0], L[1]))
    print("{}20{}23".format(L[0], L[1]))
    print("{}23{}20".format(L[0], L[1]))
    print("23{}20{}".format(L[0], L[1]))
    print("2320{}{}".format(L[0], L[1]))
    print("2023{}{}".format(L[0], L[1]))
    print("{}{}2320".format(L[0], L[1]))

    print("{}{}2024".format(L[0], L[1]))
    print("{}20{}24".format(L[0], L[1]))
    print("{}24{}20".format(L[0], L[1]))
    print("24{}20{}".format(L[0], L[1]))
    print("2420{}{}".format(L[0], L[1]))
    print("2024{}{}".format(L[0], L[1]))
    print("{}{}2420".format(L[0], L[1]))

    print("{}{}2122".format(L[0], L[1]))
    print("{}21{}22".format(L[0], L[1]))
    print("{}22{}21".format(L[0], L[1]))
    print("22{}21{}".format(L[0], L[1]))
    print("2221{}{}".format(L[0], L[1]))
    print("2122{}{}".format(L[0], L[1]))
    print("{}{}2221".format(L[0], L[1]))

    print("{}{}".format(LN[0],LN[1]))
    print("{}{}".format(LN2[0],LN2[1]))
    print("{}{}".format(LN3[0],LN3[1]))
    print("{}{}".format(LN4[0],LN4[1]))
    print("{}{}".format(LN5[0],LN5[1]))
    print("{}{}".format(LN6[0],LN6[1]))

    print("{}{}{}".format(L3[0], L3[1], L3[2]))



