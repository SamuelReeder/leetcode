class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # naive approach:
        # loop through order and build up a string from s where chaarcter matching current order element is appended
        # append rest of string at end

        # better:
        # sort by hash map values
        
        hm = {c: i for i, c in enumerate(order)}

        return "".join(sorted(s, key=lambda x: hm[x] if x in hm else 27))
