"""KITT Version 2.1.0
26.8.19

* Runs by directly inserting string into broback function, after some input filtering
"""

import random
from textblob import TextBlob # NLP library
from filterwords import filter_words # Banned words list
from chat_data import * # Keywords and User Response lists

user_name = "Michael" # Default User name

def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in greeting_keywords:
            return random.choice(greeting_responses)


class UnacceptableUtteranceException(Exception):
    """Raise this (uncaught) exception if the response was going to trigger our blacklist"""
    pass


def starts_with_vowel(word):
    """Check for pronoun compability -- 'a' vs. 'an'"""
    return True if word[0] in 'aeiou' else False


def broback(sentence):
    """Main program loop: select a response for the input sentence and return it"""
    resp = respond(sentence)
    return resp


def find_pronoun(sent): # from the Textblob module.
    """Given a sentence, find a preferred pronoun to respond with. Returns None if no candidate
    pronoun is found in the input"""
    pronoun = None

    for word, part_of_speech in sent.pos_tags:
        # Disambiguate pronouns
        if part_of_speech == 'PRP' and word.lower() == 'you':
            pronoun = 'I'
        elif part_of_speech == 'PRP' and word == 'I':
            # If the user mentioned themselves, then they will definitely be the pronoun
            pronoun = 'You'
    return pronoun


def find_verb(sent):
    """Pick a candidate verb for the sentence."""
    verb = None
    pos = None
    for word, part_of_speech in sent.pos_tags:
        if part_of_speech.startswith('VB'):  # This is a verb
            verb = word
            pos = part_of_speech
            break
    return verb, pos


def find_noun(sent):
    """Given a sentence, find the best candidate noun."""
    noun = None

    if not noun:
        for w, p in sent.pos_tags:
            if p == 'NN':  # This is a noun
                noun = w
                break
    return noun

def find_adjective(sent):
    """Given a sentence, find the best candidate adjective."""
    adj = None
    for w, p in sent.pos_tags:
        if p == 'JJ':  # This is an adjective
            adj = w
            break
    return adj


def construct_response(pronoun, noun, verb):
    """No special cases matched, so we're going to try to construct a full sentence that uses as much
    of the user's input as possible"""
    resp = []

    if pronoun:
        resp.append(pronoun)

    # We always respond in the present tense, and the pronoun will always either be a passthrough
    # from the user, or 'you' or 'I', in which case we might need to change the tense for some
    # irregular verbs.
    if verb:
        verb_word = verb[0]
        if verb_word in ('be', 'am', 'is', "'m"):  # This would be an excellent place to use lemmas!
            if pronoun.lower() == 'you':
                # KITT will always tell the person they are not whatever they said they were
                resp.append("Sorry, you are not really")
            else:
                resp.append(verb_word)
    if noun:
        pronoun = "an" if starts_with_vowel(noun) else "a"
        resp.append(pronoun + " " + noun)

    resp.append(random.choice(("ok.", "so.", "Just spinning my wheels.", "", ))) # Not sure this is going to work in context
    return " ".join(resp)


def check_for_comment_about_bot(pronoun, noun, adjective):
    """Check if the user's input was about themselves, in which case try to fashion a response
    that feels right based on their input. Returns the new best sentence, or None."""
    resp = None
    if pronoun == 'I' and (noun or adjective):
        if noun:
            if random.choice((True, False)):
                resp = random.choice(self_verbs_with_noun_caps_plural).format(**{'noun': noun.pluralize().capitalize()})
            else:
                resp = random.choice(self_verbs_with_noun_lower).format(**{'noun': noun})
        else:
            resp = random.choice(self_verbs_with_adjective).format(**{'adjective': adjective})
    return resp


def preprocess_text(sentence):
    """Handle some weird edge cases in parsing, like 'i' needing to be capitalized
    to be correctly identified as a pronoun"""
    cleaned = []
    words = sentence.split(' ')
    for w in words:
        if w == 'i':
            w = 'I'
        if w == "i'm":
            w = "I'm"
        cleaned.append(w)

    return ' '.join(cleaned)

def respond(sentence):
    """Parse the user's inbound sentence and find candidate terms that make up a best-fit response"""
    cleaned = preprocess_text(sentence)
    parsed = TextBlob(cleaned)

    # Loop through all the sentences, if more than one. This will help extract the most relevant
    # response text even across multiple sentences (for example if there was no obvious direct noun
    # in one sentence
    pronoun, noun, adjective, verb = find_candidate_parts_of_speech(parsed)

    # If we said something about the bot and used some kind of direct noun, construct the
    # sentence around that, discarding the other candidates
    resp = check_for_comment_about_bot(pronoun, noun, adjective)

    # If we just greeted the bot, we'll use a return greeting
    if not resp:
        resp = check_for_greeting(parsed)

    if not resp:
        # If we didn't override the final sentence, try to construct a new one:
        if not pronoun:
            resp = random.choice(none_responses)
        elif pronoun == 'I' and not verb:
            resp = random.choice(comments_about_kitt)
        else:
            resp = construct_response(pronoun, noun, verb)

    # If we got through all that with nothing, use a random response
    if not resp:
        resp = random.choice(none_responses)
    # Check that we're not going to say anything obviously offensive
    filter_response(resp)

    return resp

def find_candidate_parts_of_speech(parsed):
    """Given a parsed input, find the best pronoun, direct noun, adjective, and verb to match their input.
    Returns a tuple of (pronoun, noun, adjective, verb) any of which may be None if there was no good match"""
    pronoun = None
    noun = None
    adjective = None
    verb = None
    for sent in parsed.sentences:
        pronoun = find_pronoun(sent)
        noun = find_noun(sent)
        adjective = find_adjective(sent)
        verb = find_verb(sent)
    return pronoun, noun, adjective, verb


def filter_response(resp):
    """Don't allow any words to match our filter list"""
    tokenized = resp.split(' ')
    for word in tokenized:
        for s in filter_words:
            if word.lower().startswith(s):
                raise UnacceptableUtteranceException("Oops, I was about to send you something naughty")

def start():
    """Function Containing the Launch code, no arguments."""
    line_break = ("*" * 70)
    print("\n" + line_break, "\n" + """IGNITION ACTIVATED: I am Knight Industry 2000's Micro processor, K.I.T.T.
for easy reference, KITT if you prefer.""" + "\n" + line_break)
    user_name_check()

def user_name_check():
    """Function to check user name meets requirements. Defaults to the Hoff - of course.
       Consider: Adding appropriateness filter to the name check?"""
    global user_name
    user_name = input(f"""KITT: If you are Michael Knight press [Enter], otherwise, please
tell me your name...> """)
    if len(user_name) < 1: user_name = "Michael"
    if len(user_name) >= 20:
        print("\n" + "KITT: Thats a long name, I think I will call you Michael")
        user_name = "Michael"
    print("\n" + f"KITT: So, greetings {user_name}! type to talk to me, or enter \"bye\" to exit.\n")
    kittconv()

def kittconv():
    """Main conversational function. Passes input to the broback function after conversion
    to lower case. 3 Special input filter cases managed before passing into Broback

    1. User just presses [Enter] : Kitt asks for a response
    2. User says bye or goodbye : Program Exits
    3. One of the user tokens matches the filter_words module: Raises Exception
    """
    while True:
        inp = input(user_name.upper() + ": ")
        if len(inp) < 1:
            print("\n" + f"KITT: Please give me something to work with {user_name}.")
            continue
        inp = inp.lower()
        if inp == "bye" or inp == "goodbye":
            conv_end()
        for token in inp.split():
            if token in filter_words:
                raise UnacceptableUtteranceException("Sorry, my KITT 2000 Processor cannot handle that language. Exiting Program...")
        print(f"\nKITT: {broback(inp)} \n")

def conv_end():
    """Response when the user wants to quit."""
    print("\n" + f"KITT: I am not qualified to overule your wishes - Goodbye {user_name}." + "\n" + ("*" * 70))
    sys.exit()

if __name__ == '__main__':
    start()
