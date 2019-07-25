ncasos = int(input())
while ncasos >=0:
  n = int(input())
  if n >= 0:
    if n%2 == 0:
      div = n/2
    else:
      div = n/3
    print('{:.0f}'.format(div))
  else:
      print('')
  ncasos -=1

