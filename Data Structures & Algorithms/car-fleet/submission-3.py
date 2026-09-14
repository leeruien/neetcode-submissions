class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position = sorted(zip(position,speed), reverse = True)
        num_fleets = 0
        index_position = 0
        for pair in sorted_position:
            i,j = pair
            threshold = (target - i)/j
            if index_position == 0: 
                # index_speed = position.index(i)
                # threshold = (target - i)/speed[index_speed]
                num_fleets = 1
                index_position = 1
                prev = threshold
            else: 
                # index_speed = position.index(i)
                # threshold = (target - i)/speed[index_speed]
                if threshold > prev: 
                    prev = threshold
                    num_fleets += 1
        return num_fleets
                




        