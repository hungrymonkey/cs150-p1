""" Pylint told me I should add an doc String"""
import csv
import sys


def find_adjacent( var_in ):
    var_frontier, var_move = var_in
    

def sanitize_input( var_i ):
    if all( 0 <= i <= 1 for i in var_i[:-1]) is False:
       return False
    return True


def check_config( var_i ):
    inital_config = var_i[len(var_i)-1]
    if len(var_i) - 1 <= inital_config:
       return False
    return sum( var_i[:-1]) == 0

def main():
    var_l = []
    for line in csv.reader(sys.stdin):
        var_l.append(map( lambda x: int(x), line ))
    if sanitize_input(var_l[0]) is False:
        print "invalid input"
        sys.exit(0)
    print check_config(var_l[0])


if __name__ == "__main__":
    main()
    
