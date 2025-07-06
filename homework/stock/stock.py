"""
請使用python去完成
合併6/30～7/4的股票資料 每日收盤行情(全部) 成為一張資料表 (Data Frame)
使用 Colab 上傳 colab 分享連結
使用vs code   繳交 HackMD 連結，要包含程式碼及結果
請上傳 聊天機器人的對話紀錄分享連結
請使用df.info() 給整理完成 df 資訊
"""
import pandas as pd

def print_csv(path):
    df=pd.read_csv(path,encoding="big5")
    print(df.info())
