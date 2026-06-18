class Solution(object):
    def angleClock(self, hour, minutes):
        #formula 
        hour_angle= 30 * hour + 0.5 * minutes
        minute_angle=6*minutes
        theta=abs(hour_angle-minute_angle)

        return min(theta, 360-theta)
        
