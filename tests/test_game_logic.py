from streamlit.testing.v1 import AppTest

from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_first_attempt_win_awards_90_points():
    assert update_score(current_score=0, outcome="Win", attempt_number=1) == 90


def test_new_game_resets_score():
    app = AppTest.from_file("app.py").run(timeout=15)
    app.session_state["score"] = 55

    app.button[1].click().run(timeout=15)

    assert app.session_state["score"] == 0
