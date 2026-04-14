class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
     let map={}
     for (const s of strs){
        let key=s.split('').sort().join('')
        if(!map[key]){
            map[key]=[]
        }
        map[key].push(s)
     }
     return Object.values(map)
    }
}
