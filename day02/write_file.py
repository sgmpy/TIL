# f = open('ssafy.txt','w') # w: write, r: read, a: append
# f.write('This is SSAFY!')
# f.close()

with open('ssafy.txt','w',encoding='utf8') as f:
    f.write('This is SSAFY!, with 이용했다.')
