#!/usr/bin/env python
# -- coding: utf-8 -- 

idade = int(input())
ano = int(idade/365)
mes = int((idade-(ano*365))/30)
dias = (idade-(ano*365))-(mes*30)
print('{} ano(s) '.format(ano))
print('{} mes(es) '.format(mes))
print('{} dia(s) '.format(dias))

