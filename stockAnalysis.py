import csv

csv_reader = csv.reader(open("file\\stock.csv"))
totalBuy = 0
totalSell = 0
totalVolume = 0
stocks = {}
for row in csv_reader:
    if row[2] in stocks:
        trade = stocks[row[2]]
        trade.append(row[2])
    else:
        trade = []
        trade.append(row[2])
        stocks[row[2]] = trade
    if row[0] == '买入':
        totalBuy += float(row[5])
        totalVolume += int(row[3])
    elif row[0] == '卖出':
        totalSell += float(row[5])
    print(row)
print('\n交易品种:', len(stocks), '交易量:', totalVolume/100, '交易次数', csv_reader.line_num/2, '买入:', totalBuy, ';卖出:', totalSell, '盈亏:', round(totalSell - totalBuy))