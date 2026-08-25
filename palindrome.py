def is_palindrome(s):
    #lowered the letters so its all the same case
    s=s.lower()
    #if backwards is equal to the normal version ruturn true 
    if s[::-1]== s:
        return True
    return False
