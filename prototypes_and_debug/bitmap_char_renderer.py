#Créé le 13 Juin 2024
from kandinsky import fill_rect as fr

bin_a="01110;00001;01111;10001;10001;11111"
hex_a="5;0E010F11111F"
hex_sr="7;030202040404642C181808"
hex_b="6;2020202E312121322C"
hex_Q="7;1C2241414141221C080C"

hex_val=["A","B","C","D","E","F"]
dec_val=[10,11,12,13,14,15]
def hex_to_bin(hex_num):
 global final_bin
 dec_num,bin_buffer=0,[]
 for string in reversed(hex_num):
  for i in range(6):string=dec_val[i]if string==hex_val[i]else string
  dec_num+=int(string)
  buffer=[]
  while dec_num!=0:
   buffer.append(str(dec_num%2))
   dec_num=dec_num//2
  if len(buffer)<4:
    for _ in range(4-len(buffer)):buffer.append('0')
  bin_num=""
  for string in reversed(buffer):
   bin_num+=string
  bin_buffer.append(bin_num)
 bin_num=""
 for string in reversed(bin_buffer):
  bin_num+=string
 bin_buffer=""
 for n,string in enumerate(reversed(bin_num)):
  if n<len_num:bin_buffer+=string
 bin_num=""
 for string in reversed(bin_buffer):
  bin_num+=string
 final_bin+=bin_num+";"

def decode_hex(char):
 global len_num,final_bin
 n,hex_num,len_num,final_bin=0,"",0,""
 for string in char:
  if n==0:len_num+=int(string);n+=1;continue
  if n==1:n+=1;continue
  hex_num+=string
  n+=1
  if n==4:hex_to_bin(hex_num);n,hex_num=2,""
 char=final_bin
 return char

def decode_bin(char):
 rows=char.split(';')
 return[[int(c)for c in row]for row in rows]

def decode_char(char):
  char=decode_hex(char)
  char=decode_bin(char)
  return char

def draw(xf,yf,letter):
 lst=decode_char(letter)
 for ay in range(len(lst)):
  for ax in range(len(lst[ay])):
   if lst[ay][ax]==1:fr(xf+ax,yf+ay,1,1,(0,)*3)

draw(160,111,hex_Q)
