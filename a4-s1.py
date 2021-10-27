import random
import time
start = 0
end = 0
game = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]         
        ] 
def printgame():
      for i in range(3):
            for j in range(3):
                print (game[i][j] , end=" ")   
            print()            
def print_natije(player):
       print(player ,"board...")
       end = time.time()
       zaman = end - start
       print ("time spent in the game : " , time , "second")
def check_game(player):
    c = 0
    for i in range(3):
        for j in range(3):
         if   game[i][j] != "-" :
            c = c + 1;     
    if    (game[0][0] == "pink" and game[0][1] == "pink" and game[0][2] == "pink" ) :
       print_natije("player1")
       return False   
    elif  (game[0][0] == "green" and game[0][1] == "green" and game[0][2] == "green" ) :  
       print_natije(player)
       return False   
    elif  (game[1][0] == "pink" and game[1][1] == "pink" and game[1][2] == "pink" ) :
       print_natije("player1")
       return False   
    elif  (game[1][0] == "green" and game[1][1] == "green" and game[1][2] == "green" ) :  
       print_natije(player)
       return False   
    elif  (game[2][0] == "pink" and game[2][1] == "pink" and game[2][2] == "pink" ) :
       print_natije("player1")
       return False      
    elif  (game[2][0] == "green" and game[2][1] == "green" and game[2][2] == "green" ) :  
       print_natije(player)
       return False    
    elif  (game[0][0] == "pink" and game[1][0] == "pink" and game[2][0] == "pink" ) :
            print_natije("player1")
            return False    
    elif  (game[0][0] == "green" and game[1][0] == "green" and game[2][0] == "green" ) :  
       print_natije(player)
       return False   
    elif  (game[0][1] == "pink" and game[1][1] == "pink" and game[2][1] == "pink" ) :
       print_natije("player1")
       return False   
    elif  (game[0][1] == "green" and game[1][1] == "green" and game[2][1] == "green" ) :  
       print_natije(player)
       return False   
    elif  (game[0][2] == "pink" and game[1][2] == "pink" and game[2][2] == "pink" ) :
           print_natije("player1")           
           return False      
    elif  (game[0][2] == "green" and game[1][2] == "green" and game[2][2] == "green" ) :  
       print_natije(player)
       return False   
    elif  (game[0][2] == "pink" and game[1][1] == "pink" and game[2][0] == "pink" ) :
            print_natije("player1") 
            return False     
    elif  (game[0][2] == "green" and game[1][1] == "green" and game[2][0] == "green" ) :  
       print_natije(player)
       return False    
    elif  (game[0][0] == "pink" and game[1][1] == "pink" and game[2][2] == "pink" ) :
            print_natije("player1")           
            return False     
    elif  (game[0][0] == "green" and game[1][1] == "green" and game[2][2] == "green" ) :  
       print_natije(player)
       return False    
    elif c == 9 :
        return False   
    else :
        return True                                    
def init_pc_choose():
    while check_game("pc") :
     random_pc_row = random.randint(0,2)
     random_pc_col = random.randint(0,2)

     if game[random_pc_row][random_pc_col] == "-":
         game[random_pc_row][random_pc_col] = "green"
         break    
def playwithpc():
    while check_game("pc"):
        while True :
            print("pink selection. ")
            player_row = int(input ("enter the desired row :"))
            player_col = int(input ("enter the desired column :"))
            if game[player_row-1][player_col-1] == "-":
                game[player_row-1][player_col-1] = "pink"
                init_pc_choose()
                printgame()
                break
            else :
                print("choose another house !")
                printgame()
def twoplayers():   
    while True:
        finish = 0