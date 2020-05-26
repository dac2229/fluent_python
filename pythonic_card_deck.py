import collections
from random import choice

#Note the use of collections.namedtuple to construct a simple
#class to represent individual cards.
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

beer_card = Card('7','diamond')
print(beer_card)

#deck responds to the len() function by returning the number of cards in it
deck = FrenchDeck()
print(len(deck))
print()

#Reading specific cards from the deck--say, the first or last--should be as easy as deck[0]
#or deck[-1], and this is what the __getitem__ method provides:
print(deck[0])
print(deck[-1])
print()

#Should we create a method to pick a random card? No need! Python already has a function to 
#get a random item from a sequence: random.choice. 
print(choice(deck))
print(choice(deck))
print()
