import sys, csv
import operator
import os

def select_sorted(sort_columns=["high"], limit=30, group_by_name=False, order='desc', filename='documents/all_stocks_5yr.csv'):
    count = 0
    with open(filename, 'r', encoding='utf-8') as file_csv:
        csv_read = csv.DictReader(file_csv)
        sort_csv = sorted(csv_read, key=lambda x: x['high'], reverse=True)
        
        for _sort in sort_csv:
            if count != limit:
                count += 1
                print(f"{_sort['date']} | {_sort['open']} | {_sort['high']} | {_sort['low']} | {_sort['close']} | {_sort['volume']} | {_sort['Name']}")
    
    return sort_csv


def select_write(filename='dump.csv'):
    with open(filename, 'w') as file_csv:
        writer = csv.writer(file_csv)
        for save in sort_csv:
            writer.writerow(save)
    
    
if __name__ == "__main__":
    select_sorted()
    sort_csv = select_sorted()
    select_write()