# 引入requests module
import requests
# 引入 連接 DB module
import mysql.connector
from mysql.connector import Error


def getVideoId_2():
    url_2="https://www.youtube.com/c/%E7%99%BD%E7%99%A1%E5%85%AC%E4%B8%BB%E7%9A%84%E7%84%A1%E7%A2%BC%E5%B0%88%E5%8D%80/videos"
    r_2 = requests.get(url_2)
    playList_2 = []
    end_2 = 0

    for i in range(6):
        pre_start = end_2
        start = r_2.text.index('watch?v=',pre_start) #抓strat index index('定位文字', 給一個起始值)
        end_2 = r_2.text.index('"', start)             #抓end index index('定位文字', 剛剛抓到的start index)
        playList_2.append(r_2.text[start+8:end_2])
    print(*playList_2, sep="\n")
    return playList_2

def getVideoId():
    # HTML 的 str 都有 index 抓取index 就可以抓到影片ID
    url="https://www.youtube.com/c/%E7%99%BD%E7%99%A1%E5%85%AC%E4%B8%BB/videos"
    r = requests.get(url)
    playList = []
    end = 0

    #print("輸入要查詢多少影片ID :")
    for i in range(6):
        pre_start = end
        start = r.text.index('watch?v=',pre_start) #抓strat index index('定位文字', 給一個起始值)
        end = r.text.index('"', start)             #抓end index index('定位文字', 剛剛抓到的start index)
        playList.append(r.text[start+8:end])
    #print(*playList, sep="\n")
    return playList

def DBconnect_2(data_2):
    playList_2 = data_2
    try:
    # 連接 MySQL/MariaDB 資料庫
        connection = mysql.connector.connect(
            host='localhost',                 # 主機名稱
            port='3306',
            database='87acup_board',  # 資料庫名稱
            user='shiueer',           # 帳號
            password='123456789'      # 密碼
        )
        # update data
        num = 0
        for i in playList_2:
            num = num + 1
            cursor = connection.cursor()
            #sql = "INSERT INTO `video_2` (`ID`, `Video`) VALUES (%s,%s)"
            sql = "UPDATE `video_2` SET `Video`=%s WHERE `ID`=%s;"
            val = (i,num)
            cursor.execute(sql,val)
            connection.commit()
            #print('Success')
        connection.close()
        #if connection.is_connected():
            # 顯示資料庫版本
            #db_Info = connection.get_server_info()
            #print("資料庫版本：", db_Info)

            # 顯示目前使用的資料庫
            #cursor = connection.cursor()
            #cursor.execute("SELECT DATABASE();")
            #record = cursor.fetchone()
            #print("目前使用的資料庫：", record)
    except Error as e:
        print("[ERROR MSG]：", e)


def DBconnect(data):
    playList = data
    try:
    # 連接 MySQL/MariaDB 資料庫
        connection = mysql.connector.connect(
            host='localhost',                 # 主機名稱
            port='3306',
            database='87acup_board',  # 資料庫名稱
            user='shiueer',           # 帳號
            password='123456789'      # 密碼
        )
        # update data
        num = 0
        for i in playList:
            num = num + 1
            cursor = connection.cursor()
            sql = "UPDATE `video` SET `Video`=%s WHERE `ID`=%s;"
            val = (i,num)
            cursor.execute(sql,val)
            connection.commit()
            #print('Success')
        connection.close()
        #if connection.is_connected():
            # 顯示資料庫版本
            #db_Info = connection.get_server_info()
            #print("資料庫版本：", db_Info)

            # 顯示目前使用的資料庫
            #cursor = connection.cursor()
            #cursor.execute("SELECT DATABASE();")
            #record = cursor.fetchone()
            #print("目前使用的資料庫：", record)
    except Error as e:
        print("[ERROR MSG]：", e)

            
def main():
    data = getVideoId()
    data_2 = getVideoId_2()
    DBconnect(data)
    DBconnect_2(data_2)


main()