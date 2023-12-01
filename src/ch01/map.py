full_name_list = [['first_name', 'Man'], ['middle_name', 'Sinh'], ['last_name', 'Lee']]
print(f"lists in list: {full_name_list}")

full_name_dict = dict(full_name_list)
print(f"dict: {full_name_dict}")

map = full_name_dict

if 'salary' in map:
    print(map['salary'])
else:
    print('salary not found')

map.get('salary', 'Salary is hidden')