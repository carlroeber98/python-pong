import random
spielfeld = [[' ' for i in range(120)] for j in range(20)]

ball = [10,119]
schlaeger = [[8, 0], [9, 0], [10, 0], [11, 0], [12, 0]]

spielfeld[ball[0]][ball[1]] = 'o'

def schlaeger(b):
    global spielfeld
    global schlaeger
    for i in range(0, 5):
        spielfeld[schlaeger[i][b]][schlaeger[i][0]] = '|'
        b += 1

def printSpielfeld():
    global spielfeld
    ausgabe = " "
    schlaeger(5)
    for i in range (0,len(spielfeld)):
        for j in range (0,len(spielfeld[0])):
            ausgabe = ausgabe + str(spielfeld[i][j])
        ausgabe = ausgabe+"\n"
    print(ausgabe)

def löscheSpielfeld():
    global spielfeld
    spielfeld = [[' ' for i in range(120)] for j in range(20)]
    
def bewegeBall():
    global spielfeld
    global ball
    x = 2
    y = 1
    schritte1 = 0
    schritte2 = 0
    while True:
        löscheSpielfeld()
        ball[0] = ball[0] + schritte1       
        ball[1] = ball[1] + schritte2       
        spielfeld[ball[0]][ball[1]] = 'o'
        schlaeger(8)
        printSpielfeld()
        
printSpielfeld()

