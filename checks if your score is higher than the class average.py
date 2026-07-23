def better_than_average(class_points, your_points):
    total=0
    num=0
    for i in range (len(class_points)):
        total=total+class_points[i]
        num=num+1
        average=total/num
    if your_points>average:
        return True
    elif your_points==average:
        return False
    elif average>your_points:
        return False
