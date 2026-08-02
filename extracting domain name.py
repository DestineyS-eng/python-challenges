def domain_name(url):
    #where the domain will be kept
    domain=""
    #removes anything that comes before the domain name 
    url=url.replace("http://","").replace("https","").replace("http","").replace(":","").replace("//","").replace("/","").replace("www.","").replace("https://","")
    #will look through the list if there is a dot it will split it via the do and take the frist item
    for i in range (len(url)):
        if url[i]==".":
            domain=url.split(".")[0]
    return domain
        
        
x= domain_name("https://www.programiz.com/python-programming/online-compiler/")
print(x)
