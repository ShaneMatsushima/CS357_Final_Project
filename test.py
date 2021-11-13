f = open('/Users/shanematsushima/Dev/CS357_Final_Project/dfa/dfa_1.txt', 'r')
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

for line in input_dfa:
    exec(line);

print(states)
print(alphabet)
print(initial)
print(finals)
print(transitions)