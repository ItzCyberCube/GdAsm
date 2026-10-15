import math
reader=0
def codefunc(n, a, b, c,r,fl):
    a=math.floor(a)
    n=math.floor(n)
    if n == 1 and fl:
        values[a] = float(input())
    elif n == 2 and fl:
        print(values[a])
    elif n == 3 and fl:
        print(b)
    elif n == 4 and fl:
        return True
    elif n == 5 and fl:
        values[a] = b
    elif n == 6 and fl:
        values[a] = values[b] + c
    elif n == 7 and fl:
        values[a] = values[b] + values[c]
    elif n == 8 and fl:
        values[a] = values[b] - c
    elif n == 9 and fl:
        values[a] = values[b] - values[c]
    elif n == 10 and fl:
        values[a] = values[b] * c
    elif n == 11 and fl:
        values[a] = values[b] * values[c]
    elif n == 12 and fl:
        values[a] = values[b] / c
    elif n == 13 and fl:
        values[a] = values[b] / values[c]
    elif n == 14 and fl:
        values[a] = values[b] - (values[b] * (values[b] // values[c]))
    elif n == 15 and fl:
        values[a] = values[b] - (values[b] * (values[b] // c))
    elif n == 16 and fl:
        values[a] = math.floor(values[b])
    elif n == 17 and fl:
        values[a] = math.ceil(values[b])
    elif n == 18 and fl:
        values[a] = round(values[b])
    elif n == 19 and fl:
        #????
        return 0
    elif n == 20 and fl:
        values[a] = abs(values[b])
    elif n == 21 and fl:
        values[a],values[b]=values[b],values[a]
    elif n == 22 and fl:
        values[a] = max(values[b],values[c])
    elif n == 23 and fl:
        values[a] = min(values[b],values[c])
    elif n == 24 and fl:
        values[a] = values[b]/abs(values[b])
    elif n == 25 and fl:
        values[a] = math.trunc(values[b])
    elif n == 26 and fl:
        #???
        values[a] = math.trunc(values[b])
    elif n == 27 and fl:
        #???
        values[a] = math.trunc(values[b])
    elif n == 28 and fl:
        values[a] = r
    elif n == 29 and fl:
        r=a
    elif n == 30 and fl:
        r=values[a]
    elif n==31 and fl:
        if values[a]==values[b]: fl=True
        else: fl=False
    elif n==32 and fl:
        if values[a]!=values[b]: fl=True
        else: fl=False
    elif n==33 and fl:
        if values[a]>values[b]: fl=True
        else: fl=False
    elif n==34 and fl:
        if values[a]>=values[b]: fl=True
        else: fl=False
    elif n==35 and fl:
        if values[a]==b: fl=True
        else: fl=False
    elif n==36 and fl:
        if values[a]!=b: fl=True
        else: fl=False
    elif n==37 and fl:
        if values[a]>b: fl=True
        else: fl=False
    elif n==38 and fl:
        if values[a]>=b: fl=True
        else: fl=False
    elif n==39 and fl:
        if values[a]<b: fl=True
        else: fl=False
    elif n==40 and fl:
        if values[a]<=b: fl=True
        else: fl=False
    elif n==41 and fl:
        fl = not f
    elif n==42:
        fl = True



    return [r,fl]


f = open('code.txt')
code = []
for a in f:
    line = list(map(int, a.split()))
    # дозаполняю нулями функции
    while len(line) < 4:
        line.append(0)
    code.append(line)

# переменные
values = [0] * 999
reader=-1
flag=True
# компилинг
while -2<reader<1000:
    reader+=1
    line=code[reader]
    resp=codefunc(line[0], line[1], line[2], line[3],reader,flag)

    if type(resp) == bool:
        if resp:
            break

    if reader!=resp[0]:
        reader=resp[0]-2

    flag=resp[1]

