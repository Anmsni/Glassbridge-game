import random

rownum = 0
sides = 0
glassbridge = []
for i in range(10):
  sides = random.randint(1, 2)
  if sides == 1:
    glassbridge.append('left')
  else:
    glassbridge.append('right')

#print(glassbridge)
empty = []
glassbroken = 0
players = random.randint(1, 5)

while True:
  print("row:", rownum, "🪟 🪟")
  choice = input('LEFT OR RIGHT: ').lower()
  if choice == glassbridge[rownum]:
    print('Correct...🔫')
    rownum = rownum + 1
    empty.append(choice)
    print(empty)
  else:
    print('----------------')
    print('restarting...')
    print('----------------')
    print('DEATHHHHHHH 🔫🔫🔫🔫🔫🔫🔫 🥀🥀🥀')
    print('You fell... 🥀, victim to broken glass...')
    players = players - 1
    glassbroken = glassbroken + 1
    rownum = 0
  if rownum == 10:
    print('🎉 Game Passed🎉')
    break
  elif players <= 0:
    print('DEATHHHHHHH 🔫🔫🔫🔫🔫🔫🔫 🥀🥀🥀')
    print('You got no more lives left...')
    break
  print('There are', players, "players left.")
  print('There are', glassbroken, 'glass(es) broken')
  
