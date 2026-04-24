# 0 == as color place holder.
import os
class Term:
    def __init__(self, text, font):
        self.text = text
        self.font = font

    termSets = [
        { "set1": [1,1,1,1], "set2": [12,12,12,12], "set3": [13,13,13,13], "set4": [14,14,14,14],},
        { "set1": [2,2,2,2], "set2": [22,22,22,22], "set3": [23,23,23,23], "set4": [24,24,24,24],},
        { "set1": [3,3,3,3], "set2": [32,32,32,32], "set3": [33,33,33,33], "set4": [34,34,34,34],},
        { "set1": [4,4,4,4], "set2": [42,42,42,42], "set3": [43,43,43,43], "set4": [44,44,44,44],}
    
    ]
    #background.set_colorkey((0,0,0))
    
    def displaySet(self, termSet1, termSet2, termSet3, termSet4):
        for term in termSet1:
            print(f"Term: {term.text}, Font: {term.font}")
        for term in termSet2:
            print(f"Term: {term.text}, Font: {term.font}")
        for term in termSet3:
            print(f"Term: {term.text}, Font: {term.font}")
        for term in termSet4:
            print(f"Term: {term.text}, Font: {term.font}")

        