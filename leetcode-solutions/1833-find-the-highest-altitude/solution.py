class Solution(object):
    def largestAltitude(self, gain):
        current_altitude = 0
        highest_point = current_altitude

        for altitude_gain in gain:
            current_altitude += altitude_gain
            highest_point = max(highest_point, current_altitude)

        return highest_point
