import math
import statistics

def transaction_distance(t1: dict, t2: dict) -> float:
        
    dx = t1['x'] - t2['x']
    dy = t1['y'] - t2['y']
    return math.sqrt(dx*dx + dy*dy)
    
        


def user_distance(transactions1: list[dict], transactions2: list[dict]) -> float:
    """
    Computes the distance between two users, defined as the minimum distance between any two of their transactions.
    """
    if not transactions1 or not transactions2:
        raise ValueError("One or both of the transaction lists is empty.")
    
    min_distance = float('inf')
    for t1 in transactions1:
        for t2 in transactions2:
            try:
                d = transaction_distance(t1, t2)
                if d < min_distance:
                    min_distance = d
            except ValueError as e:
                print(f"Skipping invalid transaction pair: {e}")
    
    if min_distance == float('inf'):
        raise ValueError("No valid transaction pairs found.")
    
    return min_distance
