from collections import Counter
import random

class GameLogic:

    @staticmethod
    def calculate_score(tup):
        result = []
        score = 0
        true1 = True
        true2 = True
        true3 = True
        true4 = True

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


