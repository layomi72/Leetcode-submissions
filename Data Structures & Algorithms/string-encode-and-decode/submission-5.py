class Solution:

    def encode(self, strs: List[str]) -> str:
        size_of_string = []
        encoded = []
        for i in range(len(strs)):
            size_of_string.append(len(strs[i]))

        for i in range(len(strs)):
            encoded.append(str(size_of_string[i]))
            encoded.append("#")
            encoded.append(strs[i])

        return "".join(encoded)
        


    def decode(self, s: str) -> List[str]:
        list_strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            count = int(s[i:j])
            list_strings.append(s[j+1:j+count+1])
            i = j + count + 1

               

        return list_strings

