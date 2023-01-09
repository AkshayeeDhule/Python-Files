'''
writing into file
================
write(): This function is used to write data into file.

syntax:

    file_pointer.write(data)



      data.txt                         write_file.py
  ----------------                -----------------------
                      write()
                   <-------------

'''

fp=open('data.txt','w')
#d="This is first line in the file"

#fp.write(d)
#fp.close()
mn=input("Enter Mobile Number :")#9898989898
fp.write(mn)
fp.close()

