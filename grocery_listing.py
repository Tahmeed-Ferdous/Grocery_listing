print('--------Welcome to grocery list price calculator------')
print("""
 |----------------|
 |  Happy Listing |
 |                |
 |       O        |
 |      /|\\/      |
 |     / |        |
 |      / \\       |
 |     /   \\      |
 |                |
 |----------------|
""")
print('-----Try to keep the budget amount as high as possible-----')
dic={}
dic2={}

def store():#function to store the values
  total_amount_needed=0
  items=0
  budget=int(input('Enter your budget:----- TK'))
  budget_must_be_above_0=budget

  while budget_must_be_above_0>0:#while loop used to give only one condition
    product=input('Enter the name of product(type stop to end the listing):----- ').lower()
    if product == 'stop':
      break
    else:
      quantity=float(input('Enter the quantity of product:----- '))
      price=int(input('Enter the price of product:------ '))
      multiply=quantity*price
      dic[product]=multiply#update in the dictionary
      dic2[product]=quantity
      budget_must_be_above_0=budget-dic[product]

      for _ in product: #for loop used to iterate the product variable
        items+=1
        budget-=multiply
        if budget<0:# if else condition for less than zero
          print(f'Extra amount:------ {int(budget)}')
          
        else:
          print(f'Budget remaining:------ {int(budget)}TK')#formating
        break
      
    for product in dic:
      print(f"\--------{dic2[product]}--{product}=={int(dic[product])}TK---------/")

  print('----------------------------------------------')
  print('-------------------list-----------------------')
  print('----------------------------------------------')

  print('''|--------No._______Name_______price---------|''')
  for product in dic:
    print(f"""|--------{dic2[product]}_______{product}_______{int(dic[product])}TK---------|""")
  
  for values in dic.values():
    total_amount_needed+=values 
  
  print('----------------------------------------------')
  print('--------------------Sum-----------------------')

  print(f'Total budget:------ {int(total_amount_needed+budget)}TK')  
  print(f'Total cost:-------- {int(total_amount_needed)}TK')
  print(f'Extra money:------- {int(budget)}TK')#to remove minus sign
  print(f'Total items:------- {items} items')

def run_again():#run the whole process as much as possible
    storage = store()
    while input("Want to increase budget?(yes/no)------- ") == "yes":
      storage = store()
        
run_again()
