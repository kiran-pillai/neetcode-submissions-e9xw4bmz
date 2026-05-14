class Solution:

    """
    Approaches:
    - SLiding window
    - Normal for loop with counter
    """

    def largestGoodInteger(self, num: str) -> str:

        maxx = float('-inf')
        l, r = 0, 1
        counter = 0
        while r<len(num):
            if num[r] != num[r-1]:
                if r-l == 3:
                    maxx = max(maxx, int(num[l:r]))
                l=r
                counter = 0
            else:
                counter+=1
            r+=1
        if r-l >=3:
            [1,2,3,4]

            maxx = max(maxx, int(num[len(num)-3:]))
        final_max = maxx
        if final_max== float('-inf'):
            final_max = ""
        elif final_max == 0:
            final_max = "000"
        else:
            final_max = str(final_max)
        return final_max