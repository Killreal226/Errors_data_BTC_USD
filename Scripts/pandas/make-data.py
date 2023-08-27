import pandas as pd
import json
import matplotlib.pyplot as plt
import math

data = pd.read_csv('test.csv', sep=',')

with open("dict_type.json", "r") as f:
    dict_type = json.load(f)

def type_data(data, dict_type):
    for key in dict_type:
        print( data[key].dtypes)

def price_more_less_buy(data):
    for i in range(10):
        mask = data[f'px_buy_{i+1}'] < 11000    #11000
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

    for i in range(10):
        mask = data[f'px_buy_{i+1}'] > 12000    #12000
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

def price_more_less_sell(data):
    for i in range(10):
        mask = data[f'px_sell_{i+1}'] < 11000
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

    for i in range(10):
        mask = data[f'px_sell_{i+1}'] > 14000
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

def amount_more_less_buy(data):
    for i in range(10):
        mask = data[f'amt_buy_{i+1}'] < 0    
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

    for i in range(10):
        mask = data[f'amt_buy_{i+1}'] > 100   
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

def amount_more_less_sell(data):
    for i in range(10):
        mask = data[f'amt_sell_{i+1}'] < 0    
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

    for i in range(10):
        mask = data[f'amt_sell_{i+1}'] == 100   
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

def check_None(data, dict_type):
    for key in dict_type:
        if key != 'moreTradesInBatch':
            mask = data[key].isnull()   
            rows_with_greater_values = data[mask]
            row_numbers = rows_with_greater_values.index.tolist()
            print(row_numbers)

def check_msg(data):
    for i in range(15):
        mask = data['msgSeqNum'].apply(lambda x: len(str(x)) == i+1)
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        if row_numbers != [] and len(row_numbers) < 1000:
            print(row_numbers)
        else:
            print('Not')

def check_duplicated(data):
    #print (data[data['msgSeqNum'].duplicated()].index)
    print(data[data.index.isin(data[data['msgSeqNum'].duplicated()].index)])

def check_time(data):
    mask = data['exchHostTime'] > data['adapterTime']
    rows_with_greater_values = data[mask]
    row_numbers = rows_with_greater_values.index.tolist()
    print(row_numbers)
    
def check_type(data):
    mask = (data['type'] != 4) & (data['type'] != 6)
    rows_with_greater_values = data[mask]
    row_numbers = rows_with_greater_values.index.tolist()
    print(row_numbers)

def check_spred(data):
    for i in range(10): 
        mask = data[f'px_buy_{i+1}'] > data['px_sell_1']
        rows_with_greater_values = data[mask]
        row_numbers = rows_with_greater_values.index.tolist()
        print(row_numbers)

def trade_amt_px(data):
    for i in range(40375):
        data_series = data.loc[i]
        flag = True
        for j in range (10):
            if (data_series['trade_px'] == data_series[f'px_sell_{j+1}']) or (data_series['trade_px'] == data_series[f'px_buy_{j+1}']):
                flag = False
                break
        if flag == True:
            print (i)
    print ('Я кончил')

def check_invalid_time(data):
    mask = (data['exchHostTime'] < 1596240037364000000) | (data['exchHostTime'] > 1596241406562000000)
    rows_with_greater_values = data[mask]
    row_numbers = rows_with_greater_values.index.tolist()
    print(row_numbers)

def check_trade_count (data):
    mask = data['trade_cnt'] < 0
    rows_with_greater_values = data[mask]
    row_numbers = rows_with_greater_values.index.tolist()
    print(row_numbers)

def plot_density(data):
    plt.bar(data['px_buy_1'].index, height=data['px_buy_1']) 
    plt.show()

def check_fractional_part(data):
    for j in range(40375):
        data_series = data.loc[j]
        for i in range(10):
            if (len(str(data_series[f'px_buy_{i+1}'])) > 8) or (len(str(data_series[f'px_sell_{i+1}'])) > 8):
                print('нашел')
    print('я все')

def check_spred_2(data):
    mask = (data['px_sell_1'] - data['px_buy_1']) < 0.009
    rows_with_greater_values = data[mask]
    row_numbers = rows_with_greater_values.index.tolist()
    print(row_numbers)

def check_trade_amt_px(data):
    mask = ((data['trade_px'] != 0) & (data['trade_amt'] == 0)) | ((data['trade_px'] == 0) & (data['trade_amt'] != 0))
    rows_with_greater_values = data[mask]
    row_numbers = rows_with_greater_values.index.tolist()
    print(row_numbers)

def check_fraction(data):
    for j in range(40375):
        data_series = data.loc[j]
        flag = False
        for i in range(10):
            try:
                if len(str(data_series[f'px_buy_{i+1}']).split('.')[1]) > 2:
                    flag = True
                    break
            except:
                pass
            try:
                if len(str(data_series[f'px_sell_{i+1}']).split('.')[1]) > 2:
                    flag = True
                    break
            except:
                continue
        try:
            if len(str(data_series[f'trade_px']).split('.')[1]) > 2:
                flag = True
        except:
            continue
        if flag:
            print(j)

def check_delay(data):
    mask = (data['adapterTime'] - data['exchHostTime']) > 999000000
    rows_with_greater_values = data[mask]
    row_numbers = rows_with_greater_values.index.tolist()
    print(row_numbers)

if __name__ == '__main__':
    #type_data(data, dict_type)
    #print(data[30:82])
    #price_more_less_buy(data)
    #price_more_less_sell(data)
    #amount_more_less_buy(data)
    #amount_more_less_sell(data)
    #check_None(data, dict_type)
    #check_msg(data)
    #check_duplicated(data)
    #check_time(data)    #Надо подумать как это грамотно сказать 
    #check_type(data)
    #check_spred(data)
    #check_invalid_time(data)
    #check_trade_count(data)
    #plot_density(data)         
    #check_fractional_part(data)
    #check_spred_2(data)         
    #check_trade_amt_px(data)
    #check_fraction(data)
    check_delay(data)
