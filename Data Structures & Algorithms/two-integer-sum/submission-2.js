class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let dict={}
        let i=0
        for (const num of nums){
            dict[num]=i
            i++
        }
        for(let i=0;i<nums.length-1;i++){
            let valueNeeded=target-nums[i]
            if(dict[valueNeeded] && i!=dict[valueNeeded]){
                return [i,dict[valueNeeded]]
            }
        }

    }
}
