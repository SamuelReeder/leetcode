class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm = Counter(words)
        heap = []
        
        for word, freq in hm.items():
            heapq.heappush(heap, Word(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
                
        res = []
        while heap:
            res.append(heapq.heappop(heap).word)
            
        return res[::-1]
