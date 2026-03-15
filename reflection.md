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

I used GitHub Copilot in VS Code throughout this project. I used it 
mainly through the Chat view and Inline Chat to explain code and 
suggest fixes.

One correct suggestion Copilot gave me was explaining exactly why the 
hints were wrong on even attempts. When I asked it to explain the 
string conversion block in app.py, it walked me through how Python 
compares strings using lexicographical order instead of numeric order, 
giving concrete examples like "2" > "10" being True in Python. I 
verified this was correct by reading the code myself and confirming 
the fix worked in the live game after removing the str() conversion.

One misleading suggestion Copilot gave me was when it initially 
suggested keeping the TypeError fallback branch inside check_guess. 
It framed this as a safety net for unexpected input types. I rejected 
this because the fallback was actually part of the problem - it 
silently handled the broken string comparison instead of surfacing the 
real bug. The right fix was to remove the str() conversion entirely so 
check_guess never received a string in the first place.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed when two things were both true: the 
pytest test for that function passed, and I could manually reproduce 
the correct behavior in the live Streamlit app.

For the hint logic bug, I wrote a test called test_check_guess_too_high 
that calls check_guess(80, 50) and checks that the outcome is "Too High" 
and the message contains "LOWER". Before the fix this would have failed 
because the string comparison returned wrong results. After removing the 
str() conversion and simplifying check_guess, all 15 tests passed.

Copilot helped me understand what to test by explaining which inputs 
triggered the broken behavior. It pointed out that even-numbered 
attempts were the specific failure point, which helped me design a test 
that targeted exactly that scenario rather than just testing the happy 
path.

---

## 4. What did you learn about Streamlit and state?

Streamlit works differently from most apps - every time you click a 
button or interact with anything on the page, the entire Python script 
runs again from top to bottom. This is called a rerun. That means any 
regular variable you create gets reset to its starting value on every 
single click.

Session state is how you keep information alive across those reruns. 
It works like a dictionary that Streamlit saves between runs. If you 
store something in st.session_state, it survives the rerun and keeps 
its value. If you don't, it disappears. That's why the attempt counter 
and secret number had to be stored in session_state - otherwise they 
would reset every time the player clicked Submit.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is adding FIXME comments before touching any 
code. It forced me to think clearly about where the bug actually was 
before jumping into a fix, and it gave me a specific place to reference 
when asking Copilot for help. That kind of intentional marking made the 
whole debugging process feel more organized.

Next time I work with AI on a coding task I would ask for smaller, more 
targeted suggestions from the start. A few times Copilot suggested 
changes that touched more code than necessary, and reviewing large diffs 
is easy to rush. Asking for the smallest possible fix each time would 
make it easier to verify each change carefully.

This project changed how I think about AI-generated code - I used to 
assume that if the code ran without crashing it was probably correct, 
but now I understand that subtle logic bugs can hide in plain sight and 
only show up in specific situations, which is exactly why tests and 
human review matter even when the AI sounds confident.
