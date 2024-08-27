# # from collections import Counter
s = "ballair"#input()
# # print(Counter(s))
# s = "Ballari"
d = {}
# i = 0
# for i in range(0,len(s)):
#     d[s[i]] = s.count(s[i])
# print(d)
"""give the occarances of each character in a given string without repitation of same character.
ex:input:ballari
output: b:1
        a:2
        l:2
        r:1
        i:1  """
for i in range(0,len(s)):
    d[s[i]] = 1
    for j in range(i,len(s)):
        if s[i] == s[j]:
            d[s[i]] += 1
print(d)
