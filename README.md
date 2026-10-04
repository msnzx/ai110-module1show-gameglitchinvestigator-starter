# 🎮 Game Glitch Investigator

## Purpose

This project is a simple number-guessing game built with Streamlit. The player picks a difficulty level, guesses a number in a target range, and gets hints until they either win or run out of attempts. The goal was to debug and fix a bunch of intentionally broken game behaviors and turn the app into a working, testable project.

## Setup

1. Create and activate a virtual environment if needed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python -m streamlit run app.py
   ```

## Bugs found and fixed

The debugging work identified and addressed these game issues:

- Starting a new game did not reset the score.
- Win scoring applied an extra attempt offset even though the app passes a one-based attempt number.

The comparison behavior is handled by `check_guess()` in `logic_utils.py`; its too-high and too-low behavior was already correct, so it was retained and kept covered by tests.

## Demo Walkthrough

For this example, choose Normal difficulty and assume the secret number is 50:
1. Enter `40`. The game reports “Too Low” and “Go HIGHER!”; the score changes from 0 to -5.
2. Enter `70`. The game reports “Too High” and “Go LOWER!”; the score changes from -5 to 0.
3. Enter `50`. The game reports a win and awards 70 points for the third attempt.
4. Click “New Game”. The game starts again with zero attempts and a reset score.

## Test results

```bash
.....                                                                    [100%]
5 passed in 2.37s
```

The suite includes the original win/high/low comparison tests, a first-attempt scoring regression test, and a Streamlit `AppTest` that checks the New Game score reset. The app was also started locally and its Streamlit health endpoint returned `HTTP 200: ok`.

## Document Your Experience

I used AI to help inspect the game rules and suggest targeted tests, but checked each suggestion against the implementation before accepting it. I kept the existing high/low comparison logic because its tests already demonstrated the expected results. I accepted fixes for the score carry-over and the extra win-score attempt offset, then verified them with regression tests.

This project reinforced that an AI suggestion is a hypothesis, not proof. Reading the caller and helper together revealed that `attempt_number` is already incremented before scoring. A small test for the exact first-attempt award and an app-level test for starting a new game made both changes verifiable. The textual walkthrough records the example flow without relying on a screenshot or recording.
