# 1. open the file with fileName or give mode like read or write
f = open('H:\\python\\chapter 9\\sample.txt','r')   

# 2.define function of mode
# data = f.read()
data = f.read(8) #first 8 character read from the file

# 3.print the data
print(data)
# 4. last close the file 
f.close() 

