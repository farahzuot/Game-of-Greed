from collections import Counter
import random

class GameLogic:
    @staticmethod
    def roll_dice(number_of_dice):
        result = []
        for die in range(number_of_dice):
            result.append(random.randint(1,6))
        return tuple(result)


    @staticmethod
    def calculate_score(tup):
        result = []
        score = 0
        true1 = True
        true2 = True
        true3 = True

        for i in tup:
            result.append(i)
            a = Counter(result)       

        for j in result:   
            if len(a) == 3 and a.most_common()[2][1] == 2:   
                score = 1500
                break

            if a.most_common(1)[0][1] == 1 and len(result) == 6:
                score+=1500
                break
              
            if j == 1 and a[1] >= 3:
                if true1:
                    score+=((a[1]-3)*1000)+1000
                    true1 = False

            if j == 1 and a[1] < 3:
                score+=100

            if j == 5 and a[5] >= 3:
                if true3:
                    score+=((a[5]-3)*500)+500
                    true3 = False

            if j == 5 and a[5] < 3:
                score+=50               
                   
            if a[j] >= 3 and j != 1 and j != 5:
                if true2:  
                    score+=((a[j]-3)*(j*100))+(j*100)
                    true2 = False
        
        return score
    
    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)
        if all_dice_score == 0:
            return tuple()
        scorers = []
        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return tuple(scorers)



class Banker:
    def __init__(self):
        self.shelved=0
        self.balance=0
    def shelf(self,value):
        self.shelved = value
    def bank(self):
        self.balance += self.shelved
        self.shelved =0
    def clear_shelf(self):
        self.shelved =0