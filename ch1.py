from collections import deque


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

