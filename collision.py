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