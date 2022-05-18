import shutil
import os
import random as rd

def rmv_itens(original , exclude_list ) :
    for i in exclude_list :
        original.remove(i)
    return original


path_Dataset_base ="C://Users//limaa//PythonProjects//VsCodePython//Processo Seletivo Docket Brasil//Dataset"
path_simplest_rg  = path_Dataset_base + "//Simplest//RG"

rg_original = os.listdir(path_simplest_rg)
# rg_original.remove("Train")
# rg_original.remove("Test")
rg_down_Samples = rd.sample(rg_original ,  3)
rmv_list = rd.sample(rg_original ,  55)
if "Train" in rmv_list :
    rmv_list += rd.sample(rg_original ,  1)
    rmv_list.remove("Train")
if "Test" in rmv_list :
    rmv_list += rd.sample(rg_original , 1)
    rmv_list.remove("Test")
# rmv_list += ["Train" , "Test"]

rmv_itens(rg_original , rmv_list )

print(len(rmv_list))
print(len(rg_original))#rg_original)

"""#REMOVE ARQUIVOS PARA FAZER O BALANCIAMENTO
for i in rmv_list :
    path = path_simplest_rg + f"//{i}"
    ## If file exists, delete it ##
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:    ## Show an error ##
        print("Error: %s file not found" % path)"""

