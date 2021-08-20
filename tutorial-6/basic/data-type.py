""" 
name
surname
age
"""

# CamelCase    (java)
# snake_case   (python)
# PascalCase   (c#)

name    = 'Fatima'      # string
surname = 'Rzayeva'     # string
age     = 25            #int


my_info = ['Fatima', 'Rzayeva', 25]  #list
#my_info[0] = 'Tekin'

my_info = ('Fatima', 'Rzayeva', 25)  #tuple


#tuple vs list

my_info = {'name': 'Fatima', 'surname': 'Rzayeva', 'age': 25}   #dict


name_1    = 'Fatima'      # string
surname_1 = 'Rzayeva'     # string
age_1     = 25            #int


name_2    = 'Tekin'      # string
surname_2 = 'POLAT'     # string
age_2     = 25            #int


name_3    = 'Ali'      # string
surname_3 = 'ELİF'     # string
age_3     = 30            #int


#company_employees = [ 'Fatima','Tekin', 'Ali', 'Rzayeva', 'POLAT', 'ELİF', 25, 25, 30]

company_names       = ['Fatima','Tekin', 'Ali']
company_surnames    = ['Rzayeva', 'POLAT', 'ELİF']
company_ages        = [25, 25, 30]


company_names       = ('Fatima','Tekin', 'Ali')
company_surnames    = ('Rzayeva', 'POLAT', 'ELİF')
company_ages        = (25, 25, 30)

company_employees = [
    ['Fatima', 'Rzayeva', 25],
    ['Tekin', 'POLAT', 25],
    ['Ali', 'ELİF', 30],
]


company_employees = [
    {'name': 'Fatima', 'surname': 'Rzayeva', 'age': 25},
    {'name': 'Tekin', 'surname': 'POLAT', 'age': 25},
    {'name': 'Ali', 'surname': 'ELİF', 'age': 30},
]