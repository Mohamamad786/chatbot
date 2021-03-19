# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  if drink_type == 'latte':
    drink_type = order_latte()
  print(f'Alright, that\s a {size} {drink_type}!')
  name  = get_name()
  print(f'Thanks, {name}! Your drink will be ready shortly.')

# Get Size
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

# Print Message for Wrong Input
def print_message():
  print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')

# Get Drink type
def get_drink_type():
    res = input('What type of drink can I get for you? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
    if res == 'a':
      return 'brewed coffee'
    elif res == 'b':
      return 'mocha'
    elif res == 'c':
      return 'latte'
    else:
      print_message()
      return get_drink_type() 

# Latter Options
def order_latte():
  res = input('And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ')
  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte() 

# Get Name:
def get_name():
    res = input('Can I get your name please?')
    return res


# Call coffee_bot()!
coffee_bot()

