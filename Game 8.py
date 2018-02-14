T=1
print("Welcome..")
while T==1 :
     print ("Choose Game Mode")
     print ("1)one Player      2)two Players ")
     m=int(input())
     if m==1:
          p=input("Enter Your Name,Please: ")
          n= int(input ("Enter the number of coins,Please: "))
          if n<=1:
               print ("unavailable number!!")
               continue
          c=n/2
          f=n
          while n>0:
               print("Enter Num of coins you take,",p," : ")
               i=int(input ())
               if (i==f or i > n or i<=0 or i>(2*c)):
                 print ("unavailable number!!")
                 continue
               else :
                    n=n-i
                    print ("coins= ",n)
                    if n==0 :
                         print("The winner is: ",p)
                         break
                         
                    c=n
                    while c<=n:
                         if n==3:
                              n=n-1
                              print("Computer has taken ",1," coin")
                              print ("Coins= ",n)
                              break
                         elif ((n-c)-(2*c)>0 and c<=(2*i))or n==2 or n==1:
                              n=n-c
                              print("Computer has taken ",c," coins")
                              print ("Coins= ",n)
                              if n==0 :
                                   print("You lose..Try again")
                              break
                         c=c-1
          print("Do You want to play again? ")
          print ("1)YES          2)NO")
          o=int(input())
          if (o==2):
               T=0
               print("Good Bye")
                         
     if m==2:     
          p1=input("Enter The first player's Name: ")
          p2=input("Enter The second player's Name: ")
          n= int(input ("Enter the number of coins,Please: "))
          z=n-1
          a=3
          if n<=1 :
               print ("unavailable number!!")
               continue 
          while n > 0 :
               y=a%2
               if y==1 :
                    x=p1
               else :
                    x=p2
               print("Enter Num of coins you take,",x," : ")
               i=int(input ())
               if i > z or i<=0 or n-i<0:
                    print ("unavailable number!!")
                    continue
               else :
                    n=n-i
                    print ("coins= ",n)
                    z=i*2
                    a=a+1
          print ("The winner is: ",x)
          print("Do You want to play again? ")
          print ("1)YES          2)NO")
          j=int(input())
          if (j==2):
               T=0
               print("Good Bye")









          
          
