import csv
data_dict={}

with open("proceed.csv", 'r', encoding='UTF-8-SIG') as csvfile:
    # reader = csv.reader(csvfile.decode('UTF-8-SIG'))
    # print(chardet.detect(csvfile.read()))
    # print(csvfile.read())
    csv_reader = csv.reader(csvfile)

    for index, row in enumerate(csv_reader):
        # values_dict={'2015':row[1], '2016':row[2]}
        tool_dict={
            row[0]:{
                '2015':row[1],
                '2016':row[2],
                '2017':row[3],
                '2018':row[4],
                '2019':row[5],
            }
        }
        if index != 0:
            data_dict = {**data_dict, **tool_dict} #** let's you add dictionaries



for key, value in data_dict.items():
    sum=(int(value['2015']) + int(value['2016']) + int(value['2017']) + int(value['2018']) + int(value['2019']))
    value['sum']=sum
    print(key, "2015:", value['2015'], " 2019:", value['2019'], " sum:", value['sum'])

def call(keys):
    print(keys, data_dict[keys])
print('type a tool name below:')
call(input(''))
