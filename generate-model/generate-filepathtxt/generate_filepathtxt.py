
str_0 = ''
path = './anger/'
extention = '.png\n'

fileNum = 3000

for i in range(fileNum):
    str_0 += path + str(i+1) + extention

path = './contempt/'
for i in range(fileNum):
    str_0 += path + str(i+1) + extention

path = './disgust/'
for i in range(fileNum):
    str_0 += path + str(i+1) + extention

path = './fear/'
for i in range(fileNum):
    str_0 += path + str(i+1) + extention

path = './happiness/'
for i in range(fileNum):
    str_0 += path + str(i+1) + extention

path = './neutral/'
for i in range(fileNum):
    str_0 += path + str(i+1) + extention

path = './sadness/'
for i in range(fileNum):
    str_0 += path + str(i+1) + extention

path = './surprise/'
for i in range(fileNum):
    str_0 += path + str(i+1) + extention

f = open('filepath.txt', 'w')
f.write(str_0)

f.close()