# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:03:05 2018

@author: user
"""

from selenium import webdriver
import numpy as np
import pandas as pd
import datetime
import sys
sys.setrecursionlimit(10000)
today=datetime.date.today()

#csvファイル（既存データ）の読み込み
df=pd.read_csv("save data file")
#df=pd.DataFrame(index=[],columns=["id","name","date"])

#ブラウザ開く(most-popular today)
driver=webdriver.Edge('exist webdriver')
for i in np.arange(1,11):
    if i==1:
        driver.get("URL")
    else:
        a="URL/%s/" % str(i)
        driver.switch_to.default_content()  #最上位に戻す
        driver.get(a)
#    time.sleep(5)

    #動画のリスト取得
    l=driver.find_element_by_class_name("wrapper")
    l=l.find_element_by_class_name("main")
    l=l.find_element_by_class_name("row row3")
    l=l.find_element_by_class_name("content")
    l=l.find_element_by_class_name("thumbs-items")

    #そのページの動画一覧
    for i in l.find_elements_by_class_name("thumb"):
        a=i.find_element_by_tag_name("a")
        index=a.get_attribute("href").find('/',27)
        #id,nameをDataFrameに追加
        df=df.append(pd.DataFrame([[int(a.get_attribute("href")[27:index]),a.get_attribute("href")[index+1:-1],today.isoformat()]],columns=["id","name","date"]),ignore_index=True)
        #df.append(df2,ignore_index=True)
  
#重複データの削除（前残し）
df=df.drop_duplicates(["id"])
#dataframeの出力
df.to_csv("save data file",index=False)
        
driver.close()
driver.quit()