from Profile import *
import statistics
import json

def create_person(transactions_list, location):
    # list of restaurant transactions
    newProfile = Profile()
    tot_spend = 0
    num_restaurant_transactions = 0
    favorites = {}
    prices = []
    for transaction in transactions_list:
        newProfile.totalSpent += transaction[u'amount']
        prices.append(transaction[u'amount'])
    category_scores = {}
    newProfile.transactions = transactions_list
    #Putting duplicate transactions into favorites
    for rest in newProfile.transactions:
        if rest[u'name'] in favorites:
            favorites[rest[u'name']] += 1
        else:
            favorites[rest['name']] = 1
        for tag in rest[u'category']:
            # update to skew towards recent transactions
            if tag in category_scores:
                category_scores[tag] += 1
            else:
                category_scores[tag] = 1
    prices.sort()
    # newProfile.medianSpending = statistics.median(prices)
    avgspend = newProfile.totalSpent/len(newProfile.transactions)
    newProfile.favorites = reversed([x for x in sorted(newProfile.favorites.items(), key=lambda kv: kv[1])])
    newProfile.category_scores = category_scores
    return newProfile


