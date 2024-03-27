class Solution:
    def differByOneLetter(self, word1, word2):
        diffCount = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diffCount += 1
        return diffCount == 1


    def constructGraph(self, beginWord, wordList):
        graph = {word:set([]) for word in wordList}
        graph[beginWord] = set([])
        for key in graph.keys():
            for word in graph.keys():
                if self.differByOneLetter(key, word):
                    graph[key].add(word)
        return graph


    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        graph = self.constructGraph(beginWord, wordList)
        from functools import reduce
        bfs_levels = [set([beginWord])]
        visited = set([beginWord])
        for i in range(len(wordList)):
            next_words = list(map(lambda a:set(a), map(lambda word: graph[word].difference(visited), bfs_levels[-1])))
            if next_words == []:
                break
            next_words = reduce(lambda a,b: a.union(b), next_words)
            visited = visited.union(next_words)
            bfs_levels.append(next_words)
            if(endWord in next_words):
                break
        if endWord not in visited:
            return []
        
        queue = [[endWord]]
        sequences = []
        while queue:
            cur_seq = queue.pop(0)
            cur_word = cur_seq[0]
            if cur_word == beginWord:
                sequences.append(cur_seq)
                continue
            for prev_word in graph[cur_word].intersection(bfs_levels[len(bfs_levels)-len(cur_seq)-1]):
                queue.append([prev_word]+cur_seq)

        return sequences


                


