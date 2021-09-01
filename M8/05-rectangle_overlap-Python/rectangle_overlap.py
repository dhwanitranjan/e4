# rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2)
# A rectangle can be described by its left, top, width, and height. This function 
# takes two rectangles described this way, and returns True if the rectangles 
# overlap at all (even if just at a point), and False otherwise. 
# Note: here we will represent coordinates the way they are usually represented in 
# computer graphics, where (0,0) is at the left-top corner of the screen, and while 
# the x-coordinate goes up while you head right, the y-coordinate goes up while you 
# head down (so we say that "up is down")

def fun_rectangle_overlap(left1, top1, width1, height1, left2, top2, width2, height2):
    r1x1 = left1
    r1y1 = top1
    r1x2 = left1 + width1
    r1y2 = top1
    r1x3 = left1 + width1
    r1y3 = top1 - height1
    r1x4 = left1
    r1y4 = top1 - height1

    r2x1 = left2
    r2y1 = top2
    r2x2 = left2 + width2
    r2y2 = top2
    r2x3 = left2 + width2
    r2y3 = top2 - height2
    r2x4 = left2
    r2y4 = top2 - height2

    
    return True

        