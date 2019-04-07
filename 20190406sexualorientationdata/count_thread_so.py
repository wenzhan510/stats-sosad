import csv
with open('threads-sexual-orientation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    count_so = [0,0,0,0,0,0,0,0]
    for row in csv_reader:
        if line_count != 0:
            thread_id = int(row[0])
            so = int(row[1])
            count_so[so] += 1                   
        line_count +=1
    print(f'processed {line_count} lines.')
    print(f'count_so {count_so}')
