class Solution:
    def mostWordsFound(self, sentences):
        ans = 0

        for sentence in sentences:
            ans = max(ans, len(sentence.split()))

        return ans