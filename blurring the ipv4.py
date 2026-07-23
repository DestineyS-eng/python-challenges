def sanitize_log(log_string):
    final=log_string
    singles=log_string.split()
#splits each word by its space 
    for i in range (len(singles)):
       part=singles[i].split(".")
#splits what its on by its dots 
       if len(part)==4:
#if its  4 length it is IPv4
           part[1]="xxx"
           part[2]="xxx"
#we are replacing the middle numbers with three x's
           k=".".join(part)
#we are joining the ipv4 via its .
           final=log_string.replace(singles[i],k)
# replace the inital ipv4 with its new blurred one within its sentence 
           
    return final
x=sanitize_log("Alert from 10.0.0.1 on port 80")
print(x)
