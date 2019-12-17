from collections import deque


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

records = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = records


def own_sum(items):
    head, *tail = items
    return head + own_sum(tail) if tail else head

def gen():
    print('first')
    yield 1
    print('second')
    yield 2
    print('third')
    yield 3


for el in gen():
    print(el)


def search(lines, pattern, history=5):
	previous_lines = deque(maxlen=history)
	for line in lines:
		if pattern in line:
			yield line, previous_lines
		previous_lines.append(line)


def main_search():
	with open('file.txt') as f:
		for line, prevlines in search(f, 'python', 5):
			print(f'line: {line.strip()}')
			print(f'prev: {prevlines}')


main_search()


de = deque(maxlen=3)
de.extend([1, 2, 3])
print(de)
de.append(4)
print(de)
de.appendleft(1)
print(de)
de.reverse()
print(de)
de.rotate(-3)
print(de)
de.extendleft([3, 2, 1])
print(de)

de = deque([1, 2, 3])
print(de)
de.append(4)
print(de)
de.appendleft(0)
print(de)
de.pop()
print(de)
de.popleft()
print(de)

de = deque([1, 2, 3, 3, 4, 2, 4])
# index(x, start, stop) - returns the first index of the x value, starting from start'th index till stop'th index
print(de.index(4, 2, 5))
print(de.index(4, 5))
try:
    print(de.index(4, 0, 4))
except ValueError as e:
    print(e)

# insert(index, value) - insert value to deque on specified index
print(de)
de.insert(4, 0)
print(de)

# count(x) - how many times x occurs in deque
print(de.count(3))
de.append(3)
print(de.count(3))

# remove(x) - remove first occurrence of x
de.remove(3)
print(de.count(3))

# extend(iterable) - add multiple values at the right en of deque
de.extend([1, 2, 3])
print(de)

# extendleft(iterable) - add multiple values at the left end of deque. Values are reversed
de.extendleft([1, 2, 3])
print(de)

# reverse - reverse order of deque elements
de2 = deque([1, 2, 3])
print(de2)
de2.reverse()
print(de2)

# rotate(x) - rotate the deque by x (positive-right negative-left)
de3 = deque([1, 2, 3, 4, 5, 6])
print(de3)
de3.rotate(3)
print(de3)
de3.rotate(-3)
print(de3)

import queue

Q = queue.Queue()
print(Q.full())
print(Q.empty())
Q.put(1)
Q.put(2)
Q.put(3)
print(Q.queue)
Q.get()
Q.get()
print(Q.queue)
