import f_strings #when we import a module, it will run regardless wheather you invoke any function or not
if __name__ == '__main__': #this codition is putt in the file that is being imported, to stop the uncalled code from excuting.
    print(__name__) #__name__ is the name of place where code belong, if it belong in this very file then it is "__main__", but if it imported then it is the name of that imported file 
    #for example, if i import file A into file B , then the name of that imported code becomes B, not '__main__'.


