#Challenge 1

def sum_to(n):
  #start at 1
  #then add 2 then add 3 and so forth until you hit n
  # sum = 0
  # i = 0
  # while i <= n:
  #   sum = sum + i
  #   i+=1
  #   return sum
  return n * (n + 1) // 2

# print(sum_to(6))
# print(sum_to(10))

#Challenge 2

def largest(list):
  #iterate through the array to find the largest value
  #return max(list)
  #first set the first element in the array to the largest number
    # largest = list[0]
    # for n in list:
    #   if n > largest:
    #     largest = n
    # return largest
    #then compare it with every number in the array
      #if the numbert in the array is greater than largest
      #set largest equal to that number

      #indentation is tricky

    list.sort()
    return list[-1]

#print(largest([1, 2, 3, 4, 0]))
#print(largest([10, 4, 2, 231, 91, 54])

#Challenge 3

def occurrences(str1, str2):
  # count method
  return str1.count(str2)

# print(occurrences('fleep floop', 'e'))
# print(occurrences('fleep floop', 'p'))
# print(occurrences('fleep floop', 'ee'))
# print(occurrences('fleep floop', 'fe'))

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  return product

# print(product(-1, 4))
# print(product(2, 5, 5))
# print(product(4, 0.5, 5))