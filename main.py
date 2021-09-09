import socket
import sys
import time
import os, subprocess
import threading
import serial
import object
global check
global var

def set():
    os.system('object.exe')

def set2():
    global check
    arduino = serial.Serial('com7', 9600)
    temp = "";
    dist1 = "";
    dist2 = "";
    dist3 = "";
    time.sleep(1)
    print(check)

    #while 1:
    if (check == True):
        var = "D1".encode('utf-8')
        arduino.write(var)
        print("#D1; 투입구 개방")

    if (check == False):
        var = "D0".encode('utf-8')
        arduino.write(var)
        print("#D0; 투입구 폐쇄")
        time.sleep(2)
        arduino.close()

    if (check == True):
        var = "B1".encode('utf-8')
        arduino.write(var)
        print("#B1; 벨트 가동")

    if (check == False):
        var = "B0".encode('utf-8')
        arduino.write(var)
        print("#B0; 벨트 중단")
        time.sleep(2)
        arduino.close()

    # elif (var == "B2\n"):
    #    var = var.encode('utf-8')
    #    arduino.write(var)
    #    print("#B2; 벨트 반전")

    # elif (var == "C0\n"):
    #    var = var.encode('utf-8')
    #    arduino.write(var)
    #    print("#C0; 쓰레기 중간, 초기상태")

    if (object.obj == "pet"):
        var = "C1".encode('utf-8')
        arduino.write(var)
        print("#C1; 쓰레기 좌측")

    if (object.obj == "can"):
        var = "C2".encode('utf-8')
        arduino.write(var)
        print("#C2; 쓰레기 우측")

    if (check == True):
        var = "LED ON".encode('utf-8')
        arduino.write(var)
        print("LED ON")

    if (check == False):
        var = "LED OFF".encode('utf-8')
        arduino.write(var)
        print("LED OFF")
        time.sleep(2)
        arduino.close()

    if check == False:
        var = "R1".encode('utf-8')
        arduino.write(var)
        """ 1번 째 센서 값 출력 """
        time.sleep(2)
        arduino.close()
        for i in range(2):
            temp = temp + str(arduino.read().decode('utf-8'))
        dist1 = int(temp)
        print(dist1)
        temp = ""
        for i in range(2):
            temp = temp + str(arduino.read().decode('utf-8'))
        dist2 = int(temp)
        print(dist2)
    time.sleep(1)



def set1(data2):
    t3 = threading.Thread(target=set)
    t3.start()
    while True :
        data2
        # print(data2.encode())
        # client_sock.send(data)
        # client_sock.send(data2.to_bytes(4, byteorder='little'))
        i = 2

        # 값하나 보냄(사용자가 입력한 숫자)
        client_sock.sendall(data2.to_bytes(4, byteorder='little'))  # int에서 바이트 변환
        # .to_bytes(4, byteorder='little')

        # 안드로이드에서 값 받으면 "하나받았습니다 : 숫자" 보낼 것 받음
        data = client_sock.recv(1024)
        print("" + str(data.decode("utf-8") + ""))

        if data.decode("utf-8") == "c":
            print("stop    "+data.decode("utf-8"))
            print(os.system('tasklist'))  # 프로세스 목록 출력
            # os.system('taskkill /f /pid 11172') #pid를 사용한 프로세스 종료
            os.system('taskkill /f /im object.exe')  # 프로세스명을 사용한 프로세스 종료
            data2 = 1
            global check
            check = False
            break
        else:
            data2 += 1

        time.sleep(1)



host = '192.168.1.51'  # Symbolic name meaning all available interfaces
port = 8080  # Arbitrary non-privileged port

while True:
    server_sock = socket.socket(socket.AF_INET)
    server_sock.bind(('', port))
    server_sock.listen(1)

    print("기다리는 중")
    client_sock, addr = server_sock.accept()

    print('Connected by', addr)

# 서버에서 "안드로이드에서 서버로 연결요청" 한번 받음
    data = client_sock.recv(1024)
    print(data.decode("utf-8"), len(data))
    if data.decode("utf-8") != "":
        global check
        check = True
        t = threading.Thread(target=set1, args=(1,))
        t.start()
        t2 = threading.Thread(target=set2, args=(True,))
        t2.start()

    # 연결끊겠다는 표시 보냄
    # i=99
    # client_sock.send(i.to_bytes(4, byteorder='little'))

client_sock.close()
server_sock.close()