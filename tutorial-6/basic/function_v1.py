"""
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
print('Hi Fatima')
"""
#DRY
#for i in range(1_000_000):   #1000000 1_875_748 
#    print('Hi Fatima')
    
    
#metafor
#def = define  static
def print_data():
    print('Merhaba Fatima')
    
  
print_data()  
print_data()  
print_data()  

# dynamic
def print_hi(name):
    print("Merhaba " + name)
    
    
print_hi('Fatima')
print_hi('Tekin')
print_hi('Elif')


def multiple(number_1, number_2 = 7):
    print(number_1, number_2)
    
    
multiple(3, 5)
multiple(4)