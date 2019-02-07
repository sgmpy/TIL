# 파일명 변경 금지
# 아래에 클래스 Word를 선언하세요.
class Word:
    def __init__(self):
        self.wordbook = {}

    def add(self, en, ko):
        self.wordbook.update({en: ko})
        # print(self.wordbook)
        # self.wordbook[en] = ko

    def delete(self, en):
        if en in self.wordbook:
            self.wordbook.pop(en)
            # del self.wordbook[en]
            return True
        else:
            return False
    
    def print(self):
        for en, ko in self.wordbook.items():
            print(f'{en}: {ko}')





# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    my_book = Word()
    my_book.add('apple', '사과')
    my_book.add('banana', '바나나')
    my_book.add('cherry', '체리')
    my_book.add('durian', '두리안')
    my_book.print() 
    print(my_book.delete('cherry'))
    print(my_book.delete('durian'))
    print(my_book.delete('egg'))
    my_book.print()