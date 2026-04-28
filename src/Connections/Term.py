class Term:
    def __init__(self, text, font):
        self.text = text
        self.font = font

    termSets = [
        { "set1": ["a","a","a","a"], "set2": ["b","b","b","b"], "set3": ["c","c","c","c"], "set4": ["d","d","d","d"] },
        { "set1": ["e","e","e","e"], "set2": ["f","f","f","f"], "set3": ["g","g","g","g"], "set4": ["h","h","h","h"] },
        { "set1": ["i","i","i","i"], "set2": ["j","j","j","j"], "set3": ["k","k","k","k"], "set4": ["l","l","l","l"] },
        { "set1": ["m","m","m","m"], "set2": ["n","n","n","n"], "set3": ["o","o","o","o"], "set4": ["p","p","p","p"] }
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

        