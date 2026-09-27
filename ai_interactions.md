# AI Interactions Log

This project did not use a full stretch-feature workflow, but I did use AI to debug and validate the game logic. The main value came from asking for help with the state-reset bug, the reversed hint logic, and the correct contract for helper functions.

## Core debugging prompts

**Prompt used:**

```text
The game is resetting its secret number on rerun and the hints are backwards. Explain the likely Python/Streamlit cause and suggest a clean fix.
```

**AI response summary:**

The AI identified that Streamlit reruns the script and that session state should be used to keep values like the secret number and attempts across reruns. It also pointed out that the comparison result should be a single outcome string instead of a tuple, which matched the actual bug in the helper contract.

**What I accepted:**

- preserving values in `st.session_state`
- separating `check_guess()` from user-facing hint text
- keeping the logic in helper functions so it was easier to test

**What I changed after review:**

I did not keep the full refactor in the app layer; I simplified it to a targeted helper approach in `logic_utils.py` because that kept the code readable and testable.

---

## Test help

**Prompt used:**

```text
Help me write pytest checks for a number guessing game: win case, too high case, and too low case.
```

**Result:**

I used the generated test structure as a guide and then validated the actual behavior against the project code. The final tests confirm the fix:

```bash
python -m pytest -q
3 passed in 0.02s
```

---

## Stretch features status

No stretch features were attempted for this submission. The project was completed through the required debugging and documentation work instead of additional UI or advanced AI workflows.
