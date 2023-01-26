import turtle
import random
import math
import numpy as np
import time

window = turtle.Screen()
t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
# t.shape('turtle')
t.color('black')
P = []
#P = [(200, 600), (1000, 200), (1750, 800), (100, 50), (1750, 50), (900, 850), (1000, 1000), (500, 500), (700, 100), (650, 1200), (900, 100), (1800, 250), (700, 500), (900, 1800), (100, 200), (300, 400), (400, 300), (100, 1000), (200, 1700), (1000, 100)]
t.up()
t.goto(-450, 100)
t.write(
    "Zaznacz kliknięciem myszki na planszy miejsca do odwiedzenia. \n Naciśnij spację, aby rozpocząć rozwiązywanie TSP.\n Kliknij 'V', by podglądać pośrednie trasy. \n Kliknij 'C', by usunąć przecięcia. \n Kliknij 'F', by zobaczyć tylko pierwszą trasę.",
    font=("Courier New", 20, "italic"))
optM = []


def timeStamp(checkpoint):
    global start_time
    t.pu()
    t.goto(0, 30)
    t.pendown()
    t.write("Zakończono po:" + str(checkpoint - start_time), font=("Courier New", 30, "bold"))
    t.pd()
    t.penup()
    t.goto(-450, 70)
    t.pendown()
    t.write(str(P), font=("Courier New", 10, "bold"))
    t.penup()
    t.goto(-50, 90)
    t.pendown()
    t.write(str(optM), font=("Courier New", 10, "bold"))


def space():
    global opt, optM, P, start_time, zoptM
    # print("Pocz="+str(optM))
    # if len(optM)>=1:
    #    return

    optM = [0]
    for i in range(0, len(P)):
        optM.append(i)
    optM.append(0)
    opt = dlugosc(optM)
    t.color('red')
    plot(True)
    start_time = time.time()
    bab([])
    t.color('green')
    checkpoint = time.time()
    plot(True)
    timeStamp(checkpoint)


window.onkey(space, 'space')


def click(x, y):
    global P, opt
    P.append([x, y])
    t.pu()
    t.goto(x, y)
    t.pd()
    t.circle(5)
    t.write("("+str(int(x))+"."+str(int(y))+")", font=("Courier New",10,"bold"))
    t.pu()


v = False


def vision():
    global v
    v = not v
    print('v=', v)
    plot(v)


window.onkey(vision, 'v')

c = False


def cross():
    global c
    c = not c
    print('c=', c)


window.onkey(cross, 'c')

f = False


def first():
    global f
    f = not f
    print('f', f)


window.onkey(first, 'f')


def test():
    global P
    if segment_crossing(P):
        print("Przecinają się", len(P))
    else:
        print("Nie przecinają się", len(P))


window.onkey(test, 't')


def reset():
    global P
    P = []


window.onkey(reset, 'r')


def plot(graph):
    global P, opt, optM, start_time
    t.clear()
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.write(str(opt), font=("Courier New", 30, "bold"))
    t.penup()
    if not graph:
        return
    for i in range(0, len(optM) - 1):
        t.goto(P[optM[i]][0], P[optM[i]][1])
        t.pendown()
        t.goto(P[optM[i + 1]][0], P[optM[i + 1]][1])
        t.penup()


def odleglosc(i, j):
    global P
    # print([i,j])
    return math.sqrt((P[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2)


def dlugosc(M):
    d = 0
    for i in range(0, len(M) - 1):
        d += odleglosc(M[i], M[i + 1])
    return d


def bab(M):
    global P, opt, optM, zoptM, start_time, last_time, v, c
    t.pendown()
    dif_time = round(time.time() - last_time)
    if dif_time > 10:
        t.pu()
        t.goto(-400, -400)
        t.pd()
        t.write(str(round(time.time() - last_time)), font=("Courier New", 20, "bold"))
        t.pu()
        last_time = round(time.time())
    if c:
        if way_cross(M):
            #    print(M,"Ma przecięcia")
            return
        # else:
        #    print(M,"Nie ma przecięć")
    d = dlugosc(M)
    if d >= opt:
        return
    if len(M) > len(P):
        if d < opt and d > 1000:
            opt = d
            optM = M.copy()
            t.color('red')
            plot(v)
    else:
        if f:
            choose_shortest_first(M)
        else:
            choose_every(M)
    # print(opt,optM)


def choose_every(M):
    global P
    # print(M)
    for i in range(0, len(P) + 1):
        ii = i % len(P)
        if not (ii in M) or ii == M[0] and len(M) == len(P):
            MM = M.copy()
            MM.append(ii)
            bab(MM)


def choose_shortest_first(M):
    global optM, P
    if len(M) >= len(P):
        if len(M) == len(P):
            imin = 0
            MM = M.copy()
            MM.append(0)
            print("Add", imin)
            bab(MM)
        else:
            return
    else:
        # print(M)
        U = [0]
        while len(U) < len(M):
            min = 10000000000
            imin = 1
            for i in range(1, len(P) + 1):
                ii = i % len(P)
                if not (ii in M) and len(M) - 1 != ii:
                    # print(M[len(M)-1],i)
                    d = odleglosc(M[len(M) - 1], ii)
                    if min > d:
                        min = d
                        imin = ii
            U.append(imin)
            MM = M.copy()
            MM.append(ii)
            print("Add", imin, min)
            bab(MM)


def det3(m):
    a = np.array(m)
    det = np.linalg.det(a)
    return det


def point_on_segment(m):
    matrix = [
        [m[0][0], m[1][0], 1],
        [m[1][0], m[1][1], 1],
        [m[2][0], m[2][1], 1]]
    det = det3(matrix)
    if det != 0:
        return False
    if min(m[0][0], m[1][0]) <= m[2][0] <= max(m[0][0], m[1][0]) and min(m[0][1], m[1][1]) <= m[2][1] <= max(m[0][1],
                                                                                                             m[1][1]):
        return True
    else:
        return False


def sgn(a: int):
    if a < 0:
        return -1
    elif a > 0:
        return 1
    else:
        return 0


def segment_crossing(m):
    if point_on_segment([m[0], m[1], m[2]]) or \
            point_on_segment([m[0], m[1], m[3]]) or \
            point_on_segment([m[2], m[3], m[0]]) or \
            point_on_segment([m[2], m[3], m[1]]):
        return True
    if sgn(det3([[m[0][0], m[0][1], 1], [m[1][0], m[1][1], 1], [m[2][0], m[2][1], 1]])) == sgn(
            det3([[m[0][0], m[0][1], 1], [m[1][0], m[1][1], 1], [m[3][0], m[3][1], 1]])):
        return False
    else:
        return True


def way_cross(M):
    global P
    i = len(M) - 1
    result = False
    for j in range(1, i - 2):
        if i - 1 != j % len(P) and i % len(P) != j - 1:
            cross = segment_crossing([P[M[i]], P[M[i - 1]], P[M[j]], P[M[j - 1]]])
            # if cross:
            #    print("Crossing",[P[M[i]],i,P[M[i-1]],P[M[j]],j,P[M[j-1]]])
            result = result or cross
    return result


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(int(x), int(y)))


last_time = round(time.time())

canvas = turtle.getcanvas()
canvas.bind('<Motion>', motion)
window.onclick(vision)
window.onclick(click)
window.listen()
window.mainloop()




