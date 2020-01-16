digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#indexing-------------->
print(digits[-1])
print(digits[-len(digits)])

#Slicing------------->
print(digits[:3])

print(digits[0: 7])# 7 got excluded whereas 0 was included

print(digits[0:-1])#notice how 9 was excluded

#Striding--------------->
print(digits[0:10: 2])

print(digits[::2])

print(digits[::-2])

print(digits[::-1])

print(digits[5:0:-2])


for i in range(len(digits)):
  print(digits[0:i])

for i in range(len(digits)):
  print(digits[i:i+3])

#Or
window_length = 3
for i in range (len(digits)-(window_length-1)):
  print(digits[i:i+window_length])



