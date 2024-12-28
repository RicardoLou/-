class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnt = Counter(word[i - k : i] for i in range(k, n + 1, k))
        mx = max(cnt.values())
        return n // k - mx