tf = float(input('digite a temperatura em Fahrenheit'))
tc = (tf - 32) * (5/9)
tk = (tf + 459.67) * (5/9)
print('em K: {:.2f} e em C: {:.2f}'.format(tk,tc))
 