from automata.fa.dfa import DFA
from dfa.dfa_dict_1 import trans, states, finals, alphabet, initial

new_dfa = DFA(
        states= states,
        input_symbols= alphabet,
        transitions=trans,
        initial_state=initial,
        final_states=finals
)

print(new_dfa.accepts_input('01'))





