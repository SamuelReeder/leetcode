class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # hashmap denotes number of prefix occurence 
        hashmap = dict()
        for word in words:
            for i in range(1, len(word) + 1):
                temp = word[:i]
                if temp in hashmap:
                    hashmap[temp] += 1
                else:
                    hashmap[temp] = 1

        out = []
        for i in range(0, len(words)):
            out.append(0)
            temp = words[i]
            for j in range(1, len(temp) + 1):
                out[i] += hashmap[temp[:j]]
        
        return out


        
