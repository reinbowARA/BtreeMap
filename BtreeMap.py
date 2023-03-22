from BTrees._OOBTree import OOBTree

btrees = OOBTree()

def AddDuo(key, value):
  btrees[key] = value

def PrintTree():
  for pair in btrees.iteritems(): 
    print (pair)