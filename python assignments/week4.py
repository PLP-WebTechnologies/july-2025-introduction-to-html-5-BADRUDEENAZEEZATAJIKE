#Openeing and writing a file
file=open("azeezatFile.pdf","w")
content=file.write("I am in week4 \n performing different operations on file \n Submitting and Pushing to github")
print(content)

#Reading  a file
file=open("azeezatFile.pdf","r")
content2=file.read()
print(content2)

#Exception handling
try:
    file=open("azeezatFile.pdf","r")
    content3=file.readline()
except FileNotFoundError:
    print('file not found, kindly recheck dear user')
finally:
    print('Thank you for viewing azeezatfile.pdf🖐️')

