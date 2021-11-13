from automata.fa.dfa import DFA
import os

dfa_file = '/Users/shanematsushima/Dev/CS357_Final_Project/test/dfa_1.txt'

test_file = '/Users/shanematsushima/Dev/CS357_Final_Project/test/testcase.txt'

states = {} 
alphabet = {} 
initial = ''
finals = {}
transitions = {}


def runProg(dfa, test):
    f = open(dfa, 'r')
    input_dfa = f.readlines()
    f.close

    name = input_dfa[0]
    input_dfa_append = input_dfa[1:]

    _locals = locals()

    for lines in input_dfa_append:
        exec(lines.strip(), globals(), _locals)
    
    

    new_dfa = DFA(
        states = states,
        input_symbols= alphabet,
        transitions= transitions,
        initial_state= initial,
        final_states= finals
    )

    f.open(test, 'r')
    test = f.readlines()
    f.close

    result = []
    step_list = []

    for cases in test:
        step_list.append(new_dfa.read_input_stepwise(cases.strip()))
        result.append(new_dfa.accepts_input(cases.strip()))

    result_name = 'test_result_' + name + ".txt"

    if os.path.exists(result_name):
        os.remove(result_name)

    f = open(result_name, 'w')

    for i in range(len(result)):
        f.write(str(result[i]) + ": " + str(test[i]))
        if result[i] == True:
            f.write("States Visited: ")
            for step in step_list[i]:
                f.write(str(step) + "->")
            f.write("accept\n")
        else:
            f.write("State Visited: Rejected\n")
    f.close()


runProg(dfa_file, test_file)