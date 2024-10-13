# Set: immutable but elements can be added or removed
# Do not allow duplicates
# Not indexed
mySet = {'apple','pear','peach',1, 2.0}

# Tuple: immutable and Indexed
# Do not allow any change to elements
myTuple= ('apple','pear','peach', 1, False)

# my_list = ['pear','orange','pineapple','apple','peach','kiwi','banana'] 
# my_other_list = my_list[1:5]
# my_other_list.sort()
# print(my_other_list)

# while myNum > 0:
#     myNum = myNum - 1
#     print(myNum)
# print("Blastoff")

# myNumber = -4
# while myNumber < 0:
#   myNumber +=1
#   if myNumber == 0:
#     print(0)
#     continue
#   print('T'+ str(myNumber))
# print('Blastoff!')


# dict = {'alpha':1, 'beta':2, 'gamma':3}
# for key in dict:
#   print(key,dict[key])

# multiples = []
# for outer in range(1,3):
#   multiples.append([])
#   for inner in range(1,2): 
#     multiples[outer-1].append(inner) 
# print(multiples)


# import math
# def dB(V1, V2):
#   return 20 * math.log10(V1/V2), V1, V2 
# calc_dB = dB(10,5)

# print(calc_dB)

# q = 1
# def outer1(i):
#     j = i + 1
#     def outer2():
#         k = j + 1
#         def inner1():
#             m = k + 1
#             def inner2():
#                 n = q + m + 1
#                 return n
#             m = inner2()
#             return m
#         k = inner1()
#         return k
#     j = outer2()
#     return j

# print ("outer1(1) =", outer1(1))

# my_list = [[9, 8], [7, 6], [5, 4], [3, 2]]
# my_list[1].sort()
# print(my_list)

# import math
# def dB2(param1, param2):
#  dB_calc = 20 * math.log10(param1/param2)
#  print(dB_calc)
#  if dB_calc > 6:
#   return "High SNR"
#  elif dB_calc > 0:
#   return "Low SNR"
#  return "Noise"
  
# print(dB2(7,5))

# multiples = []
# for threeD in range(1,3):
#  multiples.append([])
#  for twoD in range(1,3):
#   multiples[threeD-1].append([])
#   for oneD in range(1,3):
#    multiples[threeD-1][twoD-1].append(twoD)
# print(multiples)

# def outer1(i):
#  j = i + 1
#  def outer2():
#   k = j + 1
#   def inner1():
#    m = k + 1
#    def inner2():
#     n = q + m + 1
#     return n
#    m = inner2()
#    return m
#   k = inner1()
#   return k
#  j = outer2()
#  return j

# q = 1 
# print ("outer1(1) = ", outer1(1))


# def recursive_3(num):
#  if num == 1:
#   return 12
#  return recursive_3(num - 1) -5
# print('rec_3 ',recursive_3(5))

my_first_list = ['a', 'b', 'c']
my_second_list = ['d', 'e', 'f', 'g']
my_third_list = my_second_list[0:1] + my_first_list[1:2]
my_third_list.append('h')
print (my_third_list)