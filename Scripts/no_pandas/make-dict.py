import json

str_1 = 'type,msgSeqNum,exchHostTime,adapterTime,px_buy_1,amt_buy_1,px_buy_2,amt_buy_2,px_buy_3,amt_buy_3,px_buy_4,amt_buy_4,px_buy_5,amt_buy_5,px_buy_6,amt_buy_6,px_buy_7,amt_buy_7,px_buy_8,amt_buy_8,px_buy_9,amt_buy_9,px_buy_10,amt_buy_10,px_sell_1,amt_sell_1,px_sell_2,amt_sell_2,px_sell_3,amt_sell_3,px_sell_4,amt_sell_4,px_sell_5,amt_sell_5,px_sell_6,amt_sell_6,px_sell_7,amt_sell_7,px_sell_8,amt_sell_8,px_sell_9,amt_sell_9,px_sell_10,amt_sell_10,trade_px,trade_amt,trade_cnt,moreTradesInBatch'

def make_dict(str_1: str):
    dict_type = {}
    list_type = str_1.split(',')
    for key in list_type:
        dict_type[key] = []
    with open("dict_type.json", "w") as f:
        json.dump(dict_type, f)

def write_dict():
    with open("list_count.txt", "r") as file:
        lines = file.readlines()
    list_lines = [line.strip().split(',') for line in lines]
    with open("dict_type.json", "r") as f:
            dict_type = json.load(f)
    for line in list_lines:
        i = 0 
        for key in dict_type:
            dict_type[key].append(line[i])
            i += 1
    with open("dict_full.json", "w") as f:
        json.dump(dict_type, f)

if __name__ == '__main__':
    #make_dict(str_1)
    #write_dict()
    pass