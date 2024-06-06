import os

root = '/home/awiros-tech/Documents/dogsvscats/'

# for (root,dirs,files) in os.walk(master_dir):
#   print("Directory path: %s" %root)
#   print("Directory Names: %s" %dirs)
#   for i in dirs:
#     print(root + '/' + i)
#   print("Files Names: %s"%files)




def yield_files(root):
  
    for root, dirs, files in os.walk(root):
        
        for filename in files:
            filename = os.path.join(root, filename)
            x=filename.split('/')
            t=x[6]
            
            if os.path.isfile(filename): 
                    file = open('/home/awiros-tech/Documents/list.txt','a')
                    file.write(filename)+file.write(","+ t + "\n") 
                    
yield_files(root)