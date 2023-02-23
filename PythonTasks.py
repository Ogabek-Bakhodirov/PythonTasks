 dict = {
     'fruit' : ['apple', 'banana', 'pineapple', 'strawberry', 'peach'], 
     'fruitPrice' : [3, 4, 3, 5, 6],
     'drink' : ['cola', 'fanta', 'sprite', 'pepsi', 'dinay'],
     'drinkPrice' : [6, 5, 7, 4, 3],
     'veg' : ['spinach', 'carrot', 'beets', 'potato', 'tomato'],
     'vegPrice' : [4, 5, 6, 3, 3]
 }
 value = ''

 def createMenu(categoryKey, indexValue, amount):
     if len(dict[categoryKey]) <= indexValue:
         print('Choosen index out of range')
     else:
         product = dict[categoryKey][indexValue]
         price = dict[f'{categoryKey}Price'][indexValue] * amount
         if categoryKey == 'drink':
             value = f'Amount of {product}: {amount} and price is ${price}'
         else:
             value = f'{amount} kg {product} is ${price}'
         print(value)
        
 createMenu('fruit', 3, 3)


