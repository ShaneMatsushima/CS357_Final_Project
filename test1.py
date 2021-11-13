import os

dfa_file= '/Users/shanematsushima/Dev/CS357_Final_Project/test/dfa_1.txt'

test_file= '/Users/shanematsushima/Dev/CS357_Final_Project/test/testcase.txt'


def prog(dfa, test):
    print("--------------")
    print(str(dfa))
    print("--------------")
    print(str(test))
    print("--------------")
    os.system("python test.py " + str(dfa) + " " + str(test))

prog(dfa_file, test_file)