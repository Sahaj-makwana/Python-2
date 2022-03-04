
N = int(input("Enter the number of Soldiers : "))
A = list(map(int, input().split()))[:N]
even,odd = 0,0
for i in A:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
if even > odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
