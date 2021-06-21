phone_Book = {}
input_Names = []

people = int(input())

for insert_Phonebook in range(0, people):
    arr_Name = list(map(str, input().rstrip().split()))
    phone_Book[arr_Name[0]] = arr_Name[1]
    
for _ in range(0, people):
    input_Names.append(str(input()))

for output_Name in input_Names:
    if output_Name in phone_Book:
        print(output_Name + '=' + str(phone_Book[output_Name]))
    else:
        print('Not found')
