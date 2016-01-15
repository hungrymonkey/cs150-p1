""" Pylint told me I should add an doc String"""
import csv
import sys
import copy


MOVES = ['L','R','S']

def find_adjacent( var_frontier ):
    var_moves = []
    var_config, var_move = var_frontier[-1]
    var_f = [ f for f, m in var_frontier ]
    for var_m in MOVES:
        if var_m == 'L':
            try: 
                var_c = copy.copy(var_config)
                var_c[var_config[-1]-1] 
                var_c[-1] -= 1 
                if var_c not in var_f:
                   var_moves.append((var_c, 'L'))
            except IndexError:
        elif var_m == 'R':
            var_c = copy.copy(var_config)
            if var_c[-1]+1 >= len(var_c) - 1:
                var_c[-1] += 1 
                if var_c not in var_f:
                   var_moves.append((var_c, 'R'))
        elif var_m == 'S':
            var_c = copy.copy(var_config)
            if var_c[var_config[-1]] is 1:
               var_c[var_config[-1]] -= 1
               var_moves.append((var_c, 'S'))
    return var_moves
       
        
    
    

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
    
