import sys
import os

def inversionCount(input_list):
  inv = 0
  for i in range(0,len(input_list)):
    for j in range(i+1,len(input_list)):
      if input_list[i]>input_list[j]:
        inv += 1
  return inv

def inversionCountFast(input_list):
  file_name = 'tmp_list'
  out_file = 'tmp_out'
  f = open(file_name, 'w')
  f.write(str(len(input_list))+'\n')
  for elem in input_list:
    f.write(str(elem)+'\n')
  f.close()
  os.popen("./inversion < " + file_name + " > " + out_file)
  
  f = open(out_file, 'r')
  val = int(f.readline())
  f.close()
  return val
