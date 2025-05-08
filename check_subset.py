t = int(input())
for i in range(t):

  n = int(input())

  #Input n integers like: 1 2 3 4 5....
  a = set(map(int,input().split()))

  n = int(input())
  b = set(map(int,input().split()))
  ans = a.issubset(b)
  print(ans)