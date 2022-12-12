import csv, sys

def select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='C:/Users/maxic/project_N/algorithms/documents/all_stocks_5yr.csv'):
    count = 0
    with open(filename, 'r', encoding='utf-8') as file_csv:
        csv_read = csv.DictReader(file_csv)
        sort_csv = sorted(csv_read, key=lambda x: x['date'], reverse=True)
        
        for _sort in sort_csv:
            if count != limit:
                count += 1
                print(f"{_sort['date']} | {_sort['open']} | {_sort['high']} | {_sort['low']} | {_sort['close']} | {_sort['volume']} | {_sort['Name']}")
    
    return sort_csv


def get_by_date(date="2017-08-08", name="PCLN", filename='dump.csv'):
    PCLN_dict = dict()
    for uniq_name in sort_csv: 
        if uniq_name['Name'] in 'PCLN' and uniq_name['date'] in "2017-08-08":
            PCLN_dict.update(uniq_name)
            print(PCLN_dict)
    with open('dumps.csv', 'w') as file:
        write_file = csv.writer(file)
        for i in PCLN_dict:
            write_file.writerows(i)
            

if __name__ == "__main__":
    select_sorted()
    sort_csv = select_sorted()
    get_by_date()
