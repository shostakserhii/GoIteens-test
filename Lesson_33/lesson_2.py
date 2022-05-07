open_1 = open('confusedtravolta.jpg', 'rb')
context = open_1.read()

with open('copy_1.jpeg', 'wb') as f:
    f.write(context)
