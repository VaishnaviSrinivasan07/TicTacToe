def display_board(board):
    
    
    for row in range(3): 
        print("\n+-----+-----+-----+")
        print("|     |     |     |")
        print("|",end="")
        for column in range(3):
            
            print(" ",board[row][column]," |",end="")
    print("\n+-----+-----+-----+")        
             

def enter_move(board):
    tag=False
    entry=int(input(("Enter your move:")))
    
    for row in range(3):
        for column in range(3):
                      
            if board[row][column]==entry:
                #print(board[row][column])
                board[row][column]="O"
                tag=True
                break
    if(tag==False):
        print("Invalid entry, Please enter again")
        enter_move(board)
    
    
def make_list_of_free_fields(board):
    free_tuple=()
    for row in range(3):        
        for column in range(3):
            if board[row][column] not in ("X","O"):
                free_tuple=free_tuple+((row,column),)
    
    #print(free_tuple)
    return free_tuple
    

def victory_for(board, sign):
 
        if (board[0][0]==board[1][1]==board[2][2]):          
            return board[0][0]
        elif(board[0][1]==board[1][1]==board[2][1]):
            return board[0][1]
        elif (board[0][0]==board[1][0]==board[2][0]):            
            return board[0][0]
        elif (board[0][0]==board[0][1]==board[0][2]):            
            return board[0][0]
        elif (board[0][2]==board[1][1]==board[2][0]):            
            return board[0][2]
        elif (board[0][2]==board[1][2]==board[2][2]):           
            return board[0][2]
        elif (board[2][0]==board[2][1]==board[2][2]):
            return board[2][0]
        elif(board[1][0]==board[1][1]==board[1][2]):
            return board[1][0]
        else:return "on"



def draw_move(board):
    draw=True
    while(draw):
        
        for i in range(10):
            value=int(randrange(10))
           
        for row in range(3):
            for column in range(3):
                                    
                if board[row][column]==value:
                    board[row][column]="X"
                    return board
                    
                else:
                    continue
from random import randrange

board=[
        [1,2,3],
        [4,5,6],
        [7,8,9]]


print("Lets start the game")
board[1][1]="X"
free_tuple=make_list_of_free_fields(board)
sign="on"
display_board(board)
while(free_tuple and sign=="on"):
         
    enter_move(board)
    display_board(board)    
    free_tuple=make_list_of_free_fields(board)
    sign=victory_for(board,sign)
    if sign=="X":
        print("Computer Won")
        break
    elif sign=="O":
        print("*****You Won*****")
        break
    board=draw_move(board)
    display_board(board)
    free_tuple=make_list_of_free_fields(board)
    sign=victory_for(board,sign)
    if sign=="X":
        print("*****Computer Won*****")
        break
    elif sign=="O":
        print("*****You Won*****")
        break

if(sign=="on"):
    print("*****It is a Tie*****")
    
            
