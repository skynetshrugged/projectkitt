# Project KITT - Version 1 
**Ross Mason, August 20-24 2019**

### Project Aim

Develop a simple conversational Chatbot in Python with the personality of KITT from the [Knight Rider (1982–1986)](https://en.wikipedia.org/wiki/Knight_Rider) Television Series.
 
This project was not intended to construct a program able pass the Turing test, but to inspire the Authors appreciation of the design and engineering challenges when creating a conversational UI.

**Part 1/2 of Project Series**

KITT Version 1 - This document  
[KITT Version 2](https://github.com/skynetshrugged/Ross-Mason.github.io/tree/master/AIProjects/Chatbots/Kittversion2) - Further functionality developed for KITT's code.

**Branches of AI Programming:**

* Knowledge reasoning
* Planning
* Machine learning
* **Natural language processing**
* Computer vision
* Robotics
* Artificial general intelligence

### Learning Objectives

* Enhance knowledge of developing Python 3 programs.
* Understand the fundamentals of coding simple rule based decisional systems with user input and response.
* Enhance knowledge of constructing Python on a modular basis with functions and classes.
* Embrace cycle of iterative development and testing of a project.

### What can KITT Do?

- [x] Run in a Python IDE or CMD Line environment.
- [x] Ask for keyboard input from a User.
- [x] Apply some basic Processing to the input, to screen out restricted words referenced from an imported .py file.
- [x] Match a limited number of user entered keywords (e.g. "Hi", "Kitt" etc) to a limited number of listed responses (sentences) and output these by "cycling" through a hard-coded list.
- [x] Kitt response circumstances are themed as Greeting Responses, None Responses (Where Kitt does not understand the input), and Self-Referencing responses, which refer to Kitt by name, and are constructed in a hierarchical format, meaning that if two keywords appear in the same utterance, they will still only yield one response dictated by nested conditionals in specific hierarchy with greetings at the top, and none responses last.
- [ ] General Responses other than those defined by the special circumstances.

### How does KITT do it?

- [x] Keywords from String input compared to specified Keywords, then list of responses as output.
- [x] Defined Functions & Objected Oriented programming paradigm.
- [x] Specific Class constructed to handle the response cycling with basic counter method called on the globally defined objects.

### Reflections

After some cursary research, realised that Natural Language Processing (NLP) is a huge AI Branch in it's own right that merits dedicated study, and connects to many other academic areas (similar to most of AI programming) specifically linguistics and grammar.

In order to avoid the frequent and deep NLP Rabbit holes, Version 1 is programmed with a basic functionality, and many potential enhancements have been collated into a Version 2 pending checklist, (and no doubt a V.3 will also be merited!).
 
KITT Version 1 (1.0 & 1.1), sticks to hardcoding and importing coded responses, rather than using pre-formated statistical responses provided by open source libraries such as NLTK. In practice this means v.1 is a superficial bot that responds to user keywords (Utterances) with pre-programmed phrases, however, does demonstrate basic functionality for the purposes of learning and future development.

### Project Files

* `filterwords.py` Contains a list of banned words.	
* `kitttemp.py`	Charts some personal self-development/learning from constructing the list cycling functionality.
* `kittv1.0.py`	KITT Chatbot program with randomised list responses.
* `kittv1.1.py`	KITT Chatbot with Response Cycling functionality.
* `readme.md`	This Document.

### Detailed Notes

* For *raw* working notes and planning for the project, please see associated Jupyter Notebook in the "Learning Python" Section of this repository.
