#Bubble Sorting

# list = [7,1,9,4,3]
# swap = 0
# swapped = False

# while swapped == False:
#     for i in range(len(list)-1):
#         if list[i] > list[i+1]:
#             temp = list[i]
#             list[i] = list[i+1] 
#             list[i+1] = temp
#             swap += 1
#     if swap > 0:
#         swap = 0
    
#     else:
#         swapped = True
# print("The new list order is:",list)

#Insertion Sorting

# list = [8,7,1,9,4]

# for i in range(1,len(list)):
#     temp = list[i]
#     j = i-1
#     while j >= 0 and temp < list[j]:
#         list[j+1] = list[j]
#         j -= 1
#     list[j+1] = temp
# print("The new list order is:",list)
