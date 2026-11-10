from game_logic import adjust_grid


def test_block_stays_unchanged():
    block = {
        (1, 1), (1, 2),
        (2, 1), (2, 2)
    }

    result = adjust_grid(block, 5, 5)

    assert result == block


def test_blinker():
    blinker = {
        (2, 1),
        (2, 2),
        (2, 3)
    }

    expected = {
        (1, 2),
        (2, 2),
        (3, 2)
    }

    result = adjust_grid(blinker, 5, 5)

    assert result == expected
    assert blinker == adjust_grid(result,5 ,5 )
