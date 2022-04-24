import re


class Paragraph(str):

    def __init__(self, text: str):
        super(object).__init__()
        self.text = re.split('[.!?…]', text)

    def __call__(self):
        return len(self.text)

    def __ne__(self, string_to_compare):
        return len(self.text) != len(string_to_compare)

    def __neg__(self):
        return self[::-1]


class Sentence(Paragraph):

    def __init__(self):
        Paragraph.__init__(self, text)
        self.first_sentence = self.text[0]
        self.words = list(self.first_sentence.split())

    def __bytes__(self):
        return bytes(self.first_sentence)

    def __str__(self):
        return self.first_sentence

    def __repr__(self):
        return repr(self.first_sentence)


class Word(Sentence):

    def __init__(self):
        super().__init__()
        self.first_word = self.words[0]

    def __gt__(self, other):
        return len(self.first_word) > len(other)

    def __lt__(self, other):
        return len(self.first_word) < len(other)

    def __ge__(self, other):
        return len(self.first_word) >= len(other)

    def __le__(self, other):
        return len(self.first_word) <= len(other)






text = '''Pondering these words of Hali (whom God rest) and questioning their full meaning, as one who, having an intimation, yet doubts if there be not something behind, other than that which he has discerned, I noted not whither I had strayed until a sudden chill wind striking my face revived in me a sense of my surroundings. I observed with astonishment that everything seemed unfamiliar. On every side of me stretched a bleak and desolate expanse of plain, covered with a tall overgrowth of sere grass, which rustled and whistled in the autumn wind with Heaven knows what mysterious and disquieting suggestion. Protruded at long intervals above it, stood strangely shaped and sombrecoloured rocks, which seemed to have an understanding with one another and to exchange looks of uncomfortable significance, as if they had reared their heads to watch the issue of some foreseen event. A few blasted trees here and there appeared as leaders in this malevolent conspiracy of silent expectation.'''
a = Paragraph(text)
print(a.text)
print(a.__call__())
# print(a.__neg__())
f = Sentence()
print(f.first_sentence)
w = Word()
print(w.first_word)
print(w.__le__('ff'))