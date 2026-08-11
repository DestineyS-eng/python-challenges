def get_grade(s1, s2, s3):
    grade=(s1+s2+s3)//3
    if 0<=grade<60:
        return "F"
    elif 60<=grade<70:
        return "D"
    if 70<=grade<80:
        return "C"
    if 80<=grade<90:
        return "B"
    if 90<=grade<=100:
        return "A"
