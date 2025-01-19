class Solution:
    """
    A class used to encode and decode lists of strings.

    Methods
    -------
    encode(strs: list[str]) -> str
        Encodes a list of strings to a single string.

    decode(s: str) -> list[str]
        Decodes a single string back to a list of strings.
    """

    """
        Encodes a list of strings to a single string.

        Parameters
        ----------
        strs : list[str]
            A list of strings to be encoded.

        Returns
        -------
        str
            A single string that represents the encoded list of strings.
        """
    # Implementation here

    """
        Decodes a single string back to a list of strings.

        Parameters
        ----------
        s : str
            A single string that represents the encoded list of strings.

        Returns
        -------
        list[str]
            A list of strings that were encoded in the input string.
        """

    # Implementation here
    def encode(self, strs: list[str]) -> str:
        enc = ""
        for i in strs:
            enc += f"{len(i)}#" + i
        return enc

    def decode(self, s: str) -> list[str]:
        dec = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            dec.append(s[i : i + length])
            i += length
        return dec


strs = ["we", "say", ":", "yes"]

print(Solution().decode(Solution().encode(strs)))
