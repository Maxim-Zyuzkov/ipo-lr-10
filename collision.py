def isCorrectRect(rect):
    (x1,y1), (x2,y2) = rect
    return x1 < x2 and y1 < y2

def isCollisionRect(rect1,rect2):
    if not isCorrectRect (rect1):
        raise Exception("1 прямоугольник неправильный.")
    if not isCorrectRect(rect2):
        raise Exception("2 прямоугольник неверный.")

    x1,y1=rect1[0]
    x2,y2 = rect1[1]
    x3,y3=rect2[0]
    x4,y4 = rect2[1]
    if x2 < x3 or x4 < x1:
        return False
    if y2 < y3 or y4 < y1:
        return False
    return True

def intersectionAreaRect(rect1,rect2):
    if not isCorrectRect (rect1):
        raise Exception("1 прямоугольник неправильный.")
    if not isCorrectRect(rect2):
        raise Exception("2 прямоугольник неверный.")
    x1,y1=rect1[0]
    x2,y2 = rect1[1]
    x3,y3=rect2[0]
    x4,y4 = rect2[1]
    x_left = max(x1,x3)
    x_right = min(x2,x4)
    y_bottom = max(y1,y3)
    y_high = min(y2,y4)

    if x_right > x_left and y_high > y_bottom:
        width = x_right - x_left
        height = y_high - y_bottom
        return width*height
    else:
        return 0

def intersectionAreaMultiRect(rects):
    if not rects:
        return 0
    for i,rect in enumerate(rects,start = 1):
        if not isCorrectRect (rect):
            raise Exception("{i} прямоугольник неправильный.")
    (x1,y1),(x2,y2) = rects[0]
    x_right = max(x1,x2)
    x_left = min(x1,x2)
    y_bottom = min(y1,y2)
    y_high = max(y1,y2)
    for rect in rects[1:]:
        (x1,y1),(x2,y2) = rect
        x_right1 = max(x1,x2)
        x_left1 = min(x1,x2)
        y_bottom1 = min(y1,y2)
        y_high1 = max(y1,y2)

        right = min(x_right,x_right1)
        left = max(x_left,x_left1)
        bottom = max(y_bottom,y_bottom1)
        high = min(y_high,y_high1)
   
        if right <= left or high <= bottom:
            return 0
        x_right = right
        x_left = left
        y_bottom = bottom
        y_high = high

        width = x_right - x_left
        height = y_high - y_bottom
        return width*height