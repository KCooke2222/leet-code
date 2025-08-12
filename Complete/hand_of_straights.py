class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if not divisible
        if len(hand) % groupSize != 0:
            return False
        
        # get freq cards
        freq = {}
        for num in hand:
            freq[num] = freq.get(num, 0) + 1
        keys = sorted(freq.keys())

        # build hands
        for key in keys:
            while freq[key] > 0: # start hand (while, can go multiple times same key)
                for i in range(groupSize):
                    if freq.get(key+i, 0) > 0:
                        freq[key + i] -= 1
                    else:
                        return False
        
        return True




