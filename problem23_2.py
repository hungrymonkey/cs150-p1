""" Pylint told me I should add an doc String"""
import csv
import sys
import copy
import collections
import operator
MOVES = {'L': [0,-1],'U': [-1,0],'R': [0,1],'D': [0,-1],'S': [0,0]}

def find_adjacent( var_frontier ):
    var_moves = []
    for var_m in MOVES.keys():
        var_v = valid_move( var_frontier, var_m)
        if var_v is not ():
           var_moves.append( var_v)
    return var_moves

def valid_move( var_frontier , var_m):
    if var_m == 'S':
        return suck(var_frontier)
    else:
        return move(var_frontier, var_m)
    
def check_config( var_i ):
    return sum( map( sum, var_i[:-1])) == 0

def move( var_frontier, var_m ):
    var_config, var_move = var_frontier[-1]
    var_f = [ f for f, m in var_frontier ]
    var_c = copy.copy(var_config)
    var_c[-1] = map( operator.add, var_c[-1], MOVES[var_m] )
    if inBounds( var_c ):
       if var_c not in var_f:
            return ( var_c, var_m )
    return ()


def suck( var_frontier ):
    var_config, var_move = var_frontier[-1]
    var_c = copy.copy(var_config)
    if var_c[var_c[-1][0]][var_c[-1][1]] is 1:
        var_c[var_c[-1][0]][var_c[-1][1]] -= 1
        return (var_c, 'S')
    else:
        return ()

def inBounds( var_c ):
    coord = var_c[-1]
    try:
         a = var_c[:-1][coord[0]][coord[1]]
         return True
    except IndexError:
         return False
    

def sanitize_input( var_i ):
    if inBounds( var_i ) is False:
       return False
    if all( map( lambda l: all( 0 <= i <= 1 for i in l), var_i[:-1] ) ) is False:
       return False
    return True

def find_path( var_c ):
    return bfs( var_c )

def bfs( var_c ):
    queue = []
    queue.append( [(list(var_c), "" ) ])
    while queue:
        path = queue.pop()
        node_c, node_m = path[-1]
        if check_config(node_c):
            return [ m for _, m in path ][1:]
        adj =  find_adjacent( path )
        if not adj and not queue:
            return []
        else:
            for a in adj:
                p = list( path )
                p.append( a )
                queue.append( p )



def main():
    var_l = []
    for line in csv.reader(sys.stdin):
        var_l.append(map( lambda x: int(x), line ))
    if sanitize_input(var_l) is False:
        print "invalid input"
        sys.exit(0)
    print "".join(find_path( var_l ))
    


if __name__ == "__main__":
    main()
    
