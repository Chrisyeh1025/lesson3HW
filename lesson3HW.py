import random
ans = random.randint(1,20)
guess = int(input('猜一個數字'))
guess = int(guess)
i=1
while i < 6:
    if guess == ans:
        print('你答對了,你玩了',i,'次')
        i = 6
    if guess > ans:
        print('你猜得太大')
        guess = int(input('再猜一遍'))
        i = i + 1
    if guess < ans:
        print('你猜得太小')
        guess = int(input('再猜一遍'))
        i = i + 1
if i == 6:
    print('遊戲結束')
 
 
        
   
        
   

    
