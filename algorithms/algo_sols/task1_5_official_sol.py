maxrandval = 1000000

def getentranceandfloor(flatno, flatsonfloor, floors):
    floorsbefore = (flatno - 1)//flatsonfloor
    entrance = floorsbefore//floors + 1
    floor = floorsbefore % floors + 1
    return entrance, floor

def check(k1, m, k2, p2, n2, flatsonfloor):
    entrance2, floor2 = getentranceandfloor(k2, flatsonfloor, m)
    if entrance2 == p2 and floor2 == n2:
        return getentranceandfloor(k1, flatsonfloor, m)
    return -1, -1


def slow(k1, m, k2, p2, n2):
    ent = -1
    floor = -1
    goodflag = False
    
    for flatsonfloor in range(1, maxrandval + 1):
        nent, nfloor = check(k1, m, k2, p2, n2, flatsonfloor)
        if nent != -1:
            goodflag = True
            if ent == -1:
                ent, floor = nent, nfloor
            if ent != nent and ent != 0:
                ent = 0
            if floor != nfloor and floor != 0:
                floor = 0
    
    if goodflag:
       return (ent, floor)
    else:
        return (-1, -1)
    
if __name__ == "__main__":
    print(" ".join(map(str,
        slow(*map(int, input().split(" ")))
    )))