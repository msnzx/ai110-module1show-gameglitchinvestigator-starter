# 💭 Reflection: Game Glitch Investigator

I approached the project as a debugging exercise rather than assuming that every suspected issue was a real bug. I checked the game rules against the implementation and tests, then focused the final fixes on the behaviors that could be verified.

## 1. What was broken when you started?

The comparison tests already matched the expected outcomes, so I did not treat the high/low behavior as a confirmed bug. The reproducible issues addressed in this pass were the win-score calculation and the New Game score reset.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Win on attempt 1 | Award 90 points | Old formula awarded 80 points | Win formula added an extra attempt offset |
| Click New Game after earning points | Start a fresh game with score 0 | Previous score remained in session state | New-game handler did not reset score |
| Guess 60 when secret is 50 | Return “Too High” | `check_guess(60, 50)` returns “Too High” | Existing behavior; verified by test |
| Guess 40 when secret is 50 | Return “Too Low” | `check_guess(40, 50)` returns “Too Low” | Existing behavior; verified by test |

---

## 2. How did I use AI as a teammate?

I used Copilot as a debugging teammate and checked its suggestions against the code and tests. I accepted the suggestion to align win scoring with the attempt count passed by `app.py`. The app increments the count before calling `update_score`, so the first winning attempt is attempt 1; the old extra `+ 1` reduced its award by ten more points than the formula intended. I added a test asserting that a first-attempt win awards 90 points.

I did not apply the prompt's example suggestion to change the high/low comparison. Inspection showed `check_guess` already returns `"Too High"` for 60 versus 50 and `"Too Low"` for 40 versus 50, and the existing tests cover both results. Changing that logic would have broken working behavior. Instead, I fixed the separate New Game score reset and added a Streamlit app test to verify the score returns to zero.

---

## 3. Debugging and testing my fixes

I used focused pytest cases to verify the fixes as well as the existing `check_guess()` outcomes. The scoring test checks that a first-attempt win awards 90 points. The Streamlit `AppTest` test sets a nonzero score, clicks New Game, and confirms that the score is reset. The comparison tests continue to verify win, too-high, and too-low results.

The final test run was `python -m pytest -q`: 5 tests passed. I also started the app with Streamlit and checked its health endpoint, which returned `HTTP 200: ok`. The README's sample walkthrough follows the actual score changes for guesses 40, 70, and 50 when the secret is 50.

---

## 4. What I learned about Streamlit and state

Streamlit reruns the script every time the app updates, which means variables in normal Python memory are recreated unless they are stored in `st.session_state`. The secret number, attempts, score, status, and history therefore need to be managed as session state so a rerun does not start an unrelated game.

This debugging pass also showed that resetting a game means resetting all of its related state, not just its secret and attempt count. The score needs to reset with the rest of the game, or points from the previous game leak into the next one.

---

## 5. Looking ahead: my developer habits

One habit I want to reuse is writing a small test for the exact behavior before changing code. The score and New Game regressions gave me concrete checks, while the existing comparison tests stopped me from “fixing” behavior that was already correct. I also want to keep AI suggestions scoped to the actual bug instead of accepting a larger refactor unless it clearly improves readability and testability.

Next time, I would provide the AI with the relevant function contract and caller behavior up front, and ask it to propose a regression test alongside any fix. This project changed how I think about AI-generated code: it can help me investigate and move quickly, but it still needs verification, testing, and my judgment before I trust it.
