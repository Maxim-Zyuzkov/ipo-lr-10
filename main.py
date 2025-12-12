from collision import isCorrectRect
from collision import isCollisionRect
from collision import intersectionAreaRect
from collision import intersectionAreaMultiRect

print("isCorrectRect([(-3.4, 1), (9.2, 10)]):", isCorrectRect([(-3.4, 1), (9.2, 10)])) 
print()
print("isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]):", isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))
print()
print("intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])", intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)]))
print()
print("intersectionAreaMultiRect([(-3, 1), (9, 10)], [(3, 17), (13, 1)]):",intersectionAreaMultiRect([[(-3, 1), (9, 10)], [(3, 17), (13, 1)]]))