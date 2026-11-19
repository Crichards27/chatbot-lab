# My Chatbot: Reflection & Submission

<<<<<<< HEAD
**Name:** ______________________  **Period:** ________  **Bot name:** Janus
=======
**Name:** ______________________  **Period:** ________  **Bot name:** ______________________
>>>>>>> cacb9c262dd022f45b2e18251506e4ff6bbefc68

> Write in your own words. Short, specific answers beat long, vague ones. Refer to what **your** bot actually did.

---

## How to turn this in

1. Fill in this file (replace the blanks and the `[...]` prompts). Save it.
2. Make sure your best work is saved in `persona.py`, `corpus.txt`, and your stage files.
3. **Commit and push** your work:
   - Click the **Source Control** icon (left sidebar) → type a message like `Finished chatbot lab` → **Commit** → **Sync Changes**.
   - Or in the Terminal: `git add .` then `git commit -m "Finished chatbot lab"` then `git push`
4. Submit the **link to your repository** (the web address of your repo on GitHub) to your teacher, in the place they tell you.
   - Your repo must be one your teacher can open: either add your teacher as a collaborator, or ask which they prefer.
   - Don't put personal information (full name, address, phone, school ID) in your bot or your corpus.

**Stage checkpoints your teacher saw (teacher initials):**
Stage 1 ____  Stage 2 ____  Stage 3 ____  Stage 4 ____  Stage 5 ____

---

## Part 1: Meet my bot

<<<<<<< HEAD
**Personality in one sentence:** Janus is a curious spaceship pilot who puts everything in the mission log and keeps a spare joke in the toolbox.

**Something I'm proud of in `persona.py` or `corpus.txt`:** The word groups let Janus hear “puppy” and use a pet reply without needing a separate rule for every animal.
=======
**Personality in one sentence:** [...]

**Something I'm proud of in `persona.py` or `corpus.txt`:** [...]
>>>>>>> cacb9c262dd022f45b2e18251506e4ff6bbefc68

**A real conversation.** Paste at least 8 lines of chat with your finished bot (copy from the Terminal):

```
<<<<<<< HEAD
Janus: Hello, I am Janus. Tell me what is on your mind. (type 'bye' to leave)
You: puppy
Janus: What's the weirdest thing your pet does?
You: I am nervous about the dance
Janus: Why do you say you are nervous about the dance?
You: I hate my homework
Janus: Is school getting easier or harder lately?
You: /peek school
Janus: After 'school' I usually see: can (1), feels (1), <end> (1)
You: spare
Janus: Spare battery for dramatic pauses.
You: spare
Janus: Spare joke in my toolbox.
You: I am not happy
Janus: Tell me more about what is going well.
You: bye
Janus: Goodbye. It was nice talking with you.
=======
[paste here]
>>>>>>> cacb9c262dd022f45b2e18251506e4ff6bbefc68
```

---

## Part 2: What I learned (answer all)

1. **The "hi in this" bug (Stage 1).** In your own words, why did the bot say "Hello!" to "this is hard", and how did splitting the sentence into a list of words fix it?

<<<<<<< HEAD
   Stage 1 looked for the letters `hi` anywhere in the input, and those letters are in `this`. Stage 2 sees `this`, `is`, and `hard` as separate words, so none of them match `hi`.

2. **Important word (Stage 3).** Which method does your bot use to pick the important word (first word, longest word, or your own scoring)? Give one example sentence where it picked a **good** word and one where it picked a **bad** word. Why?

   Janus skips stop words, gives each remaining word a point per letter, and adds two points for a known topic and two for being last. In “My teacher assigned a gigantic project,” it picked `project`, which is what the sentence is about. In “I missed the bus yesterday,” it picked `yesterday` because it's long and comes last, but `bus` would have led to a better follow-up.

3. **Reflection and rule order (Stage 4).** What does `reflect()` do? Why did `I hate my homework` get a different kind of reply from `I am nervous about the dance`?

   `reflect()` swaps words such as `I` → `you`, `am` → `are`, and `my` → `your`. `Homework` belongs to the school group, and the topic rule runs before the reflection rule. The dance sentence didn't match a topic group, so Janus reflected it back instead.

4. **N-grams (Stage 5).** In your own words, what does the bot store in its model, and how does it use that to write a sentence? What changed when you used `N = 3` instead of `N = 2`, or when you added lines to `corpus.txt`?

   The model stores each context and a list of words that followed it in the corpus. A word that followed that context more often appears more times in the list, so it's more likely to be picked. Janus adds a word, shifts the context, and repeats until it hits the end marker or the word limit. `N = 3` uses two words of context instead of one, so the next word usually fits better, but the bot can copy more of a training line. The new corpus lines gave it things to say about toolboxes, spare batteries, and the rover.
=======
   [...]

2. **Important word (Stage 3).** Which method does your bot use to pick the important word (first word, longest word, or your own scoring)? Give one example sentence where it picked a **good** word and one where it picked a **bad** word. Why?

   [...]

3. **Reflection and rule order (Stage 4).** What does `reflect()` do? Why did `I hate my homework` get a different kind of reply from `I am nervous about the dance`?

   [...]

4. **N-grams (Stage 5).** In your own words, what does the bot store in its model, and how does it use that to write a sentence? What changed when you used `N = 3` instead of `N = 2`, or when you added lines to `corpus.txt`?

   [...]
>>>>>>> cacb9c262dd022f45b2e18251506e4ff6bbefc68

---

## Part 3: Thinking like an engineer

5. **Where my bot fails.** Describe one thing it gets wrong or one reply that makes no sense. What would you need to change to fix it?

<<<<<<< HEAD
   When I typed “I am not happy,” Janus asked what was going well. It matched `happy` and ignored `not`. I would make the mood and topic checks look for a negation before a mood word and skip the positive match when they find one.

6. **Does it understand?** Your bot can keep a conversation going. Does it *understand* what you say? Explain what you think is different between what your bot does and what a person does.

   No. Janus follows rules and picks words based on what it saw in the corpus. A person can use the rest of the conversation to tell what I mean, even when the exact words are unfamiliar or I’m being sarcastic.

7. **Hand-made vs. learned.** In Stage 4 you typed lists of related words by hand (`mom`, `dad`, `sister` → family). Our class discussed how word2vec could learn those groups automatically. What is the advantage of learning them from lots of text? What could go wrong?

   Learning from lots of text could find related words I forgot to put in the list. But words can show up in the same situations without meaning the same thing. For example, `happy` and `sad` can both follow `I feel`. The model might also pick up biases in the texts it learns from.

8. **If I had more time**, the next feature I would add is: negation-aware mood replies. I would start by testing `I am happy`, `I am not happy`, and `I am not sad`, then updating both mood checks so the negated word doesn't trigger the wrong reply.
=======
   [...]

6. **Does it understand?** Your bot can keep a conversation going. Does it *understand* what you say? Explain what you think is different between what your bot does and what a person does.

   [...]

7. **Hand-made vs. learned.** In Stage 4 you typed lists of related words by hand (`mom`, `dad`, `sister` → family). Our class discussed how word2vec could learn those groups automatically. What is the advantage of learning them from lots of text? What could go wrong?

   [...]

8. **If I had more time**, the next feature I would add is: [...] and I would start by: [...]
>>>>>>> cacb9c262dd022f45b2e18251506e4ff6bbefc68

---

## Part 4: Honest process notes

<<<<<<< HEAD
- **Help I used** (classmates, teacher, websites, or AI tools), and what it helped with: Hermes, an AI assistant, helped implement the stages, test the replies, and draft this reflection.
- **The hardest bug I fixed** and how I found it: A test went from `I feel sad` to `I am happy about school`. Janus picked `school` and missed the mood change. The fix was to check mood words separately from the main topic.
- **Which stage was hardest, and why:** Stage 5 had the most moving parts. The model has to learn the word pairs, choose a next word, shift the pair, and stop in the right place.
=======
- **Help I used** (classmates, teacher, websites, or AI tools), and what it helped with: [...]
- **The hardest bug I fixed** and how I found it: [...]
- **Which stage was hardest, and why:** [...]
>>>>>>> cacb9c262dd022f45b2e18251506e4ff6bbefc68
