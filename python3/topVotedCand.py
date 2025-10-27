class TopVotedCandidate:

    hm = {}
    def __init__(self, persons: List[int], times: List[int]):
        # times is in increasing order

        self.ti = {time: i for i, time in enumerate(times)}

        hm = {persons[0]: 1}
        self.leaders = [[persons[0], 1]]
        for i in range(1, len(times)):
            if persons[i] not in hm:
                hm[persons[i]] = 1
            else:
                hm[persons[i]] += 1

            if hm[persons[i]] >= self.leaders[-1][-1]:
                self.leaders.append([persons[i], hm[persons[i]]])
            else:
                self.leaders.append(self.leaders[-1])
        
        self.times = times

    def q(self, t: int) -> int:
        i = self.ti[self.times[bisect.bisect_right(self.times, t) - 1]]
        return self.leaders[i][0]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
