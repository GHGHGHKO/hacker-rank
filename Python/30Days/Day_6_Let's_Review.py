# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
text = []

for T in range(t):
    s = str(input())
    text.append(s)

for S in text:
    print (S[::2], S[1::2])