study(title="[RS]BBC V0", shorttitle="[RS]BBBc.V0", overlay=true)
length = input(8)
src = input(hl2)
deviations = input(2)
ma = sma(src, length)
oma = ma > ma[1] ? valuewhen(ma < ma[1], ma[1], 0) : ma < ma[1] ? valuewhen(ma > ma[1], ma[1], 0) : nz(oma[1])
upper = oma + stdev(src, length) * deviations
lower = oma - stdev(src, length) * deviations

plotcandle(oma, upper, lower, ma, color=ma>=upper?#9ce0b2:ma<=lower?#e0b29c:ma>=ma[1]?green:maroon)