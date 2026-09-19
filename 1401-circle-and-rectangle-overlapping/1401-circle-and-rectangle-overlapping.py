class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest x-coordinate on the rectangle to the circle's center
        closestX = max(x1, min(xCenter, x2))
        
        # Find the closest y-coordinate on the rectangle to the circle's center
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the squared distance between the circle's center and this closest point
        distanceSquared = (xCenter - closestX) ** 2 + (yCenter - closestY) ** 2
        
        # If the squared distance is less than or equal to the squared radius, they overlap
        return distanceSquared <= radius ** 2
