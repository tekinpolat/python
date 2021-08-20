#DRY(Dont Repeat YourSelf)

#odd = tek
#iterable

#list.append(item)
numbers = [21, 35, 34, 56, 58, 71]     # [21,35,71]
odd_numbers = []
for number in numbers:
    #print(number)
    if number % 2 == 1:       # 21 %2 = 1 == 1  => True  34 % 2 = 0 == 1 => False
        #print(number)
        odd_numbers.append(number)
        
        

#odd use
print(odd_numbers)



numbers = [22, 65, 76, 56, 58, 71]     # [21,35,71]
odd_numbers = []
for number in numbers:
    #print(number)
    if number % 2 == 1:       # 21 %2 = 1 == 1  => True  34 % 2 = 0 == 1 => False
        #print(number)
        odd_numbers.append(number)
        
#odd use
print(odd_numbers)




numbers = [67, 98, 76, 98, 58, 71]     # [21,35,71]
odd_numbers = []
for number in numbers:
    #print(number)
    if number % 2 == 1:       # 21 %2 = 1 == 1  => True  34 % 2 = 0 == 1 => False
        #print(number)
        odd_numbers.append(number)
        
#odd use
print(odd_numbers)

























print(type(odd_numbers))

name = 'Tekin'          #string
print(type(name))

print(dir([]))
print(dir(name))



#scrapy 
#requests