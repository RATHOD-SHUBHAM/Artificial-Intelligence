#TODO : SHUBHAM SHANKAR
# STUDENT ID : 1001761068

import sys
from prob import PosteriorProbability

def main(argv):
    if len(argv) > 1:
        observation = argv[1]
    else:
        observation = ""

    PosteriorProbability(observation)

if __name__ == '__main__':
        main(sys.argv)