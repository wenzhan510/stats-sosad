import csv
with open('summarized_sexual_orientation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    user_so = []
    line_count = 0
    for row in csv_reader:
        if line_count >1:
            user_so.append(list(map(int, row)))                    
        line_count +=1
    print(f'processed {line_count} lines.')

total_user = 0
total_user_collect_over3 = 0 # 收藏数大于等于3本的人

collection_count = [0,0,0,0,0,0,0,0,0,0,0]

so_only = [0,0,0,0,0,0,0,0] # 只收藏这种性向的人
so_only_over3 = [0,0,0,0,0,0,0,0] # 只收藏这种性向，且收藏数大于等于三本

so_include = [0,0,0,0,0,0,0,0] # 收藏了这种性向的人
so_include_over3 = [0,0,0,0,0,0,0,0] # 收藏了这种性向，且总收藏书大于等于3本

accepted_so_count = [0,0,0,0,0,0,0,0] # 能够收藏的性向种类数字，比如【1】说明只收藏一种性向的
accepted_so_count_over3 = [0,0,0,0,0,0,0,0] # 能够收藏的性向种类数字，比如【1】说明只收藏一种性向的, 且收藏总数大于等于3本

for count_so in user_so: 
    accepted = 0
    total_books = 0
    for x in range(0,8):
        if count_so[x]>0:
            accepted += 1
            total_books += count_so[x]

    for y in range(0, 10):
        if total_books == y:
            collection_count[y] += 1
    if total_books > 9:
            collection_count[10] += 1    

    accepted_so_count[accepted] += 1
    if total_books >0:
        total_user += 1
    if total_books >=3:
        accepted_so_count_over3[accepted] += 1
        total_user_collect_over3 += 1
    for x in range(0,8):
        if count_so[x]>0 and total_books -count_so[x] == 0:
            so_only[x] += 1
            if total_books >=3:
                so_only_over3[x] += 1

        if count_so[x]>0:
            so_include[x] += 1
            if total_books >=3:
                so_include_over3[x] += 1

print(f'total_user {total_user}')
print(f'total_user_over3 {total_user_collect_over3}')
print(f'collection_count {collection_count}')
print(f'so_only {so_only}')
print(f'so_only_over3 {so_only_over3}')
print(f'so_include {so_include}')
print(f'so_include_over3 {so_include_over3}')
print(f'accepted_so_count {accepted_so_count}')
print(f'accepted_so_count_over3 {accepted_so_count_over3}')
