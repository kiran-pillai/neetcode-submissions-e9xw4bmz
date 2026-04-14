class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */


    // longestConsecutive(nums) {
    //     let max=0
    //     let set=new Set(nums)

    //     for(const num of set){
    //         let counter=0
    //         let currNum=num
    //         while(set.has(currNum)){
    //             counter+=1
    //             currNum+=1
    //         }
    //         max=Math.max(max,counter)
    //     }
    //     return max
    // }
      longestConsecutive(nums) {
        let setNums=new Set(nums)
        let max=0
        if(nums.length===0)return 0
        for(const num of setNums){
            if(!setNums.has(num-1)){
                let length=1
                while(setNums.has(length+num)){
                    length+=1
                }
                max=Math.max(max,length)
            }
        }
                    return max

      }
}
