# Comparative Operators (ตัวดำเนินการเปรียบเทียบ)

# Compare at least two data values. (นำข้อมูลอย่างน้อย 2 ค่ามาเปรียบเทียบกัน)
# same data type . (ชนิดข้อมูลเหมือนกัน)
# have just 2 answers => True / Fales (คำตอบ 2 คำตอบ => จริง / เท็จ)

x,y = 5, 7

print("ค่า X มากกว่า y หรือไม่ ? : " , x>y)
print("ค่า X น้อยกว่า y หรือไม่ ? : " , x<y)
print("ค่า X เท่ากับ y หรือไม่ ? : " , x==y)
print("ค่า X ไม่เท่ากับ y หรือไม่ ? : " , x!=y)

print("ค่า X มากกว่า หรือ เท่ากับ ค่า y หรือไม่ ? : " , x>=y)
print("ค่า X น้อยกว่า หรือ เท่ากับ ค่า y หรือไม่ ? : " , x<=y)

# เปรียบเทียบค่า 3 ค่า

q,w,e = 8, 7, 9
print ("ค่า x มากกว่า y และ y มากกว่า z หรือไม่ ? : " , q>w>e)
print ("ค่า x น้อกยว่า y และ y น้อยกว่า z หรือไม่ ? : " , q<w<e)
