from automata.fa.dfa import DFA
import os


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

name = input_dfa[0]
input_dfa_append = input_dfa[1:]


for lines in input_dfa_append:
    exec(lines.strip())


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
result = []
step_list = []

for cases in test:
    step_list.append(new_dfa.read_input_stepwise(cases.strip()))
    result.append(new_dfa.accepts_input(cases.strip()))


#TODO grab case results and write to an output file 
# (or terminal if not enough time to implement)

result_name = 'test_result_' + name + ".txt"

# delete file if it already exists
if os.path.exists(result_name):
        os.remove(result_name)

#create file and write results to it
q = open(result_name, 'w')

for i in range(len(result)):

    #writes bool result of test case
    q.write(str(result[i]) + ":" + " " + str(test[i]))

    #write states reached each for each state accepted
    if result[i] == True:
        q.write("states visited: ")
        for step in step_list[i]:
            q.write(str(step) + "->")
        q.write("accept\n")
    else:
        q.write("States visited: Rejected\n")

q.close()









