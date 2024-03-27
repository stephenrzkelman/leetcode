import collections

class Solution:

    # building adjacency list takes about 40x as long, especially with longer wordLists
    def allNeighborWords(self, word):
        neighbors = []
        for i in range(len(word)):
            str1 = word[:i] 
            str2 = word[i+1:]
            for char in "qwertyuiopasdfghjklzxcvbnm":
                neighbors.append(str1 + char + str2)
        return neighbors

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        queue = collections.deque([(beginWord, 1)])
        while queue:
            cur_word, cur_len = queue.popleft()
            for neighbor in self.allNeighborWords(cur_word):
                if neighbor not in wordList:
                    continue
                if neighbor == endWord:
                    return cur_len + 1
                queue.append((neighbor, cur_len + 1))
                wordList.remove(neighbor)
        return 0