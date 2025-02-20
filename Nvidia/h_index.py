class Solution:
    def hIndex(self, citations: list[int]) -> int:
        max_val = max(citations)
        cnt_ppr = [0] * (max_val + 1)

        for citation in citations:
            cnt_ppr[citation] += 1

        curr_papers = 0

        for i in range(max_val, -1, -1):
            curr_papers += cnt_ppr[i]
            if curr_papers >= i:
                return i 
            
        return 0
