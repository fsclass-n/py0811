import csv

# csv 파일 읽기
def opencsv(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        output = []
        for i in reader:
            output.append(i)
        return output

# csv 파일 쓰기
def writecsv(filename, the_list):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        a = csv.writer(f, delimiter=',')
        a.writerows(the_list)