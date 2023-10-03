from typing import List

# A, B, C, D, E, F, G, H, I
# The largest number h such that the researcher has published papers
# that have each been cited at least h times.

def hIndex(citations: List[int]) -> int: # 1, 1, 1, 2, 3, 4, 4, 5, 6
    citations.sort()

    n = len(citations)

    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i

    return 0

print(hIndex([1, 4, 1, 4, 2, 1, 3, 5, 6]))
