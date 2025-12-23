total = 0

for i in range(5):
    price = float(input("Enter product price: "))
    total += price

gst = total * 0.18
bill = total + gst

print("Total =", total)
print("GST =", gst)
print("Final Bill =", bill)