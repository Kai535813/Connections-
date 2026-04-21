# 0 == as color place holder.
import os
class Term:
    def __init__(self, text, font):
        self.text = text
        self.font = font


    termSet1 = ["term", "terms"]
    termSet2 = []
    termSet3 = []
    termSet4 = []

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

        