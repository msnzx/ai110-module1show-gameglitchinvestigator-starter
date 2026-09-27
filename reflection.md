# 💭 Reflection: Game Glitch Investigator

The game looked broken when I first ran it. The app loaded, but the number guessing flow was inconsistent and the hint messages contradicted the actual comparison logic. I had to treat it like a debugging exercise instead of just a UI polish task, because several issues were caused by the same root problem: game state was getting reset in the wrong places and the helper functions were returning the wrong shape of data.

## 1. What was broken when you started?

The first run showed a game that looked functional from the outside, but the results were wrong in obvious ways. The secret number changed unexpectedly, the hints told the player the opposite direction, and the new-game flow did not behave consistently. This made it impossible to trust the game state or the feedback shown to the user.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 60 when secret is 50 | “Too High” result | App reported the player was too low and should go higher | Logic returned reversed comparison |
| Guess 40 when secret is 50 | “Too Low” result | App reported the player was too high and should go lower | Hint text contradicted comparison |
| Click New Game after a win | Start a fresh game with a new secret | Secret and attempt state were inconsistent and sometimes stale | Streamlit reruns reset state incorrectly |
| Submit a valid guess | Attempt counter updates once | Invalid or inconsistent user flow could drift from the intended count | Game state not managed reliably |

---

## 2. How did I use AI as a teammate?

I used Copilot as a debugging assistant while I checked the logic and tested my fixes. One AI suggestion I accepted was the idea to separate outcome detection from display text, which made sense because the app needed a clean comparison result and a separate user-facing hint. I verified that this was correct by running the unit tests and checking that the output matched the expected guess behavior.

One suggestion I did not accept as written was a broader redesign that kept all logic inside the Streamlit app and used heavier rerun-based state handling. It was plausible, but it was too complicated for this small project and made the code harder to test. I simplified it by keeping the comparison rules in `logic_utils.py` and using a small, explicit `get_hint_message` helper, which made the logic easier to reason about and verify.

---

## 3. Debugging and testing my fixes

I decided a bug was really fixed when the behavior matched the expected result in a real test and the game flow remained stable after a rerun. I ran `pytest` after each major fix so I could confirm that the logic contract was correct rather than only looking at the rendered UI.

The most useful test was the core comparison test suite because it checked the real contract of `check_guess()`: win, too high, and too low. The tests showed the bug clearly because the helper returned a tuple instead of the expected simple outcome string, which also explained why the app was behaving inconsistently.

AI helped me think about what to test, especially around “wrong branch” logic and the need to separate raw comparison results from hint strings. That made the testing process much more targeted than just checking the UI one click at a time.

---

## 4. What I learned about Streamlit and state

Streamlit reruns the script every time the app updates, which means variables in normal Python memory are recreated unless they are stored in `st.session_state`. I explained this to myself as a state reset problem: the app was acting as if the secret number had to be regenerated every time a button was pressed, which is exactly what happens when the state is not preserved.

Session state is important because it keeps the game’s current secret, attempts, score, and status across reruns. Without that, the app appears random and inconsistent because it is effectively reinitializing itself during each interaction. Once I stored the values correctly, the game became stable and predictable.

---

## 5. Looking ahead: my developer habits

One habit I want to reuse is writing a small test first for a game rule before changing the code. That gave me a clean target and prevented me from guessing at the fix. I also want to keep AI suggestions scoped to the actual bug instead of accepting a larger refactor unless it clearly improves readability and testability.

Next time, I would be more explicit with the AI about the exact function contract I want, such as “return a single outcome string, not a tuple,” because that reduces confusion. This project changed the way I think about AI-generated code: it can be useful and fast, but it still needs verification, testing, and judgment before it is trustworthy.
