#python 3.7.1

print ("Hello, Dcoder!")
import random
import string

def generate_coupons(num_coupons, length=12):
    coupons = set()
    while len(coupons) < num_coupons:
        coupon = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        coupons.add(coupon)
    return coupons

def save_to_file(coupons, filename="coupons.txt"):
    with open(filename, "w") as file:
        for coupon in coupons:
            file.write(coupon + "\n")

# توليد 100 مليار قسيمة
num_coupons = 10_000_000_0000  # عدد القسائم
coupon_length = 12  # طول القسيمة
coupons = generate_coupons(num_coupons, coupon_length)

# حفظ القسائم في ملف نصي
save_to_file(coupons, "100_billion_coupons.txt")
print("تم إنشاء القسائم وحفظها بنجاح في الملف 100_billion_coupons.txt")