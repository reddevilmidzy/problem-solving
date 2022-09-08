alpah = input()
alp_list = ["A", "B", "C", "D", "E", "F","G","H", "I", "J", "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
alp_count = []
for i in range(26):
     alpah = alpah.upper()
     alp_count.append(alpah.count(alp_list[i]))
# print(alp_count)
fine_max = ((max(alp_count)))
# print(fine_max)
# print(alp_count)
if alp_count.count(fine_max) > 1:
     print("?")
else:
# print(alp_count.count(fine_max))
     fine = (alp_count.index(fine_max))
     print(alp_list[fine])
# print(fine)
