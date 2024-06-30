import csv
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utF-8') #改变标准输出的默认编码
csv_reader = csv.reader(open("file\\stock.csv"))
totalBuy = 0
totalSell = 0
totalVolume = 0
stocks = {}
trades = {}
for row in csv_reader:
    if row[2] in trades:
        if row[0] == '买入':
            trades[row[2]] -= float(row[5])
        elif row[0] == '卖出':
            trades[row[2]] += float(row[5])
    else:
        if row[0] == '买入':
            trades[row[2]] = -float(row[5])
        elif row[0] == '卖出':
            trades[row[2]] = float(row[5])
    if row[0] == '买入':
        totalBuy += float(row[5])
        totalVolume += int(row[3])
    elif row[0] == '卖出':
        totalSell += float(row[5])

for symbole,value in trades.items():
    print('交易品种: ', symbole, '盈亏：', round(value))
print('\n交易品种:', len(trades), '交易量:', totalVolume/100, '交易次数', csv_reader.line_num/2, '买入:', totalBuy, ';卖出:', totalSell, '总盈亏:', round(totalSell - totalBuy))