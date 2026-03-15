# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
When I first ran the game, it appeared to work normally, but several bugs became 
clear after playing a few rounds.

1. Hint logic bug (even attempts)
   Expected: when my guess was higher than the secret number, the game would say 
   "Too High", and when lower it would say "Too Low" - on every attempt.
   Actual: on every even-numbered attempt (2, 4, 6...), the secret number was 
   secretly converted to a string inside app.py. This caused Python to compare an 
   integer against a string, which broke the hint logic and could give completely 
   wrong directions.

2. Attempt counter starts at 1 instead of 0
   Expected: the first guess I submitted should count as attempt 1.
   Actual: the counter was initialized to 1 in session_state, so after clicking 
   Submit once it jumped to 2. This means the player silently loses one attempt 
   before they even start guessing.

3. New Game ignores difficulty setting
   Expected: clicking New Game while on Hard mode should generate a secret number 
   within the Hard difficulty range.
   Actual: the New Game button always called random.randint(1, 100) regardless of 
   the difficulty selected in the sidebar, so the difficulty setting had no real 
   effect on new games.

4. Hint messages were swapped
   Expected: "Too High" should tell me to guess lower, "Too Low" should 
   tell me to guess higher.
   Actual: the emoji and direction text were backwards - Too High said 
   "Go HIGHER" and Too Low said "Go LOWER", pointing the player in the 
   wrong direction every time.

---

## 2. How did you use AI as a teammate?
I used GitHub Copilot in VS Code throughout the project, mainly through the Chat view and Inline Chat to explain code and suggest possible fixes.

One correct suggestion Copilot gave me was explaining why the hints were wrong on even-numbered attempts. When I asked it to explain the string conversion block in app.py, it walked me through how Python compares strings using lexicographical order instead of numeric order, giving examples such as "2" > "10" evaluating to True. I verified this explanation by reviewing the code and confirming that removing the str() conversion fixed the issue in the running game.

One misleading suggestion Copilot made was recommending that I keep the TypeError fallback branch inside check_guess. It described this as a safety mechanism for unexpected input types. I rejected this suggestion because the fallback was masking the real bug rather than fixing it. The correct solution was to remove the unnecessary str() conversion so check_guess would always receive numeric inputs.

---

## 3. Debugging and testing your fixes
I considered a bug fully fixed only when two things were true: the related pytest test passed, and I could reproduce the correct behavior in the live Streamlit application.

For the hint logic bug, I wrote a test called test_check_guess_too_high that calls check_guess(80, 50) and verifies that the outcome is "Too High" and the message contains "LOWER". Before the fix, this scenario could produce incorrect results due to the string comparison. After removing the str() conversion and simplifying the check_guess logic, all 15 tests passed.

Copilot helped me understand what cases to test by explaining which inputs triggered the bug. It pointed out that even-numbered attempts were the specific failure point, which helped me design tests targeting that scenario instead of only testing normal cases.

---

## 4. What did you learn about Streamlit and state?
Streamlit behaves differently from many traditional applications because the entire script reruns from top to bottom every time a user interacts with the interface. This means that regular variables are reset each time a button is clicked or an input changes.

Session state allows values to persist across these reruns. It works like a dictionary that Streamlit maintains between executions. When values such as the secret number or attempt counter are stored in st.session_state, they survive reruns and maintain the game’s progress. Without session state, these values would reset each time the user clicked Submit.

---

## 5. Looking ahead: your developer habits
One habit I want to keep is adding FIXME comments before modifying any code. This forced me to think carefully about where the bug actually originated before attempting a fix, and it gave me a clear reference point when asking Copilot for help. It made the debugging process feel much more structured.

In future AI-assisted coding tasks, I would ask for smaller and more targeted suggestions from the start. Copilot sometimes suggested changes that touched more code than necessary, and reviewing large diffs can make it easy to overlook subtle problems. Requesting minimal fixes would make each change easier to verify.

This project also changed how I think about AI-generated code. I used to assume that if the code ran without crashing, it was probably correct. Now I understand that subtle logic bugs can exist even when the program appears to work, which is why testing and human review are still essential even when AI suggestions seem confident.
