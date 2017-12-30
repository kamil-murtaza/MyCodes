turn=1
def printArray(block):
    if turn==1: print "Player 1 Turn : "
    elif turn==2: print "Player 2 Turn"
    for i in range(len(block)):
        for j in range(len(block[i])):
            print block[i][j],
        print
    return;

def takeInput(block):
    global turn
    ans1 = input("Enter row (1-3) : ")
    ans2 = input("Enter colomn (1-3) : ")
    if ans1>=1 and ans1<=3 and ans2>=1 and ans2<=3:
        if block[ans1-1][ans2-1]!='F':
            print "Already Selected, INput again :"
            takeInput(block)
        else:
            if turn==1:
                block[ans1-1][ans2-1]='T'
                turn=2
            else:
                block[ans1-1][ans2-1] = 'C'
                turn=1
    else:
        print "Invalid input,input again :"
        takeInput(block)
    return;

def checkWinner(block):
    status="false"
    if block[0][0]=='T' and block[0][1]=='T' and block[0][2]=='T': status="p1"
    elif block[1][0] == 'T' and block[1][1] == 'T' and block[1][2] == 'T': status="p1"
    elif block[2][0] == 'T' and block[2][1] == 'T' and block[2][2] == 'T': status="p1"
    elif block[0][0] == 'T' and block[1][0] == 'T' and block[2][0] == 'T': status="p1"
    elif block[0][1] == 'T' and block[1][1] == 'T' and block[2][1] == 'T': status="p1"
    elif block[0][2] == 'T' and block[1][2] == 'T' and block[2][2] == 'T': status="p1"
    elif block[0][0] == 'T' and block[1][1] == 'T' and block[2][2] == 'T': status="p1"
    elif block[0][2] == 'T' and block[1][1] == 'T' and block[2][0] == 'T': status="p1"
    elif block[0][0]=='C' and block[0][1]=='C' and block[0][2]=='C': status="p2"
    elif block[1][0] == 'C' and block[1][1] == 'C' and block[1][2] == 'C': status="p2"
    elif block[2][0] == 'C' and block[2][1] == 'C' and block[2][2] == 'C': status="p2"
    elif block[0][0] == 'C' and block[1][0] == 'C' and block[2][0] == 'C': status="p2"
    elif block[0][1] == 'C' and block[1][1] == 'C' and block[2][1] == 'C': status="p2"
    elif block[0][2] == 'C' and block[1][2] == 'C' and block[2][2] == 'C': status="p2"
    elif block[0][0] == 'C' and block[1][1] == 'C' and block[2][2] == 'C': status="p2"
    elif block[0][2] == 'C' and block[1][1] == 'C' and block[2][0] == 'C': status="p2"
    draw=0
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j]=='F':
                draw=draw+1
    if draw==0: return "Draw";
    if status=="p1": return 1;
    elif status=="p2": return 2;
    return "Continue";

# main function starts here
print "Welcome to TIC TAC TOE GAME"
print "T is for TIck Player 1"
print "C is for Cross Player 2"
block=[['F','F','F'],['F','F','F'],['F','F','F']]
while(1):
    printArray(block)
    takeInput(block)
    if checkWinner(block)==1:
        print ("PLAYER 1 WON")
        turn=0
        printArray(block)
        break
    elif checkWinner(block)==2:
        print ("PLAYER 2 WON")
        turn=0
        printArray(block)
        break
        print ("DRAW GAME")
        turn=0
        printArray(block)
        break