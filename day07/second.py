from collections import Counter


with open("data", "r") as file_handle:
    lines = file_handle.readlines()


class Card:
    value_map = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'T':10,
        'J':1, # J is joker and has value 1
        'Q':12,
        'K':13,
        'A':14
    }

    def __init__(self, card: str):
        self.card = card
        self.value = Card.value_map[card]
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __repr__(self):
        return f"{self.card}"


class Hand:
    def __init__(self, cards:str, bid:str):
        self.cards = [Card(card) for card in cards]
        self.bid = int(bid)
        self.hand_type = self.get_hand_type()

    def handle_jokers(self, counts):
        nr_jokers = counts[1]
        if nr_jokers >= 4:
            # Four or five jokers makes five of a kind
            return 6
        elif nr_jokers == 3:
            if len(counts) == 2:
                # Three jokers with a pair makes five of a kind
                return 6
            elif len(counts) == 3:
                # Three jokers with no pair makes four of a kind
                return 5
        elif nr_jokers == 2:
            if len(counts) == 4:
                # Two jokers and no pair makes three of a kind
                return 3
            elif len(counts) == 3:
                # Two jokers with a pair makes four of a kind
                return 5
            elif len(counts) == 2:
                # Two jokers with three of a kind makes five of a kind
                return 6
        else:
            if len(counts) == 5:
                # One joker with no pair makes a pair
                return 1
            elif len(counts) == 4:
                # One joker with a pair makes three of a kind
                return 3
            elif len(counts) == 3:
                if 3 in counts.values():
                    # One joker with three of a kind makes four of a kind
                    return 5
                else:
                    # One joker with two pairs makes a full house
                    return 4
            elif len(counts) == 2:
                # One joker with four of a kind makes five of a kind
                return 6

    def get_hand_type(self):
        counts = Counter([card.value for card in self.cards])

        if 1 in counts.keys():
            return self.handle_jokers(counts)
              
        if len(counts) == 1:
            # Five of a kind
            return 6
        elif len(counts) == 2:
            if 4 in counts.values():
                # Four of a kind
                return 5
            else:
                # Full house
                return 4
        elif len(counts) == 3:
            if 3 in counts.values():
                # Three of a kind
                return 3
            else:
                # Two pair
                return 2
        elif len(counts) == 4:
            # One pair
            return 1
        else:
            # High card
            return 0
        
    def __lt__(self, other):
        if self.hand_type == other.hand_type:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                else:
                    return self.cards[i] < other.cards[i]  
        else:
            return self.hand_type < other.hand_type
    
    def __repr__(self):
        return f"{self.cards} {self.bid} {self.hand_type}"


def main():
    hands = sorted([Hand(*line.split()) for line in lines])
    score = [hand.bid * (rank + 1) for rank, hand in enumerate(hands)]
    return sum(score)

if __name__ == "__main__":
    print(main())
