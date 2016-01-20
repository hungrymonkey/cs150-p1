""" Pylint told me I should add an doc String"""
import csv
import sys
import copy
import Queue


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

def heuristic_cost( var_i ):
    return sum( var_i[:-1])
    
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
    return a_star( var_c )

def a_star( var_c ):
    open_set = Queue.PriorityQueue()
    closed_set = []
    came_from = dict{str(var_c): ()}
    open_set.put((0,0,(var_c, "")))
    g_score = {str(var_c): 0}
    f_score = {str(var_c): heuristic_cost( var_c )}
    counter = 1
    while open_set:
       curr_g, curr_f, config = pq.get()
       curr_c, curr_m = config
       if check_config( curr_c ):
           return reconstruct_path( config )
       closed_set.append( str( curr_c ))
       adj =  find_adjacent( [config] )
       for n in adj:
          c, m = n
          if c in closed_set:
             continue
          tentative_g = g_score[str(curr_c)] + 1
          if c not in open_set
               open_set.put( (g, counter, n))
               counter += 1
          elif tentative_g >= g_score[str(c)]
               continue
          came_from[str(c)] = config
          g_score[str(c)] = tentative_g
          f_score[str(c)] = tentative_g + heuristic_cost( c )
              
             
    return []
       
    
def reconstruct_parth( var_i, came_from ):
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
    
