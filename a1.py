
def is_number(s):
    try:
        i = int(s + "")
        return True
    except:
        return False




def findPositionandDistance(S):

    P = '(' + S + ')'

    X = 0
    Y = 0
    Z = 0
    D = 0
    ls_brack = []
    a = 0
    f = 0

    x = 0
    y = 0
    z = 0
    d = 0
    
    i = 0
    while i < len(P):
        
        if P[i] == '+':
            i += 1
            f = 1
        elif P[i] == '-':
            i += 1
            f = 0

        if P[i] == 'X':

            if f == 1:

                x += 1
                d += 1

            else:

                x -= 1
                d += 1


        elif P[i] == 'Y':

            if f == 1:

                y += 1
                d += 1

            else:

                y -= 1
                d += 1
        
        elif P[i] == 'Z':

            if f == 1:

                z += 1
                d += 1

            else:

                z -= 1
                d += 1

        
        elif P[i] == '(':

            if a == 0:
                if(len(ls_brack) > 0):
                    ls_brack.append(ls_brack[len(ls_brack) - 1])

                    X += ls_brack[len(ls_brack) - 1]*x
                    Y += ls_brack[len(ls_brack) - 1]*y
                    Z += ls_brack[len(ls_brack) - 1]*z
                    D += ls_brack[len(ls_brack) - 1]*d

                    x = 0
                    y = 0
                    z = 0
                    d = 0

                else:

                    ls_brack.append(1)

            else:
                a = 0


        elif P[i] == ')':

            X += ls_brack[len(ls_brack) - 1]*x
            Y += ls_brack[len(ls_brack) - 1]*y
            Z += ls_brack[len(ls_brack) - 1]*z
            D += ls_brack[len(ls_brack) - 1]*d

            x = 0
            y = 0
            z = 0
            d = 0

            ls_brack.pop()
            
            


        elif is_number(P[i]):
            a = 1

            X += ls_brack[len(ls_brack) - 1]*x
            Y += ls_brack[len(ls_brack) - 1]*y
            Z += ls_brack[len(ls_brack) - 1]*z
            D += ls_brack[len(ls_brack) - 1]*d

            ls_brack.append(int(P[i])*ls_brack[len(ls_brack) - 1])

            x = 0
            y = 0
            z = 0
            d = 0
        


        i+=1

    return[X, Y, Z, D]


print(findPositionandDistance("((+X2(+Y-X-Z)8(+Y)9(-Z-Z)))"))
