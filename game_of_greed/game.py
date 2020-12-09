from game_of_greed.game_logic import GameLogic , Banker
from collections import Counter

class Game:
    def quitting(self,score):
        print(f'Total score is {score} points')
        print(f'Thanks for playing. You earned {score} points')

    def __init__(self, roller=None):
        self.roller = roller or GameLogic.roll_dice

    # @staticmethod
    # def print_roll(roll):
    #     print(','.join([str(i) for i in roll]))

    def play(self):
        player1= Banker()
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':
            round = 1
            remaining_dice = 6
            score = 0
            dice_to_keep=0
            past_roll_shelf=0
            print(f'Starting round {round}')
            while dice_to_keep !='q':
                
                print(f'Rolling {remaining_dice} dice...')
                roll = self.roller(remaining_dice)
                # Game.print_roll(roll)
                ask = True
                while ask == True:
                    ask = False
                    print(','.join([str(i) for i in roll]))

                    if GameLogic.calculate_score(roll) ==0:
                        print('Zilch!!! Round over')

                        player1.shelved = 0
                        player1.bank()
                        print(f'You banked {player1.balance} points in round {round}')
                        round +=1
                        print(f'Total score is {score} points')
                        remaining_dice = 6
                        player1.balance =0
                        print(f'Starting round {round}')
                        dice_to_keep = 'Zilch'

                        break

                    dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')

                    v =[int(x) for x in dice_to_keep if x.isdigit()]

                    a = Counter(v).most_common()
                    b = Counter(roll).most_common()
                    votes=0

                    cheatting = True
                    if len(a) <= len(b):
                        for i in a:
                            for j in b:
                                if i[0] == j[0]:
                                    if i[1] <= j[1]:
                                        votes +=1

                    if len(a) == votes:
                        cheatting = False

                    if cheatting == True:
                        print('Cheater!!! Or possibly made a typo...')
                        ask = True
                    
                if dice_to_keep == 'q':
                    self.quitting(score)
                elif dice_to_keep == 'Zilch':
                    pass
                else:  
                    curr = tuple(v)
                    for i in curr:
                        remaining_dice -=1
              


                    player1.shelf(GameLogic.calculate_score(curr))

                    if past_roll_shelf != 0:
                        player1.shelved += past_roll_shelf
                        past_roll_shelf =0

                    print(f'You have {player1.shelved} unbanked points and {remaining_dice} dice remaining')
                    
                    if GameLogic.calculate_score(curr) == 1500:
                        remaining_dice = 6

                    countinue = input(f'(r)oll again, (b)ank your points or (q)uit ')
                    if countinue == 'q':
                        past_roll_shelf =0
                        dice_to_keep = 'q'
                        score += player1.balance
                        self.quitting(score)
                        player1.balance =0

                    if countinue == 'b':
                        past_roll_shelf =0
                        player1.bank()
                        score += player1.balance
                       
                        print(f'You banked {player1.balance} points in round {round}')
                        round +=1
                        print(f'Total score is {score} points')
                        if score >= 10000:
                            break
                        remaining_dice = 6
                        player1.balance =0
                        print(f'Starting round {round}')

                    if countinue == 'r':
                        past_roll_shelf+=player1.shelved


if __name__ == '__main__':
    game = Game()
    game.play()