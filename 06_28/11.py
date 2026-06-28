sex = input("請輸入性別（男/女）：")
age = float(input("請輸入年齡："))
scr = float(input("請輸入血清肌酸酐 Scr："))

# eGFR 公式
if sex == "男":
    egfr = 186 * (scr ** -1.154) * (age ** -0.203)
elif sex == "女":
    egfr = 186 * (scr ** -1.154) * (age ** -0.203) * 0.742
else:
    print("性別輸入錯誤")
    exit()

# 判斷分期
if egfr >= 100:
    stage = "0 期"
elif egfr >= 90:
    stage = "1 期"
elif egfr >= 60:
    stage = "2 期"
elif egfr >= 30:
    stage = "3 期"
elif egfr >= 15:
    stage = "4 期"
else:
    stage = "5 期"

print("eGFR =", round(egfr, 2))
print("腎臟病分期：", stage)