import os

os.chdir(r'C:\Users\student\junwoo\day02\dummy')
# print(os.getcwd())
for filename in os.listdir('.'):
    # 1. replace 함수 이용, 새로운 파일 이름 생성
    new_filename = filename.replace('지원자_지원자_', '합격자_')
    # 2. os.rename 함수 이용, 파일 이름 변경
    os.rename(filename, new_filename)

# 합격자_0_누구누구.txt