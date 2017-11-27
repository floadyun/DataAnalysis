from bs4 import BeautifulSoup
import matplotlib.pyplot as plot

class Symbol:
    symbol = ''
    lot = 0
    direction = 'sell'
    openPrice = ''
    closePrice = ''

soup = BeautifulSoup(open("file\\526398.htm", 'r', encoding='utf-8'), 'lxml')
trs = soup.find_all('tr', attrs={'align': "right", 'bgcolor': ''})
symbols = []
# print(trs)
for tr in trs:
    tds = tr.contents
    if len(tds) > 5:
        symbol = tds[4].string
        if symbol == '\n':
            break
        symbol = Symbol()
        symbol.direction = tds[2].string
        symbol.lot = tds[3].string
        symbol.symbol = tds[4].string
        symbol.openPrice = tds[5].string
        symbol.closePrice = tds[9].string
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
    print('交易品种:', symbol.symbol, ';交易手数:', symbol.lot, '交易方向：', symbol.direction, '开仓价:', symbol.openPrice, '平仓价:', symbol.closePrice)
def analysisSymbol(trades):
    symbols = {}
    for trade in trades:
        if trade.symbol in symbols:
            lots = symbols[trade.symbol]
            lots.append(float(trade.lot))
        else:
            lots = []
            lots.append(float(trade.lot))
            symbols[trade.symbol] = lots

    for symbol in symbols:
        print('交易品种:', symbol, '；交易次数: ', len(symbols[symbol]))

    plot.xlabel('交易品种')
    plot.ylabel('交易次数')
    plot.plot(symbols)
    plot.title('交易分析')
    plot.show()
print('------------------------------------------------------------------------------')
analysisSymbol(symbols)

