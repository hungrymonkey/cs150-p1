""" Pylint told me I should add an doc String"""
import csv
import sys
import copy
import collections
DEPTH = 5

MOVES = ['L','R','S']

def find_adjacent( var_frontier ):
    var_moves = []
    for var_m in MOVES:
        var_v = valid_move( var_frontier, var_m)
        if var_v is not ():
           var_moves.append( var_v)
    return var_moves

def valid_move( var_frontier , var_m):
    if var_m == 'L':
        return left(var_frontier)
    elif var_m == 'R':
        return right(var_frontier)
    elif var_m == 'S':
        return suck(var_frontier)
    
def check_config( var_i ):
    return sum( var_i[:-1]) == 0

def left( var_frontier ):
    var_config, var_move = var_frontier[-1]
    var_f = [ f for f, m in var_frontier ]
    var_c = copy.copy(var_config)
    var_c[-1] -= 1 
    if inBounds( var_c ):
       if var_c not in var_f:
            return ( var_c, 'L' )
    return ()

def right( var_frontier ):
    var_config, var_move = var_frontier[-1]
    var_f = [ f for f, m in var_frontier ]
    var_c = copy.copy(var_config)
    var_c[-1] += 1 
    if inBounds( var_c ):
        if var_c not in var_f:
             return ( var_c, 'R')
    return ()

def suck( var_frontier ):
    var_config, var_move = var_frontier[-1]
    var_c = copy.copy(var_config)
    if var_c[var_c[-1]] is 1:
        var_c[var_c[-1]] -= 1
        return (var_c, 'S')
    else:
        return ()

def inBounds( var_c ):
    return var_c[-1] in range(0, len(var_c)-1)
    

def sanitize_input( var_i ):
    if inBounds( var_i ) is False:
       return False
    if all( 0 <= i <= 1 for i in var_i[:-1]) is False:
       return False
    return True

def find_path( var_c ):
    return iddfs( var_c )

def iddfs(var_c):
    for i in range(1,8):
        dls_return = dls(var_c, i)
        if len(dls_return) is not 0:
            return dls_return
    return [] 

def check_visited_neighbors( adj, visited ):
    l = []
    for a in adj:
        n, _ = a
        if not visited[str(n)]:
            l.append( a )
    return l

def dls( var_c, depth ):
    stack = []
    path = []
    stack.append( ((copy.deepcopy(var_c), "" ),0) )
    visited =  collections.defaultdict( bool )
    while stack:
        n, d = stack.pop()
        node_c, node_m = n
        path = path[:d]
        path.append( n )
        visited[str(node_c)] = True
        if check_config(node_c):
            return [ m for _, m in path ]
        adj = find_adjacent( path )
        ad = check_visited_neighbors(adj, visited)
        if not ad or d >= depth:
            path.pop()
        else:
            for a in reversed(ad):
                 stack.append(  (a,d+1) )
    return []


def dfs( var_c ):
    stack = []
    path = []
    stack.append( (list(var_c), "" ) )
    while stack:
        node_c, node_m = stack.pop()
        path.append( (node_c, node_m))
        if check_config(node_c):
            return [ m for _, m in path ]
        adj =  find_adjacent( path )
        if not adj:
            path.pop()
        else:
            for a in reversed(adj):
                stack.append(  a )
    return []


def bfs( var_c ):
    queue = []
    queue.append( [(list(var_c), "" ) ])
    while queue:
        path = queue.pop()
        node_c, node_m = path[-1]
        if check_config(node_c):
            return [ m for _, m in path ]
        adj =  find_adjacent( path )
        if not adj and not queue:
            return []
        else:
            for a in adj:
                p = list( path )
                p.append( a )
                queue.insert(0,  p )



def main():
    var_l = []
    for line in csv.reader(sys.stdin):
        var_l.append(map( lambda x: int(x), line ))
    if sanitize_input(var_l[0]) is False:
        print "invalid input"
        sys.exit(0)
    print "".join(find_path( var_l[0] ))
    


if __name__ == "__main__":
    main()
    
