"""24.8.19 - Hacking, Learning, Adapting.

Constructing the code to cycle through the list (Testing functionality, before
moving into the main program - However, the functions in this code modify global
variables in order to save the state (Simple counter), this is not good practice,
so needed to find a better way of saving the state - incoming class definition i think.)

"""

# *****  Start: Uncomment the below for the global var altering version *****

#last_response = 0
#
#responses =  [
#             "A",
#             "E",
#             "I",
#             "O",
#             "U",
#             ]
#
#def response_cycle(lis):
#    """This function cycles through a list of responses.
#    
#    Parameters:
#        lis - list passed to cycle through"""
#    global last_response
#    if last_response >= len(lis):
#        last_response = 0
#    print(lis[last_response])
#    last_response += 1
#
#def repeat_func(times, f, *args):
#    """Simple function to repeatedly call a function X times, to practice the
#    intended functionality of the program.
#    
#    Parameters:
#        times - number of times to call the function in question
#        f - the function to call
#        *args - passing the argument needed for the function that is being called
#    """
#    for i in range(times):
#        f(*args)
#            
#repeat_func(20, response_cycle, responses)

# *****  End:  *****

"""24.8.19 - Hacking, Learning, Adapting.

Version 1.0 Kitt has 4 lists of cycling responses, which lends me to think,
do I need 4 different Classes to do the same thing (i.e. cycle through the list), or do I create one class where
the logic is set and the list data can be imported dependent on the response themes?

So, one class needed, with the functionality to take the list data into an instantiation of responsecycle object
and perform the computation and state saving on each. Affectively the program will instantiate 4 different
objects each with their own counters, and sets of list data.

"""


# I need to replace the: (random.choice(greeting_responses)) from the check for greeting function
# with a class object that cycles through those greeting_responses.

# Cut and paste some of the list code for testing purposes.

a = responsecycle(greeting_responses)
b = responsecycle(none_responses)

greeting_responses =  [
                      "Greetings and Salutations! - I'm scanning your interrogatives quite satisfactorily.",
                      "Hi! - By the way, don't touch Turbo Boost. Something tells me you shouldn\'t touch Turbo Boost.",
                      "Hello! - Do you know Michael Knight is a living... breathing... insult.",
                      ]

none_responses = [
                 "I want Custody of me in your Divorce!",
                 "A little higher, a little lower, Stop!",
                 "If I may say so, I\'m quite pleased with my new look.",
                 "I\'m already reviewing my computer logs of our confrontation.", 
                 ]

class responsecycle:
    """Class constructed to handle returning cyclical list responses, using
    object attributes, which avoids resorting to functions accessing global variables.
    
    attributes:
        count - A simple incremental count
        responselist - The selected data to pass to the object instance, in this
        case our responselists.
    """
    
    count = 0 # Every instance should have a count variable as an attribute
    
    def __init__(self, responselist):
        """Magic Method (Constructor) - Object is instantiated with a default count attribute value of 0,
        and with a Nul attribute waiting for data"""
        self.responselist = responselist
            
    def __str__(self):
        """Magic method to return the element of the list that relates to the
        count method"""
        return self.responselist[self.count]
    
    def inc(self):
        """Instance Method to increment the objects count attribute."""
        self.count += 1
                
def testgreet():
    print(a)
    a.inc()
    if a.count >= len(greeting_responses):
        a.count = 0
        
# Using the function to test repeated calls of the testgreet function to check it is
# working as intended.
    
def repeat_func(times, f, *args):
    """Simple function to repeatedly call a function X times, to practice the
    intended functionality of the program.
    
    Parameters:
        times - number of times to call the function in question
        f - the function to call
        *args - passing the argument needed for the function that is being called
    """
    for i in range(times):
        f(*args)
            
repeat_func(10, testgreet)

# Well it works, but just seems very messy/hacky way of doing it - and I am still
# using and modifying global things using a function, only this time,
# those global things are attributes of objects of type responsecycle, instead
# of globally defined variables
# There must be a better way! 






















