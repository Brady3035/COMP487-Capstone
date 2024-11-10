import random
from typing import Iterable

"""
Given a seed value and text to scramble, scramble the text in a pseudorandom order that can be reproduced with the seed.
"""
class Scrambler:
    
    def __init__(self, seed: int):
        self.seed = seed

    """
    Given the length of the text to be scrambled, set the new order
    """
    def set_order(self, text_len: int) -> Iterable[int]:
        random.seed(self.seed)
        order = list(range(text_len))
        random.shuffle(order)
        return order
    
    """
    Scramble the given unscrambled_string and output a randomly scrambled version.
    """
    def scramble(self, unscrambled_string: str) -> str:
        order = self.set_order(len(unscrambled_string))
        unscrambled_text = bytearray()
        unscrambled_text.extend(unscrambled_string.encode('utf-8'))
        scrambled_text = bytearray()
        scrambled_text.extend(unscrambled_string.encode('utf-8'))
        for i, token in enumerate(unscrambled_text):
            scrambled_text[order[i]] = token
        return scrambled_text.decode('utf-8')
    

    """
    Unscramble the given scrambled_string and output the unscrambled version.
    """
    def unscramble(self, scrambled_string: str) -> str:
        order = self.set_order(len(scrambled_string))
        unordered_text = bytearray()
        unordered_text.extend(scrambled_string.encode('utf-8'))
        ordered_text = bytearray()
        ordered_text.extend(scrambled_string.encode('utf-8'))
        for i in range(len(scrambled_string)):
            ordered_text[i] = unordered_text[order[i]]
        return ordered_text.decode('utf-8')
    
scrambler = Scrambler(2)
scrambled = scrambler.scramble("Hello World")
print(scrambled)
print(scrambler.unscramble(scrambled))
