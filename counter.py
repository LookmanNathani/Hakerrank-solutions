from collections import Counter

n,l = int(input()),list(map(int,input().split()))
available = Counter(l).items()
print(available)
cust = int(input())
cust_info = {}
amount = 0
for i in range(cust):
    a,b = input().split()
    cust_info[a] = b
print(customer_info)

