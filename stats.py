#!/usr/bin/env python
# coding: utf-8

# In[6]:


from typing import Dict, List, Tuple
import statistics
import numpy as np
def get_average_transactions(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> float:
    """
    Returns the average transactions of a user or all users
    """
    if not isinstance(transactions, dict):
        raise TypeError("transactions must be a dictionary")
    if user_id:
        user_transactions = transactions.get(user_id, [])
        if len(user_transactions) == 0:
            return 0
        return sum(t['amount'] for t in user_transactions) / len(user_transactions)
    else:
        all_transactions = []
        for user_transactions in transactions.values():
            all_transactions += user_transactions
        if len(all_transactions) == 0:
            return 0
        return sum(t['amount'] for t in all_transactions) / len(all_transactions)

def get_mode_transactions(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> float:
    """
    Returns the mode of transactions of a user or all users
    """
    if user_id:
        user_transactions = transactions.get(user_id, [])
        if len(user_transactions) == 0:
            return 0
        return statistics.mode([t['amount'] for t in user_transactions])
    else:
        all_transactions = []
        for user_transactions in transactions.values():
            all_transactions += [t['amount'] for t in user_transactions]
        if len(all_transactions) == 0:
            return 0
        return statistics.mode(all_transactions)

def get_median_transactions(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> float:
    """
    Returns the median of transactions of a user or all users
    """
    if user_id:
        user_transactions = transactions.get(user_id, [])
        if len(user_transactions) == 0:
            return 0
        return statistics.median([t['amount'] for t in user_transactions])
    else:
        all_transactions = []
        for user_transactions in transactions.values():
            all_transactions += [t['amount'] for t in user_transactions]
        if len(all_transactions) == 0:
            return 0
        return statistics.median(all_transactions)

def get_interquartile_range(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> Tuple[float, float]:
    """
    Returns the interquartile range of a user or all users
    """
    if user_id:
        user_transactions = transactions.get(user_id, [])
        if len(user_transactions) == 0:
            return 0, 0
        values = [t['amount'] for t in user_transactions]
        q1, q2, q3 = statistics.quantiles(values, n=4)
        iqr = q3 - q1
        return iqr
    else:
        all_transactions = []
        for user_transactions in transactions.values():
            all_transactions += [t['amount'] for t in user_transactions]
        if len(all_transactions) == 0:
            return 0, 0
        q1, q2, q3 = statistics.quantiles(all_transactions, n=4)
        iqr = q3 - q1
        return q1, q3


    
    
def get_location_centroid(transactions: List[Dict[str, any]]) -> Tuple[float, float]:
    """
    Returns the centroid of all transaction locations for a given user
    """
    x_sum = 0.0
    y_sum = 0.0
    count = 0
    for transaction in transactions:
        if not isinstance(transaction['x'], (int, float)):
            raise TypeError("Value for key 'x' is not a number")
        if not isinstance(transaction['y'], (int, float)):
            raise TypeError("Value for key 'y' is not a number")
        x_sum += (transaction['x'])
        y_sum += (transaction['y'])
        count += 1

    x_centroid = x_sum / count
    y_centroid = y_sum / count

    return x_centroid, y_centroid


def get_std_dev_user_transactions(user_transactions: List[Dict[str, any]]) -> float:
    """
    Returns the standard deviation of all transactions for a given user
    """
    try:
        amounts = [t['amount'] for t in user_transactions]
        return statistics.stdev(amounts)
    except (statistics.StatisticsError, KeyError):
        return 0


def is_fraudulent(transaction: Dict[str, any]) -> bool:
    """
    Returns True if the given transaction is fraudulent, False otherwise.
    """
    return transaction['is_fraudulent']

def get_fraudulent_transactions(transactions: List[Dict[str, any]]) -> List[Dict[str, any]]:
    """
    Returns a list of all fraudulent transactions
    """
    return [t for t in transactions if is_fraudulent(t)]


def get_abnormal_user_transaction(user_transactions: List[Dict[str, any]]) -> Dict[str, any]:
    """
    Returns a transaction that is the most abnormal for a given user.
    An abnormal transaction is defined as one with a value that is more than two
    standard deviations away from the mean of all transactions for the user.
    """
    amounts = [t['amount'] for t in user_transactions]
    mean = statistics.mean(amounts)
    stdev = statistics.stdev(amounts)
    max_dev = 0
    max_dev_transaction = None
    for transaction in user_transactions:
        dev = abs(transaction['amount'] - mean) / stdev
        if dev > max_dev:
            max_dev = dev
            max_dev_transaction = transaction

    return max_dev_transaction

def get_z_score(user_transactions: List[Dict[str, any]]) -> List[float]:
    """
    Computes the Z-score of a user's transactions and returns a list of Z-scores.
    """
    amounts = [t['amount'] for t in user_transactions]
    mean = statistics.mean(amounts)
    stdev = statistics.stdev(amounts)
    return [(amt - mean) / stdev for amt in amounts]


def get_z_scores(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> List[float]:
    """
    Computes the Z-score of a user's transactions or of all users' transactions
    and returns a list of Z-scores.
    """
    if user_id:
        user_transactions = transactions.get(user_id, [])
        if len(user_transactions) == 0:
            return []
        amounts = [t['amount'] for t in user_transactions]
        mean = statistics.mean(amounts)
        stdev = statistics.stdev(amounts)
        return [(amt - mean) / stdev for amt in amounts]
    else:
        all_transactions = []
        for user_transactions in transactions.values():
            all_transactions += user_transactions
        if len(all_transactions) == 0:
            return []
        amounts = [t['amount'] for t in all_transactions]
        mean = statistics.mean(amounts)
        stdev = statistics.stdev(amounts)
        return [(amt - mean) / stdev for amt in amounts]
















def get_location_frequency(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> Dict[Tuple[float, float], int]:
    """
    Returns a dictionary containing the frequency of all transaction locations for a given user or all users
    """
    all_transactions = []
    if user_id:
        user_transactions = transactions.get(user_id, [])
        all_transactions = user_transactions
    else:
        for user_transactions in transactions.values():
            all_transactions += user_transactions
        
    if len(all_transactions) == 0:
        return {}
    locations = [tuple([t['x'], t['y']]) for t in all_transactions]
    frequency_dict = {}
    for loc in locations:
        if loc in frequency_dict:
            frequency_dict[loc] += 1
        else:
            frequency_dict[loc] = 1
    return frequency_dict









def get_location_outliers(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> Dict[Tuple[float, float], float]:
    """
    Returns a dictionary containing the location outliers for a given user or all users based on their transaction amounts
    """
    if user_id:
        user_transactions = transactions.get(user_id, [])
        if len(user_transactions) == 0:
            return {}
        values = [t['amount'] for t in user_transactions]
        q1, q2, q3 = statistics.quantiles(values, n=4)
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        locations = [tuple([t['x'], t['y']]) for t in user_transactions]
        outliers = {}
        for loc, amount in zip(locations, values):
            if amount < lower_fence or amount > upper_fence:
                outliers[loc] = amount
        return outliers
    else:
        all_transactions = []
        for user_transactions in transactions.values():
            all_transactions += user_transactions
        if len(all_transactions) == 0:
            return {}
        values = [t['amount'] for t in all_transactions]
        q1, q2, q3 = statistics.quantiles(values, n=4)
        iqr = q3 - q1
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr
        locations = [tuple([t['x'], t['y']]) for t in all_transactions]
        outliers = {}
        for loc, amount in zip(locations, values):
            if amount < lower_fence or amount > upper_fence:
                outliers[loc] = amount
        return outliers


#def get_user_outliers(user_transactions: List[Dict[str, any]], threshold: float = 1.5) -> List[Dict[str, any]]:
   
  #  Returns a list of transactions that are considered outliers for a given user based on the threshold value.
    
  #  amounts = [t['amount'] for t in user_transactions]
  #  q1, q3 = statistics.quantiles(amounts, n=4)
  #  iqr = q3 - q1
    
def get_outliers(transactions: Dict[str, List[Dict[str, any]]], user_id: str = None) -> List[Dict[str, any]]:   
    """
    Returns a list of outlier transactions using the interquartile range (IQR) method
    """
    if user_id:
        user_transactions = transactions.get(user_id, [])
        if len(user_transactions) == 0:
            return []
        values = [t['amount'] for t in user_transactions]
        q1, q3 = np.percentile(values, [25, 75])
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        return [t for t in user_transactions if t['amount'] < lower_bound or t['amount'] > upper_bound]
    else:
        all_transactions = []
        for user_transactions in transactions.values():
            all_transactions += user_transactions
        if len(all_transactions) == 0:
            return []
        values = [t['amount'] for t in all_transactions]
        q1, q3 = np.percentile(values, [25, 75])
        iqr = q3 - q1
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        return [t for t in all_transactions if t['amount'] < lower_bound or t['amount'] > upper_bound]
    
    
  
    


def get_nth_percentile(transactions: Dict[str, List[Dict[str, any]]], user_id: str, percentile: float) -> float:
    """
    Computes the nth percentile of a user's transactions and returns a float.
    """
    if user_id not in transactions:
        return None
    user_transactions = transactions[user_id]
    amounts = [t['amount'] for t in user_transactions]
    return np.percentile(amounts, percentile)

def get_nth_percentil(transactions: Dict[str, List[Dict[str, any]]], percentile: float) -> List[Tuple[str, float]]:
    """
    Computes the nth percentile of transactions for all users and returns a list of tuples containing
    the user ID and its corresponding nth percentile value.
    """
    all_transactions = []
    for user_transactions in transactions.values():
        all_transactions += user_transactions
    if len(all_transactions) == 0:
        return []
    percentile_values = []
    for user_id, user_transactions in transactions.items():
        amounts = [t['amount'] for t in user_transactions]
        nth_percentile = np.percentile(amounts, percentile)
        percentile_values.append((user_id, nth_percentile))
    return percentile_values






