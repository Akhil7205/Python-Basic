print('started basic python')

for j in range(1, 11):
    for i in range(11, 21):
        print(f"{i} * {j} = {i*j}", end='\t')
    print()  # Move to the next line after printing one row




# statement=input("enter name: ")

# a=(statement.isalpha() or statement.isspace())
# print(a)
# statement = input("Enter name: ")
# for char in statement:
#     a = (char.isalpha() or char.isspace())
# print(a)

import datetime

# from datetime import datetime

# now=datetime.now()
# print(now)
# time=lambda x:x.time()
# hr=now.hour
# print(hr)
import time
a=time.strftime('%c')
print(a)