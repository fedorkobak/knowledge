from math import ceil

def get_P_N(K, G, M):
    '''
    Calculate the number of stairs (P) and the floor (N)
    of the flat using information about it's number (K)
    number of flats on the stairwell (G) and number
    of floors in the building.

    Paramters
    ---------
    G : int 
        number of flats on the stairwell'
    flatno : int 
        number of the flat;
    M : int 
        numver of flats in the house;

    Returns
    ---------
    P : int 
        staircase number for 
        the apartment in question;
    M : int
        floor number of the flat.
    '''
    # The number of stairwells, 
    # including all the staircases 
    # of the previous staircases
    T = ceil(K/G)
    
    P = ceil(T/M)
    N = T - (P-1)*M
    
    return P, N

def potential_transformation(curr, pot):
    '''
    Transformate potential value to real value. 
    If current value isn't defined we need to replace
    it with potential value. 
    If there is current value and it differs from
    potential value we have uncertainty that means
    that we need to replace current value with 0.

    Parameters
    ----------
    curr : int
        current value;
    pot : int
        potential value;

    Returns
    ----------
    out : int
        new current value.
    '''
    if not curr:
        return pot
    elif curr!=pot:
        return 0
    return curr
        
def sol(K1, M, K2, P2, N2):

    # if second flat is higher
    # than possible
    if N2 > M:
        return (-1, -1)
    
    # The number of stairwells in flat 2, 
    # including all the staircases of the 
    # previous staircases
    T2 = M*(P2 - 1) + N2

    # one more impossible case
    if T2 > K2:
        return (-1, -1)

    P1 = None
    N1 = None

    if T2 > 1:
        G_min = ceil(K2/T2)
        # In the description I wrote
        # formula G_max = ceil(K2/(T2-1))-1
        # but in the Python3 implementation it's
        # easier to use such formula - because
        # the `range` function, which doesn't include the
        # last value.
        G_max = ceil(K2/(T2-1))

        if G_min >= G_max-1:
            return -1, -1

        for G in range(G_min, G_max):
            # Calculate such values of P and N
            # that satisfy K1, G and M
            # but are not yet potential values
            pot_P1, pot_N1 = get_P_N(K1, G, M)
            
            # if P1 is not defined yet we fill it
            # with new value
            P1 = potential_transformation(P1, pot_P1)
            N1 = potential_transformation(N1, pot_N1)
            
    # The following cases are checked
    # when T2 = 1
    elif K1 <= K2:
        # This case is used when
        # the second flat is on the first floor
        # of the first staircase and
        # and the first flat has a lower number.
        # All the above guarantees that 
        # the first flat is on the first floor of the 
        # of the first staircase.
        N1 = 1; P1 = 1
    elif K2 > K1: 
        # This case is used when
        # the second flat is on the first floor
        # of the first staircase and
        # the first flat has a greater number.
        # We can't define how many flats there are
        # above the second flat on the same
        # staircase, so the parameters of the 
        # first flat cannot be defined.
        N1=0;P1=0
    if M==1 and N1==0:
        # If we have decided in a previous step that
        # that number of floor is underdefined. If there is
        # only one floor in the building, we can be
        # be sure that the first apartment is on the first floor.
        N1 = 1

    return P1, N1

if __name__ == "__main__":
    print(" ".join(map(str,
        sol(*map(int, input().split(" ")))
    )))
