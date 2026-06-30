# let's dive deeper 

# stone paper sccissor game 

# stone = 1     s
# paper = 0         p
# sccissor = -1         sc


# try this way next time , means segregate almost all parts and use them wisely wherever needed 
# main()
#  |
#  |-- get_player_choice()
#  |
#  |-- generate_computer_choice()
#  |
#  |-- check_winner()
#  |
#  |-- update_score()
#  |
#  |-- display_result()


import random 

def game():
    com = random.choice([0,1,-1])

    n = input("Enter your choice s/sc/p= ")
    
  

    sps = {"s":1 , "p" : 0 , "sc" : -1}


    reversesps = {1 : "s" , 0 : "p" , -1 : "sc" }
    you = sps[n]

    print(f"your choice = {reversesps[you]} \n computer's choice = {reversesps[com]} \n")

    if (com==you):
        return 9    #Match draw

    else:
        if ((you - com)==2 or (you-com)==-1):
            return 2     #You won
        else:
             return 4      #you lost 
        # did this just to ease ou things
      

i = 1
c =0
y=0
d=0
u = int(input("Enter the number of times you want to play the game "))
for i in range (1,u+1):

    result = game()                  #ye result = game() issiliye kiye hai , kyuki agar game() krte toh if me jaake check krta phir elif me jaake dobaara check karega phir run karega 
    if (result== 2):                 #aise ye variable se variable compare karega
        y=y+1
    
    elif (result== 4):
        c=c+1
    
    else:
        d=d+1
        

print (f"your score = {y}")
print (f"computer score  = {c}")
print (f"Match drawn = {d}")
    
if (y>c):
    print(f"You won  by  {y} ")

elif(c>y):
    print(f"you lost to computer by  {c} ")

else:
    print("Match draw")

