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