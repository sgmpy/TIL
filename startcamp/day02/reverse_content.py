# 1. 한번에 처리
with open('ssafy.txt','r',encoding='utf8') as f:
    lines = reversed(f.readlines())
    with open('ssafy_reverse.txt', 'w', encoding='utf8') as ff:
        ff.writelines(lines)

# 2. read / write
with open('ssafy.txt','r',encoding='utf8') as f:
    lines = f.readlines()

lines.reverse()

with open('ssafy_reverse.txt', 'w', encoding='utf8') as f:
    f.writelines(lines)
