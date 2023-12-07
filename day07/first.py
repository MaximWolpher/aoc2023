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
        'J':11,
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

    def get_hand_type(self):
        counts = Counter([card.value for card in self.cards])
        if len(counts) == 1:
            return 6
        elif len(counts) == 2:
            if 4 in counts.values():
                return 5
            else:
                return 4
        elif len(counts) == 3:
            if 3 in counts.values():
                return 3
            else:
                return 2
        elif len(counts) == 4:
            return 1
        else:
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
