aliens = []
#创建30个外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['points'] = 15
        alien['speed'] = 'fast'
        alien['color'] = 'red'
# 显示前五个外星人
for alien in aliens[0:6]:
    print(alien)



pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + " -crust pizza" + "with the following topping:")

for topping in pizza['topping']:
    print("\t" + 'topping')


