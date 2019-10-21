"""20.8.19: Chat Bot Project - KITT - Version 1.0

“It is said that to explain is to explain away. This maxim is nowhere so well
fulfilled as in the area of computer programming, especially in what is called
heuristic programming and artificial intelligence…Once a particular program is
unmasked, once its inner workings are explained in language sufficiently plain
to induce understanding, its magic crumbles away; it stands revealed as a mere
collection of procedures, each quite comprehensible. The observer says to himself,
I could have written that.”

— Joseph Weizenbaum, ELIZA (1966)

"""

import random
from filterwords import filter_words

user_name = "Michael" # Default User name

# List of Greetings keywords.
greeting_keywords =  [
                     "hello",
                     "hi",
                     "greetings",
                     "welcome",
                     "hiya",
                     "howdy",
                     "hey",
                     ]

# List of Kitt's Greeting Responses.
greeting_responses =  [
                      "Greetings and Salutations! - I'm scanning your interrogatives quite satisfactorily.",
                      "Hi! - By the way, don't touch Turbo Boost. Something tells me you shouldn\'t touch Turbo Boost.",
                      "Hello! - Do you know Michael Knight is a living... breathing... insult.",
                      ]

# Sentences KITT will respond with if he has no idea what the user just said.
none_responses = [
                 "I want Custody of me in your Divorce!",
                 "A little higher, a little lower, Stop!",
                 "If I may say so, I\'m quite pleased with my new look.",
                 "I\'m already reviewing my computer logs of our confrontation.", 
                 ]

# Responses if the input contains reference to kitt - Have added the talking about me
#element for my benefit, i.e to distinguish the responses from some of the none responses!
comments_about_kitt = [
                      "Talking about me? - You're just jealous.",
                     f"Talking about me? - No, I cannot. When you're one-of-a-kind, companionship does not compute.",
                      "Talking about me? - With all due respect, you are not possibly thinking of... Oh my word, you are!",
                      ]

class inappropriate_user_language_exception(Exception):
    """Raise this exception if the user input matches a keyword on the filter_words list"""
    pass

class inappropriate_bot_response_exception(Exception):
    """Raise this exception if the bots response was going to include a keyword on the filter_words list"""
    pass

def start():
    """Function Containing the Launch code, no arguments."""
    line_break = ("*" * 70)
    print("\n" + line_break, "\n" + """I am the voice of Knight Industry 2000's Micro processor, K.I.T.T.
for easy reference, KITT if you prefer.""" + "\n" + line_break)
    user_name_check()
    
def user_name_check():
    """Function to check user name meets requirements. Defaults to the Hoff - of course.
       Could have included appropriateness filter to the name check, but v.1 doesnt require."""    
    global user_name
    user_name = input(f"""KITT: If you are Michael Knight press [Enter], otherwise, please
tell me your name...> """)
    if len(user_name) < 1: user_name = "Michael"
    if len(user_name) >= 20:
        print("\n" + "KITT: Thats a long name, I think I will call you Michael")
        user_name = "Michael"
    print("\n" + f"KITT: So, greetings {user_name}! type to talk to me, or enter \"bye\" to exit.")
    kittconv()
        
def kittconv():
    """Main conversational function, creates a list of strings from the user input,
    performs some basic erroroneous input capturing and passes to the tokenified input
    to functions to parse in heirarcichal order.
    
    Checks against special case inputs first - then general response via NLP processes (not implemented in v.1),
    and finally responses when nothing else to say."""
    while True:
        inp = input(user_name.upper() + ": ")
        if len(inp) < 1:
            print("\n" + f"KITT: Please give me something to work with {user_name}.")
            continue
        inp = inp.lower()
        if inp == "bye":
            conv_end()
        tokenified = inp.split(" ")
        for word in tokenified:
            if word in filter_words:
                raise inappropriate_user_language_exception("Please refrain from inappropriate terminology. Exiting Program.")    
        if check_for_greeting(tokenified) == False:
            if check_for_reference_to_kitt(tokenified) == False:
                if check_and_respond_to_more_complex_input(tokenified) == False: # Pending other input processing code.
                    check_for_none_response(tokenified) # Check to see if nothing to respond to in the tokenified content

def check_for_greeting(check):
    """Checks an input against a list of Greeting Keywords, and
    prints a randomised response from a list of Greeting Responses.
    
    Parameters:
        Check - Tokens to check"""
    for word in check:
        if word in greeting_keywords:
            print("\n" + "KITT: " + random.choice(greeting_responses))
            return True
    return False

def check_for_reference_to_kitt(check):
    """If the user references Kitt anywhere in the input, Kitt uses some stock responses."""
    for word in check:
        if word == "kitt" or word == "k.i.t.t" or word == "kit" or word == "k.i.t.t.":
            print("\n" + "KITT: " + random.choice(comments_about_kitt))
            return True
    return False

def check_and_respond_to_more_complex_input(check):
    """Pending any number of NLP Techniques and Responses. ^^"""
    return False

def check_for_none_response(check):
    """This function simply prints and returns a random response from Kitt if nothing in the users
    input evaluates to a response from the other functions."""
    print("\n" + "KITT: " + random.choice(none_responses))
    return
                           
def output_filter(): #not used in v.1
    """Placeholder for code that is not generated from stock responses."""
    pass

def conv_end():
    """Response when the user wants to quit."""
    print("\n" + f"KITT: I am not qualified to overule your wishes - Goodbye {user_name}." + "\n" + ("*" * 70))
    sys.exit() 
    
start()


