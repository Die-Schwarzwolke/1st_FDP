from dice_game import roll_dice

def test_roll_range():
    for _ in range(200):
        x = roll_dice()
        assert 1 <= x <= 6