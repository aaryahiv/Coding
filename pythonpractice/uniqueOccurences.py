from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)
        occurrence_counts = list(freq.values())
        unique_counts = set(occurrence_counts)
        return len(occurrence_counts) == len(unique_counts)
