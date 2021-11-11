from os import stat_result
from typing import final
from automata.fa.dfa import DFA

f = open('put-input-dfa-file-here', 'r')

#TODO grab variables of dfa from text file of dfa

#read file and put variables based on name of categories (could be done using
# a csv or some sort of delimiter to find the variables needed easier)
# for sets, use the set() 
# for transitions, use exec() on an empty variable that has the same name 
# as the transition. look at test.py for more info

states = {} 
alphabet = {} 
initial = ''
finals = {}
transitions = {}

#TODO implement grabbed variables to create dfa

new_dfa = DFA(
    states = states,
    input_symbols= alphabet,
    transitions= transitions,
    initial_state= initial,
    final_states= finals
)


#TODO read input txt file 
f = open('put-input-string-file-here', 'r')

#TODO create array of test cases and run test cases in the dfa

test = []

for cases in test:
    print(new_dfa.accepts_input(test[cases]))

#TODO grab case results and write to an output file 
# (or terminal if not enough time to implement)

out = open('put-output-results-file-here', 'w')








