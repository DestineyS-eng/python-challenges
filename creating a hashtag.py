def generate_hashtag(s):
    words=s.title().replace(" ","")
    hashtag="#"+ words
    if len(hashtag)>140 or s==" ":
        return False
    else:
        pass
    return hashtag
        
x=generate_hashtag("hello world")
print(x)
        
