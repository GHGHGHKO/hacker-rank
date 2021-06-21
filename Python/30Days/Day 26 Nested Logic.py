# Enter your code here. Read input from STDIN. Print output to STDOUT

returned = list(map(int, input().rstrip().split()))
due = list(map(int, input().rstrip().split()))

hackos = 0

if returned[2] > due[2]:
    hackos = 10000
if returned[2] == due[2]:
    if returned[1] > due[1]:
        hackos = (returned[1] - due[1]) * 500
    elif returned[0] > due[0]:
        hackos = (returned[0] - due[0]) * 15
    
print(hackos)