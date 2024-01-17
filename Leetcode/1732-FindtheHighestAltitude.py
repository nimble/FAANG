class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        starting_gain = 0
        for g in gain:
            starting_gain+=g
            if(starting_gain >= highest_altitude):
                highest_altitude = starting_gain
        return highest_altitude

        
