import random


async def prompt():
    return input()


async def repl():
    print(" "*25 + " BOGA II")
    print(" "*19 + " CREATIVE COMPUTING")
    print(" "*17 + " MORRISTOWN, NEW JERSEY")
    print("")
    print("")
    print("")
    print("DO YOU WANT INSTRUCTIONS? ", end="")
    ans = await prompt()
    print("")
    print("")
    if ans[0] == 'Y':
        print("  THE BOGA IS HIDING ON A GRID (YOU SPECIFY THE LENGTH")
        print("AND WIDTH). TRY TO GUESS HIS POSITION USING THE HINTS")
        print("I GIVE YOU.  EACH GUESS IS TWO NUMBERS SEPERATED BY")
        print("A COMMA.  PLEASE KEEP IN MIND THAT THE BOGA IS ALSO")
        print("SEARCHING FOR YOU!!!!")
        print("")
        print("")
    ans = "Y"
    while ans[0] == 'Y':
        u = 0
        k = 1
        f = 0
        print("HOW BIG SHOULD THE GRID BE(20 MAXIMUM)? ", end="")
        g = await prompt()
        g = int(g)
        while g < 1 or g > 20:
            print("")
            print("HOW BIG SHOULD THE GRID BE(20 MAXIMUM)? ", end="")
            g = await prompt()
            g = int(g)
        s = g

        # PRINTS THE GRID

        print("WOULD YOU LIKE A SAMPLE GRID? ", end="")
        z = await prompt()
        if z[0] != 'N':
            print("")
            a = ""
            if g >= 10:
                for x in range(10, g+1):
                    x1 = int(x/10)
                    a = a + str(x1 + 48) + " "
                print(25*" ")
            a = ""
            for x in range(0, g+1):
                x1 = x - int(x/10)*10
                a = a + str(x1 + 48) + " "
            print(5*" ")
            a = ""
            for x in range(0, g+1):
                a = a + "* "
            for x in range(0, g+1):
                print(" " + '{:<4d}'.format(x) + a)
        print("")
        h = 1
        print("CHOOSE YOUR POSITION? ", end="")
        x1 = await prompt()
        pos = x1.split(',')
        if len(pos) == 2:
            y1 = int(pos[1])
            x1 = int(pos[0])
        else:
            x1 = int(x1)
            print("?? ", end="")
            y1 = await prompt()
            y1 = int(y1)
        while x1 > g or x1 < 0 or y1 > g or y1 < 0:
            print("")
            print("CHOOSE YOUR POSITION? ", end="")
            x1 = await prompt()
            pos = x1.split(',')
            if len(pos) == 2:
                y1 = int(pos[1])
                x1 = int(pos[0])
            else:
                x1 = int(x1)
                print("?? ", end="")
                y1 = await prompt()
                y1 = int(y1)
        print("THE BOGA PICKS HIS POSITION!")
        x2 = int(random.random() * g)
        y2 = int(random.random() * g)
        while True:
            print("GUESS # " + str(k) + " ? ", end="")
            x3 = await prompt()
            pos = x3.split(',')
            if len(pos) == 2:
                y3 = int(pos[1])
                x3 = int(pos[0])
            else:
                x3 = int(x3)
                print("?? ", end="")
                y3 = await prompt()
                y3 = int(y3)
            while x3 > g or x3 < 0 or y3 > g or y3 < 0:
                print("")
                print("GUESS # " + str(k) + " ? ", end="")
                x3 = await prompt()
                pos = x3.split(',')
                if len(pos) == 2:
                    y3 = int(pos[1])
                    x3 = int(pos[0])
                else:
                    x3 = int(x3)
                    print("?? ", end="")
                    y3 = await prompt()
                    y3 = int(y3)
            k += 1
            f += 1
            if k == 10:
                print("YOU USED UP ALL OF YOUR GUESSES.")
                break
            if abs(x3-x2) + abs(y3-y2) == 0:
                print("YOU GUESSED THE BOGA'S POSITION IN " + str(f) + " GUESS(ES)!")
                print("")
                break
            print("YOU GUESSED " + str(x3) + " , " + str(y3) + " ")
            print("")
            print("HE'S MORE TO THE ", end="")
            if x2 != x3:
                if x2 < x3:
                    print("NORTH", end="")
                else:
                    print("SOUTH", end="")
            if y2 != y3:
                if y2 < y3:
                    print("WEST")
                else:
                    print("EAST")

            #LINES 700-970 AND 1110-1150=BOGAS GUESSING FORMULA

            print("")
            if h != 0:
                x4 = int(0.5 * s)
                y4 = int(0.5 * s)
            print("THE BOGA GUESSES " + str(x4) + " , " + str(y4) + " ")
            u = u + 1
            print("")
            q = abs(y1 - y4) + abs(x1 - x4)
            if q == 0:
                print("THE BOGA GUESSED YOUR POSITION IN " + str(u) + " GUESS(ES)!")
                print("")
                break
            h = 0
            flag = False
            if y4 == y1 and x4 == x1:
                flag = True
            if not flag:
                a = 1
                if abs(y4-y1) >= 2:
                    a = 2
                if y4 < y1:
                    y4 = int(abs(y4 + a))
                    if y4 > g:
                        y4 = 0.5 * g
                else:
                    y4 = int(abs(y4 - a))
                if x4 != x1:
                    a = 1
                    if abs(x4 - x1) >= 2:
                        a = 2
                    if x4 < x1:
                        x4 = int(abs(x4 + a))
                        if x4 > g:
                            x4 = 0.5 * g
                            a = 2
                    else:
                        x4 = int(abs(x4 - a))
        print("THE BOGA WAS AT " + str(x2) + " , " + str(y2) + " ")
        print("")
        print("DO YOU WANT TO PLAY AGAIN? ", end="")
        ans = await prompt()


async def main():
    await repl()
