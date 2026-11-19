"""
persona.py  --  YOUR BOT'S PERSONALITY LIVES HERE.

This file is only data: a name, phrases, and word lists. You will edit it in
every stage. The more creative you get here, the more your bot feels like a
real character (a sarcastic coach? a pirate? a robot who loves pizza?).

Other files borrow this data with an import, like:
    from persona import BOT_NAME
"""

# ---------------------------------------------------------------------------
# BASICS
# ---------------------------------------------------------------------------
BOT_NAME = "Janus"  # TODO: rename your bot!

GREETING = "Hello, I am {name}. Tell me what is on your mind."
FAREWELL = "Goodbye. It was nice talking with you."

# ---------------------------------------------------------------------------
# STAGE 2: topic words and the replies the bot can choose from.
# Format:  "word the user types": ["reply 1", "reply 2", ...]
# TODO: add at least 5 topics of your own!
# ---------------------------------------------------------------------------
RESPONSES = {
    "school": [
        "What part of school is on your mind?",
        "Is school getting easier or harder lately?",
        "Tell me about your favorite class. Or your least favorite.",
    ],
    "family": [
        "Tell me more about your family.",
        "How do you get along with your family?",
        "Who in your family do you talk to the most?",
    ],
    "sports": [
        "What do you love most about playing sports?",
        "Do you play better alone or with a team?",
        "What is the hardest part of training?",
    ],
    "sad": [
        "I am sorry you feel that way. What happened?",
        "When did you start feeling sad?",
        "Is there anything that usually cheers you up?",
    ],
    "happy": [
        "That is great! What made you happy?",
        "Tell me more about what is going well.",
    ],
    "computer": [
        "Do you like working with computers?",
        "What would you build if you could build anything?",
    ],
    "food": [
        "What is your favorite meal?",
        "Do you cook, or do you just eat?",
    ],
    "friends": [
        "What do you like most about your friends?",
        "Do your friends feel the same way?",
    ],
    "music": [
        "What song should I add to the flight playlist?",
        "What's a song you never skip?",
        "If your day had a soundtrack, what would the first track be?",
    ],
    "art": [
        "If you could paint a mural on the ship, what would it look like?",
        "Do you plan what you're making or see where the pencil takes you?",
        "What's the last thing you made that surprised you?",
    ],
    "books": [
        "What book would you bring on a long flight?",
        "Which character would you trust to land the ship?",
        "What kind of story keeps you up past bedtime?",
    ],
    "pets": [
        "Does your pet have a name or a title, like Captain Socks?",
        "What's the weirdest thing your pet does?",
        "Could your pet be trusted with the ship's snack drawer?",
    ],
    "space": [
        "What would you visit first if you had a spaceship?",
        "Would you rather see Saturn up close or walk on the Moon?",
        "What would you name a planet if you found one?",
    ],
}

DEFAULT_RESPONSES = [
    "Please go on.",
    "I see. Tell me more.",
    "Interesting. Why do you say that?",
    "How does that make you feel?",
]

# ---------------------------------------------------------------------------
# STAGE 3: words too boring to "riff" on, and templates to riff with.
# {word} gets replaced by the important word the bot found.
# TODO: add more stop words and at least 5 templates of your own.
# ---------------------------------------------------------------------------
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "so", "if", "of", "to", "in", "on",
    "at", "for", "with", "about", "as", "by", "from", "up", "out",
    "i", "me", "my", "mine", "you", "your", "we", "our", "they", "them",
    "he", "she", "it", "its", "his", "her", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "do", "does", "did",
    "have", "has", "had", "will", "would", "can", "could", "just", "very",
    "really", "not", "no", "yes", "like", "get", "got", "im", "dont", "its",
    "what", "when", "why", "how", "who", "there", "here", "then", "than",
    "actually", "basically", "literally", "maybe", "quite", "pretty", "also",
    "still", "even", "too", "some", "any",
}

RIFF_TEMPLATES = [
    "Tell me more about {word}.",
    "Why does {word} matter to you?",
    "How does {word} make you feel?",
    "What comes to mind when you think about {word}?",
    "Let's talk about {word}. What happened?",
    "Is {word} something you think about often?",
    "Mission log entry: {word}. What should I write next?",
    "My radar picked up '{word}'. What's the story there?",
    "The flight crew wants to know: how did {word} come up?",
    "If I added {word} to the ship's log, what detail shouldn't I leave out?",
    "I don't have a button for {word}. Can you explain it to me?",
]

# ---------------------------------------------------------------------------
# STAGE 4: pronoun swapping, and groups of related words.
# ---------------------------------------------------------------------------
REFLECTIONS = {
    "i": "you",
    "me": "you",
    "my": "your",
    "mine": "yours",
    "myself": "yourself",
    "am": "are",
    "you": "I",
    "your": "my",
    "are": "am",
}

# Each topic (a key from RESPONSES) lists words that should ALL trigger it.
# This is a hand-made version of "words that mean similar things".
# TODO: add more words to every group, and add groups for your new topics.
TOPIC_GROUPS = {
    "family": ["family", "mom", "mother", "dad", "father", "parents", "sister", "brother",
               "cousin", "aunt", "uncle", "grandma", "grandpa", "siblings"],
    "school": ["school", "homework", "teacher", "class", "test", "exam", "grade", "grades",
               "quiz", "classroom", "assignment", "semester", "recess", "studying"],
    "sports": ["sports", "wrestling", "soccer", "football", "practice", "game", "team", "coach",
               "basketball", "baseball", "volleyball", "tennis", "tournament", "swimming"],
    "sad": ["sad", "unhappy", "upset", "down", "gloomy", "miserable", "blue", "lonely",
            "discouraged", "disappointed", "heartbroken"],
    "happy": ["happy", "excited", "glad", "cheerful", "thrilled", "joyful", "delighted",
              "pleased", "jubilant", "ecstatic"],
    "computer": ["computer", "code", "coding", "python", "laptop", "program", "robot",
                 "keyboard", "software", "debugging", "algorithm", "screen", "hardware"],
    "food": ["food", "pizza", "hungry", "dinner", "lunch", "snack", "cooking",
             "breakfast", "sandwich", "pasta", "recipe", "dessert", "soup"],
    "friends": ["friends", "friend", "buddy", "classmates", "bestie", "pal", "buddies",
                "friendship", "pals"],
    "music": ["music", "song", "songwriter", "playlist", "guitar", "drums", "concert"],
    "art": ["art", "drawing", "painting", "sketch", "mural", "watercolor", "sculpture"],
    "books": ["books", "book", "novel", "reading", "author", "chapter", "paperback"],
    "pets": ["pets", "pet", "puppy", "dog", "cat", "kitten", "hamster"],
    "space": ["space", "planet", "moon", "orbit", "rocket", "astronaut", "spaceship"],
}
