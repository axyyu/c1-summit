from Profile import *

def create_person(transactions_list, location):
    # list of restaurant transactions
    newProfile = Profile()
    tot_spend = 0
    num_restaurant_transactions = 0
    favorites = {}
    for transaction in transactions_list:
        if transaction['category'][0] == 'restaurant':
            newProfile.transactions.append(transaction)
            newProfile.totalSpent += transaction['amount']
    category_scores = {}
    #Putting duplicate transactions into favorites
    for rest in newProfile.transactions:
        if rest in favorites:
            favorites[rest['name']] += 1
        else:
            favorites[rest['name']] = 1
        for cat in rest['category']:
            # update to skew towards recent transactions
            if cat in category_scores:
                category_scores[tag[u'alias']] += 1
            else:
                category_scores[tag[u'alias']] = 1
    avgspend = newProfile.totalSpent/len(newProfile.transactions)
    newProfile.favorites = reversed([x for x in sorted(newProfile.favorites.items(), key=lambda kv: kv[1])])
    return newProfile


