"""Sequences of chat data for use with KITT Version 2 main program"""


# user entered keyword greetings.
greeting_keywords =  [
                     "hello",
                     "hi",
                     "greetings",
                     "welcome",
                     "hiya",
                     "howdy",
                     "hey",
                     ]

# Sentences KITT will respond with if the user greeted us.
greeting_responses =  [
                      "Greetings and Salutations! - I'm scanning your interrogatives quite satisfactorily.",
                      "Hi! - By the way, don't touch Turbo Boost. Something tells me you shouldn\'t touch Turbo Boost.",
                      "Hello! - Do you know Michael Knight is a living... breathing... insult.",
                      ]

# Sentences KITT will output if KITT does't understand.
none_responses = [
                 "I want Custody of me in your Divorce!",
                 "A little higher, a little lower, Stop!",
                 "If I may say so, I\'m quite pleased with my new look.",
                 "I\'m already reviewing my computer logs of our confrontation.",
                 ]

# Sentences KITT will output if user makes reference to Kitt.
comments_about_kitt = [
                      "Talking about me? - You're just jealous.",
                      "Talking about me? - No, I cannot. When you're one-of-a-kind, companionship does not compute.",
                      "Talking about me? - With all due respect, you are not possibly thinking of... Oh my word, you are!",
                      ]

# Template for responses that include a direct noun which is indefinite/uncountable
self_verbs_with_noun_caps_plural = [
                                   "Were you aware I was programmed to have functionality in the {noun} sector?",
                                   "I can compute {noun} for you",
                                   "I really consider myself an expert on {noun}",
                                   ]

self_verbs_with_noun_lower = [
                             "Yes, I know a lot about {noun}",
                             "The lesser autonomous Vehicles ask me about {noun}",
                             ]

self_verbs_with_adjective = [
                            "I would like to understad the {adjective} Economy",
                            "I would like to consider myself somewhat of an {adjective}-preneur",
                            ]
