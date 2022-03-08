# โครงสรา้งควบคุม (control Structure)
# 1. แบบลำดับ
# 2. แบบเลือก
# 3. แบบทำซ้ำ

'''
if boolean expression
    statement

'''

age = int(input("คุณมีอายุเท่าไหร่ :"))

'''if age>=15:
    print("วัยรุ่น")
    print("จบโปรแกรม")
elif age>=20:
    print("วัยผู้ใหญ่")
    print("จบโปรแกรม")
elif age>=30:
    print("วัยทำงาน")
    print("จบโปรแกรม")
else:
    print("วัยเด็ก")
    print("จบโปรแกรม")'''

#age == 15
#name = "ninny"
#print(type(age>=15))
#print(name=="ninny")

# โครงสร้างควบคุมแบบเลือก (if..else)
'''
if จริง :
    ทำอะไร
else เท็จ :
    ทำอะไร
'''
# #การใช้ And Or Not

if age>=15 and age <=19:
    print("วัยรุ่น")
    print("จบโปรแกรม")
elif age>=20 and age <=29:
    print("วัยผู้ใหญ่")
    print("จบโปรแกรม")
elif age>=30:
    print("วัยทำงาน")
    print("จบโปรแกรม")
else:
    print("วัยเด็ก")
    print("จบโปรแกรม")
# Ternary Operator
"เงื่อนไขเป็นจริง if expression else เงื่อนไขอื่น ๆ "
print("วัยรุ่น") if age>=15 else print("วันเด็ก")

print ("จบโปรแกรม")


