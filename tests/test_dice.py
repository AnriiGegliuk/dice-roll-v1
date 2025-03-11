from src.dice_roll_v1.dice import Dice

class TestDice():
    def test_one_roll(self):
        dice = Dice()
        roll = dice.roll()
        assert isinstance(roll, int)
        assert roll > 0
        assert roll < 10
