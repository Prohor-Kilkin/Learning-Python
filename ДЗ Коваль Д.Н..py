lst = [
	{'name': 'Jennifer', 'final': '95'},
	{'name': 'David', 'final': '92'},
	{'name': 'Nikolas', 'final': '98'}
]

res = sorted(lst, key=lambda x: x['name'])
print(res)

res = sorted(lst, key=lambda x: x['final'], reverse=True)
print(res)

# --------------------------------------------------------------------------------------------

nums = [5, 8, 4, 3, 6, 8, 9, 7]
s = []
c = []
a = list(map(lambda i, j: (i ** 2, j ** 3), nums, nums))
for n in range(len(a)):
	s.append(a[n][0])
	c.append(a[n][1])

print(s)
print(c)






