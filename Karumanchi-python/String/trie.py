class Node(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie(object):
    def __init__(self):
        self.root = Node()
        self.root.data = "/" 
    def addWord(self,word):
        current = self.root
        i=0
        while i < len(word):
            if word[i] not in current.children:
                current.children[word[i]] = Node()
            current = current.children[word[i]]
            i+=1
        current.isEnd = True


    def getWordList(self,startingCharecters):
        current = self.root
        for c in startingCharecters:
            try:
                current = current.children[c]
            except:
                return []

        return self.getWordListHelper(current,startingCharecters)

    def getWordListHelper(self,current,startingCharecters):
        if current.isEnd:
            return [startingCharecters]

        wordList = []
        for c in current.children:
            wordList.extend(self.getWordListHelper(current.children[c],startingCharecters+c))
        return wordList
    
                       