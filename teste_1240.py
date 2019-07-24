ncasos = int(input())

while ncasos > 0:
  a,b = list(input().split())
  if (len(a) >= len(b)):
    if a[-len(b):] == b:
      print("encaixa")
    else:
      print("não encaixa")
  else:
    print('')
  ncasos -=1
