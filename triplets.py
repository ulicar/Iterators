import itertools

def take(n, iterable):
  "Return first n items of the iterable as a list"
  return list(itertools.islice(iterable, n))

def consume(n, iterable):
  "Return items from iterable, starting from n"
  return list(itertools.islice(tokens, n, None))

tokens = "Isla djevojka kroz sumu kad tamo vuk iskoci na nju".split()

for step in range(len(tokens)):
    print ' '.join(take(3, consume(step, tokens)))
