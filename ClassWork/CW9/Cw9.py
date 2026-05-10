def fun(n):
    for i in range(1,n+1):
        print(i)

def fun2(n):
    if n >= 1:
        fun2(n-1)
        print(n)

def fun3(n):
    if n == 1:
        return n
    else:
        return n * fun3(n-1)

def CW1(n,b):
    if b == 0:
        return 1
    else:
        return b * CW1(n, b-1)

# print(CW1(10,2))


def CW2(a, b):
    if a == b:
        return a
    else:
        return a + CW2(a + 1, b)

# print(CW2(1, 7))

def CW3(n):
    if n == 0:
        return ""
    else:
        return "*" + CW3(n-1)

# print(CW3(10))

def CW4():
    lst = [0,1,2,3,4,5,6,7,8]
    def pole(viv):
        for i in range(3):
            for j in range(3):
                print(viv[(i+j)+i*2], end="|")
            print()
            print("---------")

    def win(viv):
        if viv[0] == viv[1] == viv[2]:
            print(f"you win {viv[0]}")
            return True
        elif viv[3] == viv[4] == viv[5]:
            print(f"you win {viv[3]}")
            return True
        elif viv[6] == viv[5] == viv[8]:
            print(f"you win {viv[6]}")
            return True
        elif viv[0] == viv[3] == viv[6]:
            print(f"you win {viv[0]}")
            return True
        elif viv[1] == viv[4] == viv[7]:
            print(f"you win {viv[1]}")
            return True
        elif viv[2] == viv[5] == viv[8]:
            print(f"you win {viv[2]}")
            return True
        elif viv[0] == viv[4] == viv[8]:
            print(f"you win {viv[0]}")
            return True
        elif viv[2] == viv[4] == viv[6]:
            print(f"you win {viv[2]}")
            return True

    x = "X"
    o = "O"
    count = 0

    def xod(a, viv1):
        pole(viv1)
        b = int(input(f"{a} Ходят "))
        if viv1[b] == "O" or viv1[b] == "X":
            print("Балбес поле занято ")
            xod(a,viv1)
        else:
            viv1[b] = a
            return viv1

    while win(lst) != True:
        if count % 2 != 0:
            lst = xod(x, lst)
            win(lst)
            count += 1
        else:
            lst = xod(o, lst)
            win(lst)
            count += 1
        if count == 9:
            print("Ничья")
            break

from random import *
lst = [randint(0,100) for i in range(100)]
a=sum(lst[i] for i in range(10))

c=0
b=sum(lst[c+i] for i in range(10))
def CW5(a1,b1,c1):

    if c == 90:
        return c
    else:
        return
    return()



CW5()