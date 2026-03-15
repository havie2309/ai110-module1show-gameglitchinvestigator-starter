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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
