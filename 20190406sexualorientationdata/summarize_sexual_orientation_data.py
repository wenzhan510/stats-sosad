import csv
with open('sexual_orientation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    last_user = 0
    present_user = 0
    user_so = []
    count_so = [0,0,0,0,0,0,0,0,0]
    for row in csv_reader:
         # print(f'column names are{", ".join(row)}')
        if line_count != 0:
            present_user = int(row[0])
            so = int(row[2])
            if last_user == present_user:
                count_so[so] +=1       
            else:
                user_so.append(count_so)
                # print(f'\t user_id {last_user}, whose sexual_orientation is {count_so}.')
                count_so = [0,0,0,0,0,0,0,0,present_user]
                count_so[so] +=1  
                last_user = present_user                    
        line_count +=1
    print(f'processed {line_count} lines.')

with open('summarized_sexual_orientation.csv', mode='w') as summary_file:
    summary_writer = csv.writer(summary_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    summary_writer.writerow(['unknown','bl','gl','bg','gb','mix_so','no_cp','other_so','user_id'])
    for count_so in user_so: summary_writer.writerow(count_so)

