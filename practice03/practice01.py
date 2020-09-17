from random import randrange

subs = ['I', 'You']
verbs = ['Play', 'Love']
objs = ['Hockey', 'Football']

r = randrange(2)
a = [i.pop(r) for i in (subs, verbs, objs)]
print(a)
