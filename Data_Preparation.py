import shutil
import os
import random as rd

def rmv_itens(original , exclude_list ) :
    for i in exclude_list :
        original.remove(i)
    return original
def Separate_Train_test( path_data_dir , test_rate = 0.2 ):# , not_consider_list = [] ):
    ark_names = os.listdir(path_data_dir)
    test_set  = rd.sample(ark_names , int(test_rate * len(ark_names)))
    rmv_itens(ark_names , test_set)
    try:
        os.makedirs(f"{path_data_dir}//Train")
        os.makedirs(f"{path_data_dir}//Test")
    except OSError:
        print("Ocorreu um erro ao criar as pastas")
    for f in ark_names :
        shutil.move(path_data_dir + f"//{f}" ,path_data_dir + f"//Train" )
    for f in test_set :
        shutil.move(path_data_dir + f"//{f}" ,path_data_dir + f"//Test" )

        

path_Dataset_base ="C://Users//limaa//PythonProjects//VsCodePython//Processo Seletivo Docket Brasil//Dataset"
path_simplest_rg  = path_Dataset_base + "//Simplest//RG"
path_simplest_cnh = path_Dataset_base + "//Simplest//CNH"
path_simplest_cpf = path_Dataset_base + "//Simplest//CPF"


path_in_use = path_simplest_cpf
rg_original = os.listdir(path_in_use)
# rg_original.remove("Train")
# rg_original.remove("Test")
# rg_down_Samples = rd.sample(rg_original ,  3)
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
    path = path_in_use + f"//{i}"
    ## If file exists, delete it ##
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:    ## Show an error ##
        print("Error: %s file not found" % path)"""

Separate_Train_test(path_in_use)