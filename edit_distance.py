#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Module for calculating Edit Distance between two strings.


Created on Fri June 11 14:30:00 2021

@author: InstantPants

algorithm_parameters={'DELETE': 1,\
                      'INSERT': 1,\
                      'SUBSTITUTE': 2,\
                      'MATCH': 0,\
                      'show_steps': False},\
"""
from numpy import zeros # for index slicing
 

default_params = {
    'DELETE': 1,
    'INSERT': 1,
    'SUBSTITUTE': 2,
    'MATCH': 0,
    'show_steps': False
}
    
def edit_distance(X, Y, **kwargs):
    '''
    Calculates the edit distance between two string inputs X and Y

    Parameters
    ----------
    X : string
        Source text

    Y : string
        Destination text

    p : dictionary, optional
        The default is default_params.
        Dictionary of costs for each action
    '''
    params = default_params.copy()
    params.update(kwargs)

    n = len(Y)+1
    m = len(X)+1
    
    D = zeros((n, m), dtype=int)    

    if params['show_steps']:
        print("ACTIONS\nDEL: {}\nINS: {}\nSUB: {}\nMAT: {}".format(params['DELETE'],params['INSERT'],params['SUBSTITUTE'],params['MATCH']))

    # POPULATE FIRST ROW AND COLUMN with 0:x*INSERT:INSERT
    D[0,:] = [x for x in range(0,m*params['INSERT'],params['INSERT'])]
    D[:,0] = [y for y in range(0,n*params['INSERT'],params['INSERT'])]
        
    # POPULATE EDIT TABLE
    for y in range(1, n):
        for x in range(1, m):
            # CALCULATE MINIMUM ACTION
            DEL = D[y-1, x] + params['DELETE'] # N  = delete
            INS = D[y, x-1] + params['INSERT'] # W  = insert
            SUB = D[y-1,x-1] + params['SUBSTITUTE'] # NW = substitute/match
            MAT = D[y-1,x-1] + params['MATCH']
            D[y,x] = min(DEL, INS, SUB if X[x-1] != Y[y-1] else MAT)

            # PRINT ACTION TAKEN
            if params['show_steps']:
                if D[y,x] == DEL:
                    action = "DEL"
                elif D[y,x] == INS:
                    action = "INS"
                else:
                    action = "SUB" if X[x-1] != Y[y-1] else "MAT"

                print("{}-{} ({}) = {}".format(X[x-1], Y[y-1], action, D[y,x]))

    # PRINT DISTANCE TABLE
    print("MINIMUM EDIT DISTANCE TABLE\n")
    for y in range(n+1):
        for x in range(m+1):
            if (y == 0 and x == 0) or (y == 1 and x == 0) or (y == 0 and x == 1):
                # White space in top left corner
                print(' '.rjust(2), end=' ')
            elif x == 0 and y > 1:
                # Y word in left most column
                print(str(Y[y-2]).rjust(2), end=' ')
            elif y == 0 and x > 1:
                # X word in top most row
                print(str(X[x-2]).rjust(2), end=' ')
            else:
                # Edit Distance
                print(str(D[y-1,x-1]).rjust(2), end=' ')
                
            if x == m:
                print()
    
    # PRINT MINIMUM DISTANCE
    print("Minimum Edit Distance is: ", D[-1,-1])
    
    
if __name__ == '__main__':    
    edit_distance("satu", "sunda", show_steps = True)
