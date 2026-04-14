class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let map={}
        for(const num of nums){
            if(map[num]){
                map[num]+=1
            }
            else{
                map[num]=1
            }
        }
        console.log(map)
        // sort values descending
        // slice k values and return keys
        let sortedObject=Object.entries(map).sort(([,a],[,b])=>b-a)
        let finalAnswer=sortedObject.slice(0,k)
        return finalAnswer.map((entry)=>entry[0])  
    

    }
}
