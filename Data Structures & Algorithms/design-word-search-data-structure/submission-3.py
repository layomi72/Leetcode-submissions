class WordDictionary:

    def __init__(self):
        self.children = {}
        self.word = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]

        curr.word = True

    def search(self, word: str) -> bool:
        curr = self

        def dfs(j, kid):
            curr = kid
            for i in range(j,len(word)):
                char = word[i]
                if char == ".":
                    for kid in curr.children.values():
                        if dfs(i + 1, kid):
                            return True
                    return False

                  
                else:
                    if char not in curr.children:
                        return False

                    curr = curr.children[char]


            return curr.word

        return dfs(0,self)
