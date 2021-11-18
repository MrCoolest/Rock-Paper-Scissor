# In this we will play rock paper sessior with Bot
import random

class Play_Game:
     def __init__(self, name):
          self.name = name
          self.game_instruments = ['Rock','Paper','Scissor']
          self.game_winning_logic = {self.game_instruments[0] : {self.game_instruments[0]: None, self.game_instruments[1] : False, self.game_instruments[2] : True},self.game_instruments[1] : {self.game_instruments[0]: True, self.game_instruments[1] : None, self.game_instruments[2] : False}, self.game_instruments[2] : {self.game_instruments[0]: False, self.game_instruments[1] : True, self.game_instruments[2] : None}}
          print(f'Welcome {self.name} to our game!!')

 
     def winner(self,player,bot):
          win = self.game_winning_logic.get(player)
          win = win[bot]
          print(f'You choose {player}\nBot choose {bot}')
          print("You're the Winner") if win == True else print("Draw") if win == None else print("Sorry you loss")
          return win


     def play(self, times):
          try:
               player_win = 0
               bot_win = 0
               times+=1
               for time in range(1,times):
                    print('\n')
                    player = int(input('Choice (Rock : 1, Paper : 2, Scissor : 3) :- '))
                    if player in range(1,4):
                         player_choice = self.game_instruments[player-1]
                         bot_choice =  random.choice(self.game_instruments)
                         ans = self.winner(player_choice,bot_choice)
                         if ans == False:
                              bot_win+=1
                         elif ans == True:     
                              player_win+=1
                         else:   
                              pass
                    else:
                         print('Sorry given input not match')
                         retry = input('Want to try again? press "Y": ')
                         if retry == 'Y' or retry == 'y':
                              self.play((times-1)-time)
                         
               print(bot_win, player_win)          
          except Exception as e:
               print(f"Something went wrong {e}")       
          finally:
               print(f"\nFinall decission:- {self.name} is winner") if player_win > bot_win else print('\nFinall decission:- The match is Draw') if player_win == bot_win else print('\nFinall decission:- Bot is winner')      




if __name__ == "__main__":
     p = Play_Game('Ankit')
     p.play(3)

