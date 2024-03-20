d = {'dog': 'woof', 'cat': 'meow'}
del d['cat']
if 'dog' in d: print(d['dog'])

for k, v in d.items(): print(k, 'says', v)
