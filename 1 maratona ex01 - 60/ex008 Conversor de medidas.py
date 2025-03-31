m = float(input('\033[31;1;7m A medida em metros e?: \033[m'))
dm = m * 10
cm = m * 100
mm = m * 1000
da = m / 10
hm = m / 100
km = m /1000
print('\033[32;1mA medida em dm é {}\n , em cm é {}\n , em mm é {}\n , em da é {}\n , em hm é {}\n , em km é {}\n '.format(dm, cm, mm, da, hm, km))