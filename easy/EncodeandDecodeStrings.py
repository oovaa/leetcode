import string


class Solution:
    possibilities = string.printable

    def encode(self, strs: list[str]) -> str:
        pass

    def decode(self, s: str) -> list[str]:
        pass


strs = ["neet", "code", "love", "you"]
enc = ""

for i in strs:
    enc += f"#{len(i)}" + i

print(enc)
dec = []

for i, v in enumerate(enc):
    if enc[i] == "#" and enc[i + 1] in string.digits:
        sl = int(enc[i + 1])
        # print([enc[i : i + 2]], sl)
        hold = enc[i + 2 : i + sl + 2]
        # print(hold)
        dec.append(hold)

print(dec)
