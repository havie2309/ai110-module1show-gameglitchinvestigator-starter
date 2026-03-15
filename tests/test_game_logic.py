from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score


# --- check_guess tests ---

def test_check_guess_correct():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_check_guess_too_high():
    outcome, _ = check_guess(80, 50)
    assert outcome == "Too High"

def test_check_guess_too_low():
    outcome, _ = check_guess(20, 50)
    assert outcome == "Too Low"

def test_check_guess_hint_too_high_says_go_lower():
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_check_guess_hint_too_low_says_go_higher():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message


# --- parse_guess tests ---

def test_parse_guess_valid_int():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42
    assert err is None

def test_parse_guess_float_string():
    ok, value, err = parse_guess("7.9")
    assert ok == True
    assert value == 7

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("")
    assert ok == False
    assert err == "Enter a guess."

def test_parse_guess_not_a_number():
    ok, value, err = parse_guess("abc")
    assert ok == False
    assert err == "That is not a number."


# --- get_range_for_difficulty tests ---

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200


# --- update_score tests ---

def test_update_score_win():
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_update_score_too_high_decreases():
    new_score = update_score(50, "Too High", 1)
    assert new_score < 50

def test_update_score_too_low_decreases():
    new_score = update_score(50, "Too Low", 1)
    assert new_score < 50