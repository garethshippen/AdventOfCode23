from collections import Counter
class Card():
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.hand = self.determine_hand()
        self.rank = self.make_rank()

    # replace with the modal card. if there is no modal card, replace with the highest matching card
    def improve_cards(self, cards):
        def get_key(item): # allows sorting in rank order
            ranks = list("AKQT98765432J")
            priority = list(range(len(ranks)))
            look_up = {key:value for key,value in zip(ranks, priority)}
            return look_up[item]

        def get_modal(cards): #returns the highest modal card, or None if no modal
            cards = cards.replace("J", "")
            count = Counter(cards)
            freq = 2
            modes = []
            for pair in count.most_common():
                if pair[1] >= freq:
                    freq = pair[1]
            for pair in count.most_common():
                if pair[1] == freq:
                    modes.append(pair[0])
            if len(modes) > 0:
                return sorted(modes, key = lambda x : get_key(x))[0]
            else:
                return None
                
        if "J" in cards and len(set(cards)) == 1:
            return "AAAAA" 
        if "J" in cards:
            mode = get_modal(cards)
            if mode:
                return "".join(cards).replace("J", mode)
            else:
                highest = ""
                cards = sorted(cards, key = lambda x : get_key(x))
                for c in cards:
                    if c != "J":
                        highest = c
                        break
                return "".join(cards).replace("J", highest) 
        else:
            return cards

    def determine_hand(self):
        cards = self.improve_cards(self.cards)
        count = sorted(list(Counter(cards).values()), reverse = True)
        uniques = set(cards)        
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
        sub = {'A':'z', 'K':'y', 'Q':'x', 'T':'v', '9':'u', '8':'t', '7':'s', '6':'r', '5':'q', '4':'p', '3':'o', '2':'n', 'J':'m'}
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
    #print(hand.get_cards(), i+1, hand.get_bid(), int((i+1)) * int((hand.get_bid())), sep="\t")
    total += (i+1) * int(hand.get_bid())
print(total)
