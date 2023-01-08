import os

srcpath = '/Users/mahendran/Downloads/TRIAL1'
destpath = '/Users/mahendran/Downloads/TRIAL'
files = os.listdir(srcpath)
renamedfilelist = open("renamedfilelist.txt","w")
i=1

for index, srcfile in enumerate(files):
     print(index)
     print(srcfile)

     file_name, file_extension = os.path.splitext(srcfile)
     print(file_name)
     print(file_extension)
     
     counter=str(i)
     i = i+1
     destfile = ''.join([counter,file_extension]);
     os.rename(os.path.join(srcpath, srcfile), os.path.join(destpath, destfile)) 
     str1=','.join([srcfile,destfile])
     str1 = str1 + '\n'
     renamedfilelist.write(str1)
