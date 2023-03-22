from BTrees._OOBTree import OOBTree

btrees = OOBTree()

# добовляет пару и изменяет значение у ключа
def AddDuo(key, value):
  btrees[key] = value

# выводит пару
def PrintTree():
  if len(btrees) == 0:
    print("Дерева нет!")
  else: 
    for pair in btrees.iteritems(): 
      print (pair)

# вывод значения из ключа
def GetValue(key):
  if key in btrees:
    print(key, " => " ,btrees[key])
  else:
    print("нет такого ключа")

# очищает дерево
def DoVoidTree():
  for i in list(btrees.keys()):
    del btrees[i] 
  print("Дерево стерто")