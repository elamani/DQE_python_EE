lst = [56,78,99,35,76]
even_list = []
odd_list = []
odd_count,even_count = 0,0
for i in lst:
    if i % 2 == 0:
        even_list.append(i)
        even_count+=1
    else:
        odd_list.append(i)
        odd_count+=1
print(f'Average of even numbers : {sum(even_list)/even_count}')
print(f'Average of odd numbers : {sum(odd_list)/odd_count}')

