"""
STAGE 4: Related words, pronoun swapping, and memory
====================================================
Three upgrades that make the bot feel a lot smarter:

  A. TOPIC GROUPS   "mom", "dad", "sister" all mean the topic "family".
  B. REFLECTION     "I hate my homework" -> "Why do you say you hate your homework?"
  C. MEMORY         Remember earlier important words and circle back to them.

Run it:   python stage4_topics_memory.py
"""

import random

from chat_loop import run_chat
from persona import RESPONSES, DEFAULT_RESPONSES, REFLECTIONS, TOPIC_GROUPS
from stage2_word_lists import clean_words
from stage3_important_word import find_important_word, riff_on

remembered = []     # important words from earlier in the conversation
recalled = set()    # words the bot has already brought back up
mood_counts = {"sad": 0, "happy": 0}
last_mood = None


# ---------------------------------------------------------------------------
# A. Topic groups (this is a hand-made version of "words that mean similar things")
# ---------------------------------------------------------------------------
def find_topic(words):
    """Return the topic name (a key of RESPONSES) if any word belongs to a
    group in TOPIC_GROUPS, otherwise None."""
    for topic, group in TOPIC_GROUPS.items():
        for word in words:
            if word in group:
                return topic
    return None


# ---------------------------------------------------------------------------
# B. Reflection
# ---------------------------------------------------------------------------
def reflect(words):
    """Swap perspective: ['i', 'am', 'sad'] -> 'you are sad'."""
    # TODO 1: Right now this just glues the words back together unchanged.
    #   Build a new list called `swapped`. For each word: if it is a key in
    #   REFLECTIONS, add REFLECTIONS[word]; otherwise add the word itself.
    #   Then return " ".join(swapped).
    swapped = []
    for word in words:
        swapped.append(REFLECTIONS.get(word, word))
    return " ".join(swapped)


# ---------------------------------------------------------------------------
# The brain
# ---------------------------------------------------------------------------
def get_reply(user_input):
    global last_mood
    words = clean_words(user_input)
    important = find_important_word(words)

    # C. Memory: save this turn's important word for later
    if important is not None:
        remembered.append(important)

    # Track mood separately so a topic like school cannot hide a mood word.
    mood = None
    for word in words:
        for mood_name in mood_counts:
            if word in TOPIC_GROUPS[mood_name]:
                mood = mood_name
    if mood is not None:
        mood_counts[mood] += 1
        previous_mood = last_mood
        last_mood = mood
        if previous_mood is not None and previous_mood != mood:
            if mood == "happy":
                return "That sounds more upbeat than before. What changed?"
            return "That sounds like a tougher turn than before. Want to talk about it?"

    # TODO 2 (memory callback): every so often, bring up something from earlier.
    #   Fill in the blank so the bot picks a RANDOM old word (not just the first).
    if len(remembered) >= 3 and random.random() < 0.25:
        earlier = remembered[:-1] if important is not None else remembered
        choices = [word for word in earlier if word not in recalled and word not in words]
        if choices:
            old_word = random.choice(choices)
            recalled.add(old_word)
            return f"Earlier you mentioned {old_word}. Does that connect to this?"

    # Topic groups first
    topic = find_topic(words)
    if topic is not None:
        return random.choice(RESPONSES[topic])

    # Reflection: when the user is talking about themselves
    if ("i" in words or "my" in words) and len(words) >= 3:
        return f"Why do you say {reflect(words)}?"

    # Riff on the important word
    if important is not None:
        return riff_on(important)

    return random.choice(DEFAULT_RESPONSES)


if __name__ == "__main__":
    run_chat(get_reply)


# ---------------------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------------------
# TODO 3: Expand TOPIC_GROUPS in persona.py. Add 5+ words to every group and
#         create groups for your own topics (don't forget matching RESPONSES!).
#
# CHECKPOINT: type "I am nervous about the dance". Is the reply grammatical?
#   Now type "I hate my homework". Why did you get a DIFFERENT kind of reply?
#   (Hint: look at the ORDER of the rules in get_reply. Order matters!)
# Answer: Yes: "Why do you say you are nervous about the dance?" The second
# sentence matches the school group via "homework". The bot returns a school
# reply before it checks whether it should swap pronouns.
#
# THINK (this is the big idea behind word2vec): you just typed lists of words
#   that "mean the same thing" BY HAND. What if a program could LEARN those
#   groups by reading millions of sentences? Your teacher will discuss this.
# Answer: Words like "mom" and "dad" often show up around similar words,
# such as "my" and "parents". A model could learn that their contexts are
# similar without a hand-written list. Similar contexts don't always mean
# identical meanings: even opposites like "happy" and "sad" can be neighbors.
#
# CHALLENGE 1: Don't let the memory callback repeat the same old word twice.
# CHALLENGE 2: Add a mood tracker: count how many "sad" topics vs "happy"
#   topics came up, and have the bot comment when the conversation turns.
