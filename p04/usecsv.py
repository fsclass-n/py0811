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

# 숫자 데이터만 뽑아 콤마(,) 제거
def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(j.replace(',', ''))
            except:
                pass
    return listName