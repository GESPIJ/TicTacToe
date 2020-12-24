import math
X='X'
O='O'
EMPTY='Empty'
matriz = [[X,O,X],[X,O,EMPTY],[O,EMPTY,EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #for (x,row) in enumerate(board):
        #for (y,value) in enumerate(row):
            #if (==)
    x = sum([row.count(X) for row in board])
    o=  sum([row.count(O) for row in board])

    return X if (x==o) else O

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    new = []
    for row in board:
        new+=row
    if (new[0]==new[1]==new[2]==(X) or new[3]==new[4]==new[5]==(X) or new[6]==new[7]==new[8]==(X) or
        new[0]==new[3]==new[6]==(X) or new[1]==new[4]==new[7]==(X) or new[2]==new[5]==new[8]==(X) or
        new[0]==new[4]==new[8]==(X) or new[2]==new[4]==new[6]==(X)):
        return X
        
    elif (new[0]==new[1]==new[2]==(O) or new[3]==new[4]==new[5]==(O) or new[6]==new[7]==new[8]==(O) or
        new[0]==new[3]==new[6]==(O) or new[1]==new[4]==new[7]==(O) or new[2]==new[5]==new[8]==(O)  or
        new[0]==new[4]==new[8]==(O) or new[2]==new[4]==new[6]==(O)):
            return O
    else:
            return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board)):
        return True
    tableroLleno =  sum([row.count(EMPTY) for row in board])
    return tableroLleno == 0 
    #raise NotImplementedError
    
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerResult = winner(board)
    if (winnerResult==X):
        return 1
    elif (winnerResult==O):
        return -1
    else:
        return 0
    #raise NotImplementedError

#def recursion(board,player1,max):
    # constanteMin=100
    # constanteMax=-100
    # constante=0
    # coordenadas=(0,0)
    # res={'res':-100 if max else 100, 'coordenadas':coordenadas}
    # listaCombinaciones=[]
    # ficha = 'X' if player1 else 'O'
    
    # if (terminal(board)):
    #     print(utility(board))
    #     res['res']=utility(board)
    #     print("UNA LLAMADA")
    #     return res
    # else:
    #     for i,x in enumerate(board):
    #         for j,y in enumerate(x):
    #             if(board[i][j]==EMPTY):
    #             #tablero=board.copy()
    #                 board[i][j]=ficha
    #                 res= recursion(board,not(player1),True)
    #             if (res['res']>constanteMax and max):
    #                 constanteMax=res['res']
    #                 coordenadas=(i,j)
    #                 nuevo= {}
    #                 listaCombinaciones.append([res,coordenadas])
    #                 print(constanteMax)
    #                 print(coordenadas)
    #             elif(res['res']<constanteMin and not(max)):
    #                 constanteMin=res['res']
    #                 coordenadas=(i,j)
    #                 print(constanteMin)
    #                 print(coordenadas)

    # #print("Hola")
    # #objeto = {'coordenadas':coordenadas, 'res':constanteMax if max else constanteMin}
    # return objeto
# constante=-100
# coordenadas=(0,0)
# for i,x in enumerate(matriz):
#     for j,y in enumerate(x):
#         if (matriz[i][j]==EMPTY):
#             tablero=list(map(list, matriz))
#             tablero[i][j]='X'
#             resultado=recursion(tablero,False)
#             if (resultado>constante):
#                 constante=resultado
#                 coordenadas=(i,j)
#                 print(resultado)
#                 print(f'{i},{j}')
#                 print(coordenadas)
#listando=recursion(matriz,True,True)
#print(listando)
#print("Hola")

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    tab = list(map(list, board))
    ficha=player(board)
    def minimizando(board,dep=0):
        ficha=player(board)
        constanteMax=-100
        constanteMin=100
        constante=0
        MAX = ficha==X
        tab = list(map(list, board))
        if (terminal(board)):
            #print(utility(board))
            res=utility(board)
            #print("UNA LLAMADA")
            return res
        else:
            for i,x in enumerate(tab):
                for j,y in enumerate(x):
                    if(tab[i][j]==EMPTY):
                    #tablero=board.copy()
                        tab[i][j]=ficha
                        #res= minim(board)
                        res=minimizando(tab,dep+1)
                        tab[i][j]=EMPTY

                        if (MAX):
                            constanteMax=max(constanteMax,res)
                        else:
                            constanteMin = min(constanteMin,res)
            return constanteMax if MAX else constanteMin
                        
    MAX = ficha==X
    constanteMax=-100
    constanteMin=100
    coordendas = (-1,-1)
    #constanteMax=-100
    #constante=0
    for i,x in enumerate(tab):
        for j,y in enumerate(x):
            if(tab[i][j]==EMPTY):
                    #tablero=board.copy()
                tab[i][j]=ficha
                #res= minim(board)
                res=minimizando(tab)
                tab[i][j]=EMPTY
                if (res>constanteMax and MAX):
                    constanteMax=res
                    coordenadas=(i,j)
                elif (res<constanteMin and not(MAX)):
                    constanteMin=res
                    coordenadas=(i,j)
    print("Final ejecucion de la funcion")
    return coordenadas
    #coordenadas=(0,0)
    #res={'res':-100 if max else 100, 'coordenadas':coordenadas}
    #listaCombinaciones=[]
   # player
    #ficha = player(board)
    #Max= player(board)==X

minimax(matriz)

