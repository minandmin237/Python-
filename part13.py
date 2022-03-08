#Assignment 1: โปรแกรมคำนวณค่าดัชนีมวลกาย (BMI)
# BMI = น้ำหนัก (Kg) / ส่วนสูง * ส่วนสูง  (m)

# input
weight = int(input ("กรุณาป้อนน้ำหนักของคุณ (kg) :"))
high = int(input("ป้อนส่วนสูงของคุณ (cm) :"))

#process
#cm => m
high = high/100
#calculate bmi
bmi = weight/(high*high)

#ouput
print("BMI = " ,bmi)