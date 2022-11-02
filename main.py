# Program make a simple calculator

#개발 내용 Checklist
#정상적인 경우에 대해서 로그 찍기 완료
#Divide by zero 예외 경고 만들기
#대소문자 구분 없이 다음 계산 진행할지 여부 확인
#Are you sure? 질문 만들기
#다른 파일에 계산 함수 옮기고 그 파일에서 불러오기 

# 로그 기록을 만들 클래스 import 하기

import logging
from os import system

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 콘솔 출력을 지정합니다
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 파일 출력을 지정합니다.
fh = logging.FileHandler(filename="Calclog.txt")
fh.setLevel(logging.INFO)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)


#여기까지가 로그 전처리 구간

import Calculate

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            numadd=Calculate.add(num1, num2)
            logging.debug(f'콘솔 출력 : {num1} + {num2} = {numadd}')
            logging.info(f'파일 출력 : {num1} + {num2} = {numadd}')
            

        elif choice == '2':
            numsub=Calculate.subtract(num1,num2)
            logging.debug(f'콘솔 출력 : {num1} - {num2} = {numsub}')
            logging.info(f'파일 출력 : {num1} - {num2} = {numsub}')

        elif choice == '3':
            nummul=Calculate.multiply(num1, num2)
            logging.debug(f'콘솔 출력 : {num1} * {num2} = {numadd}')
            logging.info(f'파일 출력 : {num1} * {num2} = {numadd}')
            
        elif choice == '4':
            if num2 == 0:
                logging.debug('잘못된 입력입니다 제수가 0이 되면 안됩니다')
                logging.info('잘못된 입력입니다 제수가 0이 되면 안됩니다')
            else:
                numdiv=Calculate.divide(num1,num2)
                logging.debug(f'콘솔 출력 : {num1} / {num2} = {numdiv}')
                logging.info(f'파일 출력 : {num1} / {num2} = {numdiv}')
                    
        else:
            logging.info(f'파일 출력 : 연산 선택은 1,2,3,4만 가능합니다')    

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        next_calculation=next_calculation.lower()
        if next_calculation == "no":
            next_sure = input("Are you sure? (yes/no): ")
            next_sure=next_sure.lower()
            if next_sure == "yes":
                break
        

    else:
        logging.info('정상적이지 않은 선택입니다 다시 입력해주세요')