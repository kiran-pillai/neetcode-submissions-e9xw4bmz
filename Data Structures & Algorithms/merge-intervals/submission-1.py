class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda interval: (interval[0],interval[1]))
        final_arr = []
        for interval in sorted_intervals:
            curr1, curr2 = interval
            if not len(final_arr):
                final_arr.append(interval)
            last1, last2 = final_arr[-1]
            if last2>=curr1:
                final_arr[-1] = [min(last1,curr1), max(last2,curr2)]
            else:
                final_arr.append(interval)
            
        return final_arr