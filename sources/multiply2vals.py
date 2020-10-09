'''
A simple command line tool that takes 2 values and adds them together using
the calc.py library's 'add2' function.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    print("The result is " + str(calc.multiply2(str(sys.argv[1]), str(sys.argv[2]))))
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: 'multiply2vals X Y' where X and Y are individual values.")
    print("       If add2vals is not in your path, usage is './multiply2vals X Y'.")
    print("       If unbundled, usage is 'python multiply2vals.py X Y'.")
    print("")
    sys.exit(1)
