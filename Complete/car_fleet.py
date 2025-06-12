class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort descending
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        times = [(target - pos) / spd for pos, spd in cars]

        fleets = 1
        for i in range(1, len(times)):
            # current faster prev add to fleet, reduce to fleet time
            if times[i] <= times[i-1]:
                times[i] = times[i-1]
            # else new fleet
            else:
                fleets += 1
        
        return fleets