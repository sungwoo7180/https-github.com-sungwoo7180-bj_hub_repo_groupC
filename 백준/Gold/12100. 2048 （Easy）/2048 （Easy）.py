from itertools import product

n = int(input())
lst = []
for i in range(n):

    lst.append(list(map(int, input().split())))

def rotate_90():
    global lst
    lst = list(map(list, zip(*lst[::-1])))

def rotate_reverse():
    global lst
    lst = list(map(list, zip(*lst)))[::-1]


def left():
    global lst
    for i in range(n):
        if 0 in lst[i]:
            cnt = 0
            while 0 in lst[i]:
                lst[i].remove(0)
                cnt += 1
            for u in range(cnt):
                lst[i].append(0)
        chk = [False for _ in range(n)]
        for j in range(0,n-1):
            k = j + 1
            if lst[i][j] == lst[i][k] and chk[j] is False and chk[k] is False:
                lst[i][j] += lst[i][k]
                lst[i][k] = 0
                chk[j] = True
                chk[k] = True
        if 0 in lst[i]:
            cnt = 0
            while 0 in lst[i]:
                lst[i].remove(0)
                cnt += 1
            for u in range(cnt):
                lst[i].append(0)
    return

def right():
    rotate_90()
    rotate_90()
    left()
    rotate_reverse()
    rotate_reverse()
    return

def up():
    rotate_90()
    rotate_90()
    rotate_90()
    left()
    rotate_reverse()
    rotate_reverse()
    rotate_reverse()
    return

def down():
    rotate_90()
    left()
    rotate_reverse()
    return



result = []
cmd = [0,1,2,3]
cmds = list(product(cmd,repeat=5))

copys = [item[:] for item in lst]
for cmd in cmds:
    lst = [item[:] for item in copys]
    for a in cmd:
        if a == 0:
            left()
        elif a == 1:
            up()
        elif a == 2:
            down()
        elif a == 3:
            right()
    result.append(max(map(max,lst)))

print(max(result))