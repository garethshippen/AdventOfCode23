from collections import Counter
class Card():
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand = self.determine_hand()
        self.rank = self.make_rank()

    def determine_hand(self):
        count = sorted(list(Counter(self.cards).values()), reverse = True)
        uniques = set(self.cards)        
        match count[0]:
            case 5:
                return "five"
            case 4:
                return "four"
            case 3:
                if len(uniques) == 2:
                    return "house"
                else: 
                    return "three"
            case 2 :
                if len(uniques) == 3:
                    return "two"
                else:
                    return "pair"
            case _ :
                return "high"
    def make_rank(self):
        sub = {'A':'z', 'K':'y', 'Q':'x', 'J':'w', 'T':'v', '9':'u', '8':'t', '7':'s', '6':'r', '5':'q', '4':'p', '3':'o', '2':'n'}
        rank = ""
        for c in self.cards:
            rank += sub[c]
        return rank
        
    def get_cards(self):
        return self.cards
    def get_bid(self):
        return self.bid
    def get_hand(self):
        return self.hand
    def get_rank(self):
        return self.rank
    
#filename = "day6\\testhands.txt"
filename = "day6\\input.txt"
#filename = "day6\\testinput.txt"

card_buckets = [[],[],[],[],[],[],[]]

with open(filename) as source:
    for line in source.readlines():
        hand = line[0:5]
        bid = line[6:]
        bid = bid.replace("\n", "")
        hand = Card(hand, bid)
        
        match hand.get_hand():
            case "five":
                card_buckets[6].append(hand)
            case "four":
                card_buckets[5].append(hand)
            case "house":
                card_buckets[4].append(hand)
            case "three":
                card_buckets[3].append(hand)
            case "two":
                card_buckets[2].append(hand)
            case "pair":
                card_buckets[1].append(hand)
            case "high":
                card_buckets[0].append(hand)

all_hands = []
for bucket in card_buckets:
    all_hands += sorted(bucket, key=lambda x: x.get_rank())

total = 0
for i, hand in enumerate(all_hands):
    total += (i+1) * int(hand.get_bid())
print(total)