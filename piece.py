from typing import List

class Piece():
    def __init__(self, start, length, source):
        self.start = start
        self.length = length
        self.source = source

    def __str__(self):
        return f"start: {self.start}, length: {self.length}, source: {self.source}"

class PieceTable():
    def __init__(self, original):
        self.original: str = original
        self.add: str = ""
        self.pieces: List[Piece] = []

    def insert(self, text: str, start: int):
        self.pieces.append(Piece(start, len(text), "add"))
        self.add = text

    def remove(self, start: int, length: int):
        self.pieces.append(Piece(start, length, "original"))

        # print(self.pieces[-1])

    def reconcile(self):
        original = self.original

        for piece in self.pieces:
            if piece.source == "add":
                original = original[:piece.start] + self.add + original[piece.start:]
            elif piece.source == "original":
                original = original[:piece.start] + original[piece.start + piece.length:]

        return original

text = "Taylor Swift wrote Folklore and Evermore"

# get idx of Folklore
idx = text.index("Folklore")
# get end idx
end_idx = idx + len("Folklore")

to_add = ", 1989,"

table = PieceTable(text)
table.insert(to_add, end_idx)

print(table.reconcile())

to_remove = "Folklore, "

idx = table.reconcile().index(to_remove)

table.remove(idx, len(to_remove))
result = table.reconcile()

print(result)