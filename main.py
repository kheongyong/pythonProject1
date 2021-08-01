import pandas as pd
from tqdm.notebook import tqdm_notebook
import numpy as np
from pyarrow import csv
import os
from pydrive.drive import GoogleDrive
drive = GoogleDrive('/content/drive')
folder_name = "/content/drive/MyDrive/(B) Projects/KELAB Projects/EDACOM 2021/에너지 솔루션/한전 제공 데이터/경진대회__전력사용량1_과천시고압/"
temp_arr = ["01", "02", "03", "04"]
for i in range(len(temp_arr)) : #매 월에 따른 처리
    file_name = "(고압)과천시_2019"+temp_arr[i]+".csv" #파일명
    # df = pd.read_csv(folder_name + file_name, encoding = 'cp949')
    # df.shape
    #print(df)
    ##########################출력명######################
    all_files = os.listdir(folder_name)

    li = []
    column_names = ['date', 'time', '시/도', '읍_면_동', '고객번호', '계약종별', '계약전력', '공급방식', '고저압구분', '유효전력량', '지상무효전력량', '진상무효전력량']
    for filename in all_files:
        df = csv.read_csv(folder_name + file_name, read_options = csv.ReadOptions(encoding = 'CP949', skip_rows = 1, column_names = column_names))
        # df.drop_duplicates() # 중복 레코드를 제거함
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    frame.shape