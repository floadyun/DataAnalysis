from bs4 import BeautifulSoup
import matplotlib.pyplot as plot
import operator

class Symbol:
    year = ''
    symbol = ''
    lot = 0
    direction = 'sell'
    openTime = ''
    closeTime = ''
    openPrice = ''
    closePrice = ''
    profit = 0.0

symbols = []
tradeRecords = ['184109.html', '211953.html',  '22769972.htm',  '526398.htm', '63401.htm', '80881309.htm', '220327.html', '223736.html', '2024063.htm',  '196322.html',  '214354.html',
                 '22789423.htm',  '22769972_2.htm', '80885244.htm', '8009113.htm', '8009926.htm']
for tradeRecord in tradeRecords:
    if tradeRecord == '2024063.htm':
        soup = BeautifulSoup(open("file\\trade\\" + tradeRecord, 'r', encoding='utf-8'), 'lxml')
        trs = soup.find_all('tr')
        line = 0
        for tr in trs:
            tds = tr.contents
            if len(tds) > 13:
                symbol = tds[1].string
                if symbol == '\n':
                    break
                symbol = Symbol()
                symbol.direction = tds[7].string
                symbol.lot = float(tds[15].string)
                symbol.symbol = tds[5].string.replace('.ecn', '').upper()

                symbol.openTime = tds[9].string
                symbol.closeTime = tds[9].string
                symbol.openPrice = tds[11].string
                symbol.closePrice = tds[12].string
                symbol.profit = float(tds[23].string)
                symbols.append(symbol)
    else:
        soup = BeautifulSoup(open("file\\trade\\"+tradeRecord, 'r', encoding='utf-8'), 'lxml')
        trs = soup.find_all('tr', attrs={'align': "right"})
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
                symbol.symbol = symbol.symbol.replace('.STP', '')
                symbol.symbol = symbol.symbol.replace('.', '')

                if symbol.symbol == 'USOIL':
                    symbol.symbol = 'XTIUSD'
                if symbol.symbol == 'GOLD':
                    symbol.symbol = 'XAUUSD'
                symbol.openTime = tds[1].string
                symbol.closeTime = tds[8].string
                symbol.openPrice = tds[5].string
                symbol.closePrice = tds[9].string
                symbol.profit = float(tds[13].string)
                symbols.append(symbol)

def analysisSymbol(trades):
    categorys = {}
    times = {}
    months = {}
    for trade in trades:
        print('交易品种:', trade.symbol, '交易手数:', trade.lot, '交易方向:', trade.direction, '开仓时间', trade.openTime, '盈亏:', trade.profit)
        if trade.symbol in categorys:
            symbols = categorys[trade.symbol]
            symbols.append(trade)
        else:
            symbols = []
            symbols.append(trade)
            categorys[trade.symbol] = symbols
        time = trade.openTime.split(' ')[0]
        month = trade.openTime.split(' ')[0]
        if time.__contains__('.'):
            time = time.split(".")[0]
            month = month.split('.')[1]
        elif time.__contains__('/'):
            time = time.split('/')[2]
            month = month.split('/')[1]
        if time in times:
            symbolss = times[time]
            symbolss.append(trade)
            if month in months[time]:
                monthSymbols = months[time][month]
                monthSymbols.append(trade)
            else:
                monthSymbols = []
                monthSymbols.append(trade)
                months[time][month] = monthSymbols
        else:
            symbolss = []
            symbolss.append(trade)
            times[time] = symbolss
            monthSymbols = {}
            monthSymbolss = []
            monthSymbolss.append(trade)
            monthSymbols[month] = monthSymbolss
            months[time] = monthSymbols
    allProfit = 0
    maxProfit = 0
    maxLoss = 0
    totalProfit = 0
    totalLoss = 0
    trades = 0
    totalVolumes = 0
    print('\n')
    numbers = 0
    for category in categorys.values():
        profit = 0
        volume = 0
        buys = 0
        sells = 0
        symbol = category[0]
        for symbol1 in category:
            profit += symbol1.profit
            totalVolumes += symbol1.lot
            volume += symbol1.lot
            if symbol1.profit > 0:
                totalProfit += symbol1.profit
                if symbol1.profit > maxProfit:
                    maxProfit = symbol1.profit
            if symbol1.profit < 0:
                totalLoss += symbol1.profit
                if symbol1.profit < maxLoss:
                    maxLoss = symbol1.profit
            if symbol1.profit < -1000:
                numbers += 1
            if symbol1.direction == 'buy':
                buys += 1
            else:
                sells += 1
        allProfit += profit
        trades += len(category)
        print('交易品种:', symbol.symbol, ' 交易笔数:', len(category), '交易量:', round(volume, 2),  '多/空:%d/%d' % (buys, sells),  '盈亏:', round(profit, 2))
    print('\n')
    print('亏损超一千美金的次数：', numbers)
    times = dict(sorted(times.items(), key=operator.itemgetter(0)))  # 按key值排序
    for category in times.values():
        profit = 0
        volume = 0
        buys = 0
        sells = 0
        symbol = category[0]
        time = symbol.openTime.split(' ')[0]
        if time.__contains__('.'):
            time = time.split(".")[0]
        elif time.__contains__('/'):
            time = time.split('/')[2]
        for symbol1 in category:
            profit += symbol1.profit
            volume += symbol1.lot
            if symbol1.profit > 0:
                if symbol1.profit > maxProfit:
                    maxProfit = symbol1.profit
            if symbol1.profit < 0:
                if symbol1.profit < maxLoss:
                    maxLoss = symbol1.profit
            if symbol1.direction == 'buy':
                buys += buys
            else:
                sells += sells
        trades += len(category)
        print('\n交易年限:', time, ' 交易笔数:', len(category), '交易量:', round(volume, 2),  ' 盈亏:', round(profit, 2))
        monthTrade = months[time]
        monthTrade = dict(sorted(monthTrade.items(), key=operator.itemgetter(0)))#按key值排序
        for monthList in monthTrade.values():
            monthProfit = 0
            monthVolume = 0
            for mTrade in monthList:
                monthRecord = mTrade.openTime.split(' ')[0]
                if monthRecord.__contains__('.'):
                    monthRecord = monthRecord.split(".")[1]
                elif monthRecord.__contains__('/'):
                    monthRecord = monthRecord.split('/')[1]
                monthProfit += mTrade.profit
                monthVolume +=mTrade.lot
            print('月份：', monthRecord, '交易笔数：', len(monthList), '交易量', round(monthVolume, 2), '盈亏：', round(monthProfit, 2))

    print('\n交易品种:', len(categorys), '交易笔数:', trades, '交易量:', round(totalVolumes, 2), '最大盈利:', maxProfit, '最大亏损:', maxLoss, '总盈利:', round(totalProfit, 2), '总亏损:', round(totalLoss, 2), '合计盈亏:', round(allProfit, 2))

    # plot.xlabel('交易品种')
    # plot.ylabel('交易次数')
    # plot.plot(symbols)
    # plot.title('交易分析')
    # plot.show()

analysisSymbol(symbols)

