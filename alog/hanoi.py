def move(n,f,m,t):
    if(n==1):
       print("{0}:{1}-->{2}".format(n,f,t))
    else: 
        move(n-1,f,t,m)
        print("{0}:{1}-->{2}".format(n,f,t))
        move(n-1,m,f,t)
    
move(3,'a','b','c')









                

                
