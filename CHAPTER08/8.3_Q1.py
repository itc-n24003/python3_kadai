import collections
data = 'すもももももももものうち'
cout = collections.Counter(data)
res_dict = collections.defaultdict(list)
for ch, cnt in cout.items():
    res_dict[cnt].append(ch)
print(res_dict[1])
