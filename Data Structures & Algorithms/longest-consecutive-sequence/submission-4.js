class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */


    longestConsecutive(nums) {
        let max=0
        let set=new Set(nums)

        for(const num of set){
            let counter=0
            let currNum=num
            while(set.has(currNum)){
                counter+=1
                currNum+=1
            }
            max=Math.max(max,counter)
        }
        return max
    }
}
