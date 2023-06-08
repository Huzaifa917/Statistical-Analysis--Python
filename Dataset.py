#!/usr/bin/env python
# coding: utf-8

# In[6]:


from typing import Dict, List

filename = 'transaction.txt'

def read_transactions_file(filename: str) -> Dict[str, List[Dict[str, any]]]:
    transactions = {}

    with open(filename, 'r') as f:
        for line in f:
            fields = line.strip().split(':')
            user_id = fields[0].strip()
            transaction_id = fields[1].strip()
            description = fields[2].strip()
            amount = float(fields[3].strip())
            x = float(fields[4].strip())
            y = float(fields[5].strip())
            is_fraudulent = fields[6].strip().lower() == 'true'

            if user_id not in transactions:
                transactions[user_id] = []

            transaction = {
                'transaction_id': transaction_id,
                'description': description,
                'amount': amount,
                'x': x,
                'y': y,
                'is_fraudulent': is_fraudulent
            }

            transactions[user_id].append(transaction)

    return transactions


# In[ ]:





# In[ ]:




