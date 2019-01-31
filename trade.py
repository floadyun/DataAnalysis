from bs4 import BeautifulSoup
import matplotlib.pyplot as plot

class Symbol:
    symbol = ''
    lot = 0
    direction = 'sell'
    openTime = ''
    closeTime = ''
    openPrice = ''
    closePrice = ''
    profit = 0.0

symbols = []
tradeRecords = ['184109.html', '220327.html', '223736.html', '526398.htm', '196322.html', '211953.html', '214354.html']
for tradeRecord in tradeRecords:
    soup = BeautifulSoup(open("file\\trade\\"+tradeRecord, 'r', encoding='utf-8'), 'lxml')
    trs = soup.find_all('tr', attrs={'align': "right"})
    print('记录长度:', len(trs))
    for tr in trs:
        tds = tr.contents
        if len(tds) > 13:
            symbol = tds[4].string
            if symbol == '\n':
                break
            symbol = Symbol()
            symbol.direction = tds[2].string
            symbol.lot = float(tds[3].string)
            symbol.symbol = tds[4].string.replace('.ecn', '').upper()
            if symbol.symbol == 'GOLD':
                symbol.symbol = 'XAUUSD'
            symbol.openTime = tds[1].string
            symbol.closeTime = tds[8].string
            symbol.openPrice = tds[5].string
            symbol.closePrice = tds[9].string
            symbol.profit = float(tds[13].string)
            symbols.append(symbol)
            # if symbol in symbols:
            #     symbols[symbol].append(symbol)
            #     numbes[symbol].append(tds[3].string)
            # else:
            #     trades = []
            #     singleNumbs = []
            #     trades.append(symbol)
            #     singleNumbs.append(tds[3].string)
            #     symbols[symbol] = trades
            #     numbes[symbol] = singleNumbs

for symbol in symbols:
    print('交易品种:', symbol.symbol, ';交易手数:', symbol.lot, '交易方向：', symbol.direction, '开仓价:', symbol.openPrice, '平仓价:', symbol.closePrice, '盈亏:', symbol.profit)
print('\n')
def analysisSymbol(trades):
    categorys = {}
    for trade in trades:
        if trade.symbol in categorys:
            symbols = categorys[trade.symbol]
            symbols.append(trade)
        else:
            symbols = []
            symbols.append(trade)
            categorys[trade.symbol] = symbols
    allProfit = 0
    maxProfit = 0
    maxLoss = 0
    totalProfit = 0
    totalLoss = 0
    trades = 0
    totalVolumes = 0
    for category in categorys.values():
        profit = 0
        volume = 0
        symbol = category[0]
        for symbol1 in category:
            profit += symbol1.profit
            totalVolumes += symbol1.lot
            if symbol.symbol == symbol1.symbol:
                volume += symbol1.lot
            if symbol1.profit > 0:
                totalProfit += symbol1.profit
                if symbol1.profit > maxProfit:
                    maxProfit = symbol1.profit
            if symbol1.profit < 0:
                totalLoss += symbol1.profit
                if symbol1.profit < maxLoss:
                    maxLoss = symbol1.profit
        allProfit += profit
        trades += len(category)
        print('交易品种:', symbol.symbol, ' 交易笔数:', len(category), '交易量:', round(volume, 2), ' 盈亏:', round(profit, 2))

    print('\n交易笔数:', trades, '交易量:', round(totalVolumes, 2), '最大盈利:', maxProfit, '；最大亏损:', maxLoss, '总盈利:', round(totalProfit, 2), '总亏损:', round(totalLoss, 2), '合计盈亏:', round(allProfit, 2))
    # plot.xlabel('交易品种')
    # plot.ylabel('交易次数')
    # plot.plot(symbols)
    # plot.title('交易分析')
    # plot.show()

analysisSymbol(symbols)

