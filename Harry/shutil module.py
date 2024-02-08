import shutil

shutil.copy('sourse/of/file', 'destination/of/file') #to copy a file fom one place to other
shutil.copy2('sourse/of/file', 'destination/of/file') #to copy a file fom one place to other while preserving the metadata
shutil.move('sourse/of/file', 'destination/of/file') #to move file from one place to other, can be used to remane
shutil.copytree('sourse/of/file', 'destination/of/file') # to copy a whole folder
shutil.rmtree('destination/of/file') #to delete a folder 

#we cannot delete a file with it, for that we have to use os module



