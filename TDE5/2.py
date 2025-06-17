b = True
while b:
    Num = [0, 0]
    while Num[1] <= 10:
        while Num[0]<=10:
            P = Num[0]*Num[1]
            print(P)
            Num[0]= Num[0]+1
            if Num[0] > 10:
                Num[1] = Num[1]+1
                Num[0] = 0
            if Num[1] > 10:
                break
    x = input('continuar? digite 0')
    if x != 0:
        b = False