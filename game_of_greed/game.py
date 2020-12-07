from game_of_greed.game_logic import GameLogic , Banker

class Game:
    def quitting(score):
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
            while dice_to_keep !='q':
                print(f'Starting round {round}')
                print(f'Rolling {remaining_dice} dice...')
                roll = self.roller(remaining_dice)
                # Game.print_roll(roll)
                print(','.join([str(i) for i in roll]))
                dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')

                if dice_to_keep == 'q':
                    Game.quitting(score) 
                elif int(dice_to_keep) in roll:
                    remaining_dice -=1
                    curr = int(dice_to_keep)
                    player1.shelf(GameLogic.calculate_score((curr,)))

                    print(f'You have {player1.shelved} unbanked points and {remaining_dice} dice remaining')
                    player1.bank()

                    countinue = input(f'(r)oll again, (b)ank your points or (q)uit ')
                    if countinue == 'q':
                        dice_to_keep = 'q'
                        score += player1.balance
                        Game.quitting(score)
                        player1.balance =0

                    if countinue == 'b':
                        score += player1.balance
                        print(f'You banked {player1.balance} points in round {round}')
                        round +=1
                        print(f'Total score is {score} points')
                        remaining_dice = 6
                        player1.balance =0



if __name__ == '__main__':
    game = Game()
    game.play()