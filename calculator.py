#A project to calculate the area of ​​the room and give the amount for the cost of the work
length=input('Please type length :\n')
width= input('Please type width :\n')
# i need to change from string to float 
float_length=float(length)
float_width=float(width)
money = input ('How much for 1 meter ? \n')
float_money = float(money)
area= (float_length*float_width*2)
# i need to change from float to  string
str_area=str(area)
print('The total are is :'+str_area )
budget=(float_money*area)
str_budget=str(budget)
print('Give the guy : $'+str_budget)




# كود لطباعه النسخ
p=input('Type the text you want to copy :\n ')
s=input ('How many copies? ?\n')
s_int=int(s)
for x in range(s_int):
    print (p)
print (' Counting begins with the number zero')    
