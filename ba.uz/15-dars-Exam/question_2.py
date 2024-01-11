# 2. N ta son berilgan. Ular ichda 2 ta nol mavjud. Shu 2 ta nol orasida joylashgan elementlar yig'indisini toping
n = int(input())
lst = [int(input()) for i in range(n)]
ind_l = lst.index(0)
ind_r = lst.index(0, -1)
print(ind_l, ind_r)
print(sum(lst[ind_l:ind_r]))
