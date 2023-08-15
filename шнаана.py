# b = "qwertq kokokky zqszbdujchtr p[pl,lmmn"
# a = "wer"
# c = "q"
#
#
# def search_substring(subst, st):
# 	res = st.find(subst)
# 	if res == -1:
# 		print("МИМО")
# 	else:
# 		print("Есть контакт")
#
#
# search_substring(a, b)
#
#
# def first_last(letter, st):
#
# 	first = st.find(letter)
# 	second = st.rfind(letter)
# 	if first == -1:
# 		return None, None
# 	else:
# 		return first, second
#
#
# print(first_last(c, b))
#
#
# def top_3(st):
#
# 	for i in st:
# 		if ord(i) != 32 and i not in s:
# 		s = {i: st.count(i) for k in st}
# 	print(s)
#
#
# print(top_3(b))
# s = {i: b.count(i) for i in b if ord(i) != 32}
# res = sorted(s.items(), key=lambda x: x[1], reverse=True)
# x = res[0:3]
# for i in x:
# 	print(f"{i[0]}-{i[1]}")

