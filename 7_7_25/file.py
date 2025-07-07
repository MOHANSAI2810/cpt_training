# # with open('file1.txt', 'a') as f:
# #     a = ['mohan', 'abhijith']
# #     f.write(','.join(a) + '\n')


# with open("ADS&AA-4.pdf","rb") as f:
#     data=f.read()
#     print(data.decode('latin-1'))

# with open('binary','rb') as f:
#     print(f.read())


# with open('file1.txt', 'r+') as f:
#     a = f.readlines()
# for i in a:
#     print(i.strip())
# with open('File1.txt', 'r') as file:
#     sp_line = [line.strip() for line in file.readlines() if line.strip() != '']
#     print(sp_line)
#     print(file.closed)
#     file.close()
#     print(file.closed)

# with open('file1.txt', 'w+') as f:
#     while True:
#         print("Type anything and if you want to exit type exit")
#         a=input("Enter the sentence").encode().decode("unicode_escape")
#         if a.lower()=='exit':
#             break
#         else:
#             f.write(a+'\n')
#     print(f.read())
    
# with open('file1.txt','r') as f:
#     a=f.readlines()
#     b=''.join(a).strip().split()
#     print(b)\
    
with open('file1.txt','r') as f1, open('file2.txt','r') as f2:
    print(f1.read())
    print(f2.read())
    f1.close()
    f2.close()
    print(f1.read())