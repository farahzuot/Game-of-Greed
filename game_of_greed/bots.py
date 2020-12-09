from game_of_greed.game import Game
from game_of_greed.game_logic import GameLogic
import builtins
from abc import abstractmethod
import re

class Bot:
    def __init__(self):
        self.old_print= print
        self.old_input= input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        builtins.print = self.old_print
        builtins.input = self.old_input


    @abstractmethod
    def _mock_print(self, *args):
        self.old_print(*args)


    @abstractmethod
    def _mock_input(self, *args):
        return self.old_input(*args)


    @classmethod
    def play(cls , gamesNum=1):

        tot =0
        for i in range(gamesNum):
            bot = cls()
            game = Game()
            game.play()
            tot+= bot.total_score
            bot.reset()

        print(
            f"{gamesNum} rounds may have average_score : {tot // gamesNum}"
        )

class Basic_bot(Bot):

    def _mock_input(self, *args):
        self.old_print(*args)
        return "n"
    def _mock_print(self, *args):
        self.old_print(*args)


class Nervous_Nellie(Bot):

    def __init__(self):
        super().__init__()
        self.roll = None

    def _mock_print(self, args):
        
        first_char = args[0]
        if first_char.isdigit():
            self.roll = tuple(int(char) for char in args.split(","))
        elif args.startswith("Thanks for playing."):
            self.total_score = int(re.findall(r"\d+", args)[0])
        self.old_print(args)

    def _mock_input(self, args):
        if args.startswith("Wanna play?"):
            return "y"
        elif args.startswith("Enter dice to keep (no spaces), or (q)uit:"):
            scorers = GameLogic.get_scorers(self.roll)
            keepers = "".join([str(ch) for ch in scorers])
            return keepers
        elif args.startswith("(r)oll again, (b)ank your points or (q)uit "):
            return 'b'
        else:
            raise ValueError(f"Unrecognized args {args}")

if __name__ == "__main__":
    # Basic_bot.play(1)
    Nervous_Nellie.play(1)