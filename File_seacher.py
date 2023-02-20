import os
import shutil

class File_find():
    def __init__(self,root,name,**kwargs):
        self.file_list=[]
        self.root=root
        self.name=name
        self.args=kwargs

    def file_seacher(self,rootdir,name):
        dirlist=os.listdir(rootdir)
        for file in dirlist:
            path=rootdir+'\\'+file
            if os.path.isdir(path)!=True: #不是文件夹
                if file.find(name)>=0: #包含查找的名称
                    self.file_list.append(rootdir+'\\'+file)
            else: #是文件夹
                self.file_seacher(path,name) 
        return 0
        
    def file_copy(self,dirlist,copydir):
        for i in dirlist:
            if i!=None:
                shutil.copy(i,copydir)
        return 0   
      
    def run(self):
        self.file_seacher(self.root,self.name)
        print('文件地址：')
        print(self.file_list)
        if self.args :
            copydir='C:\\Users\\mader\\Desktop\\test'
            self.file_copy(self.file_list,copydir)
        
if __name__ == "__main__":
    
    root='D:\\论文及学习'
    name='opt'
    iscopy=True
    File_find(root,name,copy=True).run()




