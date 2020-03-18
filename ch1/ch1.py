class UnpackingaSequenceintoSeparateValues:

    def unpacking1(self):
        line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
        uname, *fields, homedir, sh = line.split(':')
        print(uname, fields, homedir, sh)

    def unpacking2(self):
        records = ('ACME', 50, 123.45, (12, 18, 2012))
        name, *_, (*_, year) = records
        print(name, year)

    def own_sum(self, items):
        head, *tail = items
        return head + self.own_sum(tail) if tail else head


class Generators:

    def __init__(self):
        for el in self.gen():
            print(el)

    def gen(self):
        print('first')
        yield 1
        print('second')
        yield 2
        print('third')
        yield 3


from collections import deque


class DequeTest:
    def deque1(self):
        de = deque()  # empty
        de.append(1)  # add to the right end
        de.appendleft(0)  # add to the left end
        de.pop()  # remove right end element (return deleted element)
        de.popleft()  # remove left end element (return deleted element)
        print(de)  # empty

    def deque2(self):
        de = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6])
        de.index(2, 0, 2)  # el, beg, end - returns the first index of the value
        de.insert(0, 99)  # insert value (99) in index (0)
        de.remove(9)  # remove first occurrence of value (9)
        de.count(6)  #


from collections import defaultdict
# It automatically initializes the first value
# so you can simply focus on adding items.
# It will automatically create dictionary entries for keys accessed later on
# (even if they aren’t currently found in the dictionary).


class DefaultDict:
    def defdict(self):
        d = defaultdict(list)
        d['a'].append(1)
        d['a'].append(2)
        d['b'].append(1)
        print(d)

    def defdict2(self):
        d = defaultdict(set)
        d['a'].add(1)
        d['a'].add(2)
        d['b'].add(1)
        print(d)

    def setdef(self):
        d = {}
        d.setdefault('a', []).append(1)
        d.setdefault('a', []).append(2)
        d.setdefault('b', []).append(1)
        print(d)


from collections import OrderedDict
import json
# To  control  the  order  of  items  in  a  dictionary,
# you  can  use  an OrderedDict

# Be aware that the size of an OrderedDict
# is more than twice as large as a normal dictionary
# due to the extra linked list that’s created.


class DefaultDictTest:
    def orddict(self):
        d = OrderedDict()
        d['a'] = 2
        d['b'] = 1
        d['c'] = 3
        print(d.items())  # should be a: 2 b: 1 c: 3

    def orddictjson(self):
        # may be useful is we need to serialize or deserialize to json and have
        # specific order
        d = OrderedDict()
        d['a'] = 2
        d['b'] = 1
        d['c'] = 3
        print(json.dumps(d))


class CalculatingWithDict:
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    def minmaxsort(self):
        # will return tuple of value and name
        reverse_dict = zip(self.prices.values(), self.prices.keys())
        min_price = min(reverse_dict)
        max_price = max(reverse_dict)
        sorted_price = sorted(reverse_dict)

    def minanother(self):
        min(self.prices, key=lambda k: self.prices[k])  # will return FB
        min_price = self.prices[min(self.prices, key=lambda k: self.prices[k])]


def find_commonalities():
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    print(a.keys() & b.keys())


find_commonalities()
