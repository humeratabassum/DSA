class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist1 = abs(x - z)  # Distance of Person 1 to Person 3
        dist2 = abs(y - z)  # Distance of Person 2 to Person 3

        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0

        