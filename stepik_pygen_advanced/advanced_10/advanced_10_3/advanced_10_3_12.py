text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for symbol in text:
    result[symbol] = result.setdefault(symbol, text.count(symbol))
