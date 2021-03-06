from automata.fa.dfa import DFA
import os, sys

print(sys.argv[1])
print(sys.argv[2])

#grab variables of dfa from text file of dfa
f = open(str(sys.argv[1]), 'r')
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


#implement grabbed variables to create dfa

new_dfa = DFA(
    states = states,
    input_symbols= alphabet,
    transitions= transitions,
    initial_state= initial,
    final_states= finals
)

#read input txt file 
f = open(str(sys.argv[2]), 'r')

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


# grab case results and write to an output file
# Output file is placed in a folder called results for easy of access 
# (or terminal if not enough time to implement)

cwd = os.getcwd()
result_name = str(cwd) + '/results/test_result_' + name + ".txt"

# delete file if it already exists
if os.path.exists(result_name):
        os.remove(result_name)

#create file and write results to it
q = open(result_name, 'w')

for i in range(len(result)):

    #writes bool result of test case
    q.write(('Accept' if result[i] else 'Reject') + ": " + str(test[i]) + "\n")

    #write states reached each for each state accepted
    if result[i] == True:
        q.write("States Visited: ")
        for step in step_list[i]:
            q.write(str(step) + "->")
        q.write("accept\n")
    else:
        q.write("States Visited: Rejected\n")
    
    q.write("--------------------------------------------\n")

q.close()
