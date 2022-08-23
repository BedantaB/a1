class Stack:


    def __init__(self):
        self.mlist = []


    def isEmpty(self):
        if len(self.mlist) > 0:
            return False
        else:
            return True


    def push(self,x):
        self.mlist.append(x)


    def top(self):
        if not self.isEmpty():
            return self.mlist[-1]

    
    def pop(self):
        if not self.isEmpty():
            return self.mlist.pop()




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
    ls_brack = Stack()
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
                if(not ls_brack.isEmpty()):
                    ls_brack.push(ls_brack.top())

                    X += (ls_brack.top())*x
                    Y += (ls_brack.top())*y
                    Z += (ls_brack.top())*z
                    D += (ls_brack.top())*d

                    x = 0
                    y = 0
                    z = 0
                    d = 0

                else:

                    ls_brack.push(1)

            else:
                a = 0


        elif P[i] == ')':

            X += (ls_brack.top())*x
            Y += (ls_brack.top())*y
            Z += (ls_brack.top())*z
            D += (ls_brack.top())*d

            x = 0
            y = 0
            z = 0
            d = 0

            ls_brack.pop()


        elif is_number(P[i]):
            a = 1

            X += (ls_brack.top())*x
            Y += (ls_brack.top())*y
            Z += (ls_brack.top())*z
            D += (ls_brack.top())*d

            ls_brack.push(int(P[i])*ls_brack.top())

            x = 0
            y = 0
            z = 0
            d = 0


        i+=1

    return[X, Y, Z, D]


print(findPositionandDistance("((+X2(+Y-X-Z)8(+Y)9(-Z-Z)))"))
