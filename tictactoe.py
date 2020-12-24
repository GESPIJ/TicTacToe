"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    listaCombinaciones = []
    for (x,row) in enumerate(board):
        for (y,val) in enumerate(row):
            if (val == EMPTY):
                listaCombinaciones.append((x,y))
    return listaCombinaciones
        #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    ficha = player(board)
    #print(f'Board Type {type(board)}')
    #print(f'{type(action[0])}')
    board[action[0]][action[1]] = ficha
    return board
    #raise NotImplementedError


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
      
    ##raise NotImplementedError


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    tab = list(map(list, board))
    ficha=player(board)
    def minimizando(board):
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
                        res=minimizando(tab)
                        tab[i][j]=EMPTY

                        if (MAX):
                            constanteMax=max(constanteMax,res)
                        else:
                            constanteMin = min(constanteMin,res)
            return constanteMax if MAX else constanteMin
                        
    MAX = ficha==X
    constanteMax=-100
    constanteMin=100
    coordenadas = (-1,-1)
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
    #print("Final ejecucion de la funcion")
    return coordenadas
            


         
    #raise NotImplementedError