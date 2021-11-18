# -*- coding: utf-8 -*-
"""
Created on 23-09-2021

@author: Hirtih Kumar C V
"""

import os
class _search:
    def search(Fname, directory):
        result = []
        for root, dirs, files in os.walk(directory):
            if Fname in files:
                result.append(os.path.join(root, Fname))
            print(result)
        if result == []:
            print("File '{0}' not found in directory '{1}'".format(Fname,directory))
        else:
            return result

    def Delete(Fname , directory):
        result = _search.search(Fname , directory)
        try:
            if os.path.isfile(result[0]):
                while True:
                    YN = str(input("Are you sure you want to delete the file '{0}'? ".format(Fname))).lower()
                    if not YN.isalpha():
                        print("Only strings are accepted. Please try again.")
                        continue
                    elif YN in ["y","yes"]:
                        os.remove(result[0])
                        print("The file '{0}' have been deleted successfully".format(Fname))
                        break
        except TypeError:
            pass
        else:
            print("'{0}' is not a file".format(Fname))
    
    def D_Calc(O_Path):
        Count = 0
        Ptr = len(O_Path) - 1
        while O_Path[Ptr] not in ["\\",":","//"]:
            Count += 1
            Ptr -= 1
        return O_Path[0:len(O_Path) - Count]
    
    def EXT_Calc(EXT):
        Count = 0
        Ptr = len(EXT) - 1
        while EXT[Ptr] not in ["."]:
            Count += 1
            Ptr -= 1
        return EXT[len(EXT) - Count - 1: len(EXT)]
    
    def Rename(Fname , directory):
        result = _search.search(Fname, directory)
        O_EXT = ""
        N_EXT = ""
        try:
            if os.path.isfile(result[0]):
                while True:
                    New_Name = input("Enter a new name for the file '{0}' (with extension):".format(Fname))
                    
                    Conc_Path = _search.D_Calc(result[0])
                    EXT_NPath = _search.EXT_Calc(New_Name)
                    EXT_OPath = _search.EXT_Calc(result[0])
                    O_EXT = EXT_OPath
                    N_EXT = EXT_NPath
                    while True:
                        if N_EXT == O_EXT:
                            os.rename(result[0], Conc_Path+New_Name)
                            print("The file '{0}' have been changed to '{1}' and is saved in the path'{2}'".format(Fname,New_Name,Conc_Path+New_Name))
                            break
                        elif N_EXT != O_EXT:
                            YN = str(input("Extensions are not matching '{0}' <-> '{1}'.Enter Yes to try again:".format(O_EXT,N_EXT))).lower()
                
                        if YN in ["yes","y"]:
                            continue
                        elif YN not in ["yes","y"]:
                            print("Your file name has not been changed.")
                            break
                        break
            else:
                print("'{0}' is not a file.".format(Fname))
        except TypeError:
            pass

class RW:
    def Write(Fname , directory):
        if Fname[len(Fname) - 4:len(Fname)] in [".txt"]:
            strings = input("start writing: ")
            while True:
            
                YN = str(input("Are you sure you want to save the file: ")).lower()
                if not YN.isalpha():
                    print("Enter Yes (OR) NO. Please try again.")
                    continue
                elif YN not in ["y","yes"]:
                    print("File '{0}' is not saved.".format(Fname))
                    break
                elif YN in ["y","yes"]:
                    FILE = directory+Fname
                    with open(FILE,"w") as f:
                        f.write(strings)
                    print("File '{0}' is saved in the path '{1}'".format(Fname,FILE))
                    break
                else:
                    print("File '{0}' is not saved.".format(Fname))
                    break
        else:
            print("Sorry only '.txt' file is supported.")
    
    def Read(Fname, directory):
        try:
            if Fname[len(Fname) - 4:len(Fname)] not in [".txt"]:
                print("Write and read method are fixed for .txt file type only. Please try again")
            else:
                FILE = directory + Fname
                with open(FILE,"r") as f:
                    print(f.read())
        except FileNotFoundError:
            print("File named '{0}' not found in the directory '{1}'".format(Fname,directory))

class E_Handler:
    def Name_Directory(Num):
        while True:
            try:
                letter = {1:"for",2:"of",3:"of",4:"of",5:"of"}
                Fname = input("Enter the name of the file(with extension): ")
                directory = input("Enter the directory {0} the file: ".format(letter.get(Num))).upper()
                if len(directory) == 2 and directory[0].isalpha() and directory[1] == ":":
                    return Fname , directory
                    break
            except ValueError:
                print("Entered a string OR special character. Only integers are accepted. Please try again.")
                continue
            except NameError:
                print("Entered a string OR special character. Only integers are accepted. Please try again.")
                continue
            except TypeError:
                print("Entered a string OR special character. Only integers are accepted. Please try again.")
                continue
            else:
                print("{0} is not a valid directory. Please try again.".format(directory))
                continue
    
    def Get():
        while True:
            try:
                Num = int(input("1.Write in file\n2.Read the file\n3.Search for file\n4.Delete file\n5.Rename file: "))
            except ValueError:
                print("Entered a string OR special character. Only integers are accepted. Please try again.")
                continue
            
            except NameError:
                print("Entered a string OR special character. Only integers are accepted. Please try again.")
                continue
            except TypeError:
                print("Entered a string OR special character. Only integers are accepted. Please try again.")
                continue
            if Num > 5:
                print("Option {0} not found. Please try again.".format(Num))
                continue
            else:
                return int(Num)
                break

if __name__ == "__main__":
    Num = E_Handler.Get()
    ND = E_Handler.Name_Directory(Num)
    if Num == 1:
        RW.Write(ND[0],ND[1])
    elif Num == 2:
        RW.Read(ND[0],ND[1])
    elif Num == 3:
        S_file = _search.search(ND[0],ND[1])
        try:
            print("Path for the file '{0}' is '{1}'".format(ND[0],S_file[0]))
        except TypeError:
            pass
    elif Num == 4:
        _search.Delete(ND[0],ND[1])
    elif Num == 5:
        _search.Rename(ND[0],ND[1])