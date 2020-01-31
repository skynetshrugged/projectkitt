# Project KITT - Version 2 
**Ross Mason, August 2019**

### Project Aim

Develop a conversational Chatbot in Python with the personality of KITT from the [Knight Rider (1982–1986)](https://en.wikipedia.org/wiki/Knight_Rider) Television Series.
 
This project was not intended to construct a program able pass the Turing test - or win the [Loebner Prize](https://medium.com/pandorabots-blog/mitsuku-wins-loebner-prize-2018-3e8d98c5f2a7#targetText=Mitsuku%20wins%20Loebner%20Prize%202018!&targetText=The%20Loebner%20Prize%202018%20was,Bruce%20Wilcox), but to inspire the authors appreciation of the design and engineering challenges when creating a conversational UI.

**Part of Series: 2/2**

KITT Version 1 - KITT's Basic Input/Output functions, responding to keywords from pre-determined lists of responses.  
KITT Version 2 - Supplementing with some basic NLP functionality (imported as blackbox from another programmer). 

### What can KITT Version 2 do, in addition to Version 1 features?

- [x] Use the TextBlob NLP software (A Python Library sitting on top of the more comphrensive and open source Natural Language Tool Kit), to construct more meaningful responses.
- [ ] Use the Class created in Version 1 to provide non-random list cycling responses.
- [ ] Converse in a meaningful way that is somewhat understandable.

### How does KITT Version 2 do it?

- [x] KITT Version 2 is based on a limited version of [Brobot](https://apps.worldwritable.com/tutorials/chatbot) an example Bot created by Liza Daly to demonstrate using NLP in a Conversational UI.

KITT Version 2 uses Textblob to tokenise, parse and catorgorise the input sentences into grammatical components,
(noun, pronoun, verb, adjective), and applies a series of heirarchical rules, dictating how to respond,
most of which end with a choice of random responses from a list, some of which try to reflect some of the users input back to the user.

KITT Version 2 - Is a combination of `Brobot` code and my KITT Version 1's code bolted together in an inelegant way.

- [x] Defined Functions & External TextBlob library.

### Reflections

I was a little lost at the start of this project, as I was looking for something that can enhance programming knowledge with an AI focus, but not overwhelming in scope. The NLTK and working through the guidance on NLP applications did not meet that criteria!

A skim through all the chapters of the the NLTK Tutorial Book has been informative me on two fronts, firstly it is a detailed guide, not just for using NLP techniques in python with the massively helpful methods in the NLTK library, but also as an intermediate Pythonic tutorial itself, with a highly comprehensive refresher of Pythonic knowledge interweaved in the book.

However, once again the breadth and depth of NLP as a subject of study in-itself has proven problematic, and although working through the many excercises in this book would be a fantastic start, this went beyond the time frames possible for this project.

In order to get the functionality I was looking for into KITT, I needed to use the example code and simpler NLP library (Textblob - which sits on the shoulders of the NLTK), by copying and hacking it from the Chatbot creation guide by Liza, however, I was able to produce an output, but I did not understand the *how or why* - perhaps this is the sacrifice I needed to make to get started?

In order to progress I went back to Liza Daly's tutorial, looked at her code in order to reverse engineer something and gain some understanding of the coded implementaton.

I bolted on my user input functionality from Kitt Version 1 - But did not include the randomised response function, as this would heave meant too many changes to code that I have not touched to maintain functionality of the NLP parsing. I did not know how Textblob or the imported logic worked, well enough to add my feature, and spending time on this aspect would have taken me further from the core aim.

I gained a lot of learning when coding this project, at least 20+ discrete writeups/lookups, which were then new additions to my learning notebooks. An absolute smasher in terms of learning experience, if not of practical value ^^.

### Project Files

* `chat_data.py`	Contains the listed responses - Imported in main program
* `deconstructing_brobot.py`	Details of hacking through original brobot code for comprehsion and enhancing functionality.
* `filterwords.py`	List of Banned Words for filtering user input and Bot output.
* `kitt_v2.1.0.py`	Main Program - runs from CMD Line or Interpreter.
* `readme.md` Notes and Configuration.
