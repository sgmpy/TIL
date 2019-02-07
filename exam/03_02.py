# 파일명 변경 금지
def alphabet_mode(word):
    # 아래에 코드를 작성하시오.
    # word는 소문자로만 구성 되어있습니다.
    # word에서 가장 많이 발생한 알파벳 하나를 반환합니다.
    result = {}
    for char in word:
        if char in result:
            result[char] = result[char] + 1
        else:
            result[char] = 1
    
    max_count = max(result.values())

    for char, count in result.items():
        if max_count == count:
            return char



# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(alphabet_mode('hello'))
    print(alphabet_mode('internationalization'))
    print(alphabet_mode('haha'))