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

The starter app had several real issues:

- The secret number was resetting on rerun because game state was not managed correctly in Streamlit.
- The higher/lower hint logic was backwards.
- New game resets were inconsistent and could leave stale state behind.
- Attempt counting and score logic were not aligned with the actual game flow.

The fixes were applied by:

- moving the comparison logic into a clean helper contract in `logic_utils.py`
- separating outcome detection from user-facing hint text
- resetting session state properly when difficulty changes or a new game starts
- counting valid attempts only after a real guess is accepted

## Demo walkthrough

1. Launch the app and choose a difficulty from the sidebar.
2. The app shows the allowed range and remaining attempts.
3. Enter a guess and submit it.
4. The game returns a correct hint such as “Go LOWER!” or “Go HIGHER!” and updates the score.
5. When the correct number is guessed, the app shows a win state and resets cleanly when the player clicks New Game.

## Test results

```bash
C:\Users\muham\Desktop\assignment 2 ai found\ai110-module1show-gameglitchinvestigator-starter> python -m pytest -q
3 passed in 0.02s
```

## Status

The core game logic is working and the project passes its pytest checks. The app now behaves consistently for valid guesses, invalid input, win states, and game resets.
