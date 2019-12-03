#PyAutoGUI 설치하장!!!!><

import pyautogui as pag
import time
if __name__== '__main__':
    # while True:
    #     x,y = pag.position() 마우스 좌표 찾기
    #     print ("x : {}\ty : {}".format(x,y), end = "\r")
    # pag.moveTo(1088,275,duration=0.3) # 어디까지 이동해라
    # pag.move(1088,275,duration=0.3) #지금 위치에서 저 값을 더한만큼 가라.
    # pag.doubleClick()
    # pag.drag(0,200,duration=1)
    # pag.rightClick()
    pag.doubleClick(1088,275)
    #TODO: scroll
    time.sleep(1) #크롬이 열리기를 기다려야한대용!!!!!
    pag.typewrite("http://ticket.interpark.com/")
    #pag.press("hangual") // 강하늘 한글로 바꾸기
    # pag.typewrite("rkdgksmf")
    pag.press("enter")
