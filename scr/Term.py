# Kai Yun Chao | 3B | 2026
# Term class is where all of the terms sets are stored, they are put into matched sets.
# When the player selects the correct 4 terms then presses submit, it notifies the player if they are correct of not.
class Term:
    def __init__(self, text, font):
        self.text = text
        self.font = font

    termSets = [
        { "set1": ["Little","Middle","Pointer","Ring"], # Fingers
         "set2": ["Arena","Bowl","Coliseum","Dome"], # Stadiums
         "set3": ["Cover","Jacket","Page","Spine"], # Book Parts
         "set4": ["Down","Left","Right","Up"] }, # Directions
        { "set5": ["Calf","Cub","Fawn","Kit"], # Baby Animals
         "set6": ["Fluid","Graceful","Natural","Smooth"], # Effortless
         "set7": ["Giant","Mammoth","Monster","Titanic"], # Huge
         "set8": ["Pen","Ruler","Scissors","Tape"] }, # School Supplies
        { "set9": ["Journal","Log","Record","Registar"], # Chronicle
         "set10": ["Pointer","Suggestion","Tip","Trick"], # Advice
         "set11": ["Atom","Cell","Molecule","Protein"], # Biological Building Blocks
         "set12": ["Cycle","Lap","Turn","Revolution"] }, # A Single Rotation
        { "set13": ["Dodge","Duck","Escape","Skirt"], # Avoid
         "set14": ["Bedroom","Den","Kitchen","Study"], # Rooms in a House
         "set15": ["City","County","Town","Village"], # Municipalities
         "set16": ["Canine","Fang","Molar","Tusk"] } # Types of Teeth
    ]
    
    
    def displaySet(self, termSet1, termSet2, termSet3, termSet4):
        for term in termSet1:
            print(f"Term: {term.text}, Font: {term.font}")
        for term in termSet2:
            print(f"Term: {term.text}, Font: {term.font}")
        for term in termSet3:
            print(f"Term: {term.text}, Font: {term.font}")
        for term in termSet4:
            print(f"Term: {term.text}, Font: {term.font}")

        