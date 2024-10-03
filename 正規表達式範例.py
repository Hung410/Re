# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 20:08:21 2024

@author: 2h7u7
"""

import re
#範例一
# regex=r"[a-zA-Z]([12])\d{8}"
# string="A123456789, S299888777"
# match=re.search(regex,string) #search檢查有沒有不乾淨的文字(三字經之類)

# print(match)

# print(match[0])
# print(match.group())
# print(match.group(0)) #15 16 17是一樣的結果

# print(match.group(1)) #19 20是一樣的結果
# print(match[1]) #群組的結果


# # 範例二
# regex02=r"[0-9]+"
# regex022=r"\d{9}(\d)" #這是將尾數群組起來
# string2="0911111111, 0922222222, 0933333333"
# listmatch2=re.findall(regex02,string2) #綜合 符合規格的資料拿到手 使用findall
# listmatch22=re.findall(regex022,string2)
# print(listmatch2)
# print(listmatch22) #將尾數列印


#範例三
# regex03 = r'\d{9}(\d)'
# string03 = "0911111111, 0922222222, 0933333333"
# iterableMatch03 = re.finditer(regex03, string03)
# if iterableMatch03 != None:
#     for match in iterableMatch03:
#         print(match[0])
#         print(match[1])


#範例四
# regex04 = r'^2[0-9]{3}\/[01]?[0-9]\/([0-3]?[0-9])'
# string04 = "2024/09/18"
# match04 = re.match(regex04, string04) #match必須一開始就配對成功 不然會出錯
# print(match04)
# print(match04[0])
# print(match04[1])


#範例五
# regex05 = r'\d'
# string05 = "One1Two2Three3Four4"
# listMatch05 = re.split(regex05, string05) #看到數字就切
# print(listMatch05)#會有空字元

# #範例六
# regex06 = r"\D"
# string06 = "5-20 #1314"
# strResult = re.sub(regex06, "", string06)#第一個參數是正規表達式,"",資料來源
# print(strResult)  #非數字的清掉


#範例七 環視概念(有這樣的條件就會被選中)
#去除中文字裡的空白
#環視的東西不會被配對出來
# regex07 = r"\s(?![a-zA-Z])" # 也可以寫成 r"(?<![a-zA-Z])\s" #配對到右邊不是空白的東西
# string07 = "一 天 一 蘋 果 醫 生 遠 離 我。An apple a day keeps the doctor away." 
# strResult = re.sub(regex07, '', string07)
# print(strResult)


#範例八
# regex02=r"" #空字串
# string2="0912"
# listmatch2=re.findall(regex02,string2) #綜合 符合規格的資料拿到手 使用findall
# print(listmatch2) #出來會是5個空字串 0以前 0跟9之間 9跟1之間 2後面



# regex09 = r'(?=(\d{3})+\b)'
# string09 = '1234567890'
# strResult2 = re.sub(regex09, ',', string09) #3的倍數 這個組合 空的字元會變成,
# print(strResult2)

# regex09 = r'(?=(\d{3})+\b)'
# string09 = '1234567890'
# strResult3 = re.sub(regex09, ',', string09) #3的倍數 這個組合 空的字元會變成,
# print(strResult3)

# regex10 = r'(?<=\d)(?=(\d{3})+\b)' #左邊也要是數字的
# string10 = '123456789000'  
# print(re.sub(regex10, ',', string10))



#範例九
regex09 = r'[A-Z](?P<gender>[12])\d{8}' #gender 是key的名稱
string09 = "A100000001"
match09 = re.match(regex09, string09)

# 完整配對的文字
print(match09[0])
print(match09.group(0))
print(match09.group())
print(match09.group(1)) #group
print(match09['gender']) #字典的概念 取得group的值




