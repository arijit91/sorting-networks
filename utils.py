import sys

def inversionCount(input_list):
  inv = 0
  for i in range(0,len(input_list)):
    for j in range(i+1,len(input_list)):
      if input_list[i]>input_list[j]:
        inv += 1
  return inv
