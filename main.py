from automata.fa.dfa import DFA


#TODO grab variables of dfa from text file of dfa
f = open('/Users/shanematsushima/Dev/CS357_Final_Project/test/dfa_1.txt', 'r')
input_dfa = f.readlines()
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

for lines in input_dfa:
    exec(lines)


#TODO implement grabbed variables to create dfa

new_dfa = DFA(
    states = states,
    input_symbols= alphabet,
    transitions= transitions,
    initial_state= initial,
    final_states= finals
)

#read input txt file 
f = open('/Users/shanematsushima/Dev/CS357_Final_Project/test/testcase.txt', 'r')

#create array of test cases and run test cases in the dfa
test = f.readlines()

#close file once it has been read
f.close()

#test each test case from file
for cases in test:
    print(new_dfa.accepts_input(cases.strip()))

#TODO grab case results and write to an output file 
# (or terminal if not enough time to implement)

# out = open('put-output-results-file-here', 'w')








