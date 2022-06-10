import random
import time

class Rock_Paper_Scissors :
    
    def __init__(self, l = ["R", "P", "S"]) -> None :
        
        self.l = l
    
    def real_name(self, choice) -> str :
        
        if choice == 'R':
            return 'Rock'
        elif choice == 'P':
            return 'Paper'
        else:
            return 'Scissors'
        
    def check_move(self, user_choice, cpu_choice, player_name) -> str :
        
        names = ['CPU',player_name]
        
        if self.user_choice == self.cpu_choice :
            return 'The game is Tie'
        
        else : 
            
            if self.user_choice == 'R' :
                
                if self.cpu_choice == 'P':
                    return names[0]+' win the game'
                else:
                    return names[1]+' win the game'
                
            elif self.user_choice == 'P' :
                
                if self.cpu_choice == 'C' :
                    return names[0]+' win the game'
                else:
                    return names[1]+' win the game'
                
            else:
                if self.cpu_choice == 'R':
                    return names[0]+' win the game'
                else:
                    return names[1]+' win the game'
   
    def play_game(self)-> None :
        
        game_move=1
        count_game=1

        print('\n ############# welcome to the Rock_Paper_Scissors Game \n')
        player_name=str(input('You will play again the computer so Please, enter your name             '))

        while game_move==1:
            self.user_choice = str(input('\nEnter your choice between "R", "P" or "S"               '))

            while (self.user_choice not in self.l):
                self.user_choice = str(input('\nInput is invalid;  enter your choice between "R", "P" or "S"               '))

            print('\nWait for 2 second, the CPU is making it choice\n')
            time.sleep(2)

            self.cpu_choice = random.choice(self.l)

            print(f'{player_name} ({self.real_name(self.user_choice)}) : CPU ({self.real_name(self.cpu_choice)})\n')

            print(f'{self.check_move(self.user_choice,self.cpu_choice,player_name)} after {count_game} part(s)\n')

            if self.user_choice==self.cpu_choice:
                input("Press Enter to continue...\n")
                count_game+=1
            else:
                game_move=0
                print(f'Thanks {player_name} for trying this game. hope you enjoyed it\n')
    
    