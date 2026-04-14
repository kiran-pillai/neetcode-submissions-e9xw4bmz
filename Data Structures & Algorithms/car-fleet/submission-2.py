class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed), reverse=True)
        fleets=0
        slowest_time=0
        print(cars)
        for p, s in cars:
            arrival_time=(target-p)/s
            if arrival_time>slowest_time:
                fleets+=1
                slowest_time=arrival_time
        return fleets
        
 

    
    """
    [3,3]
    [3,4.5,10,3]
    """
