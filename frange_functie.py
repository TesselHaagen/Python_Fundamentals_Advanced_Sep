from decimal import Decimal 

def frange(start: Decimal, stop: Decimal, step=Decimal(1.0), endpoint=False):
    """
    Returns a sequence of floats with an increment of the step size, starting at start and stopping at stop.

    Arguments:
     - start (float): the start value of the list
     - stop (float): the stop value of the list
     - step (float): the steps between the elements of the list
     - endpoint (bool): 
    
    Returns:
     A list with floats
    """
    numbers = []
    while True:
        numbers.append(Decimal(start))

        start += Decimal(step) 

        if start > stop and endpoint or start >= stop and not endpoint:
            break
    
    return numbers

print(frange(1, 5, 0.5, True))

