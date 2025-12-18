#Normal Writing Editon
class StringTraverse:
    def __init__(self, text):
        self.text = text
    def traverse_words(self):
        words = self.text.split()
        for i, word in enumerate(words, start=1):
            print(f"Word {i}: {word}")
UI = input("Enter a string: ")
T = StringTraverse(UI)
T.traverse_words()