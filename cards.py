import random 

suits = ['clubs', 'diamonds', 'hearts', 'spades']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

deck = [(r, s) for r in ranks for s in suits]

random.shuffle(deck)

hand1 = [deck.pop() for _ in range(5)]
hand2 = [deck.pop() for _ in range(5)]

# Check winner
hand1 = sorted([deck.pop() for _ in range(5)], key=lambda x:ranks.index(x[0]), reverse=True)
hand2 = sorted([deck.pop() for _ in range(5)], key=lambda x:ranks.index(x[0]), reverse=True)


if ranks.index(hand1[0][0]) < ranks.index(hand2[0][0]):
    print(f"Hand two wins with {hand2[0]} over {hand1[0]}")
elif ranks.index(hand1[0][0]) > ranks.index(hand2[0][0]):
    print(f"Hand one wins with {hand1[0]} over {hand2[0]}")
else:
    if suits.index(hand1[0][1]) < suits.index(hand2[0][1]):
        print(f"Hand two wins with {hand2[0]} over {hand1[0]}")
    elif suits.index(hand1[0][1]) > suits.index(hand2[0][1]):
        print(f"Hand one wins with {hand1[0]} over {hand2[0]}")


