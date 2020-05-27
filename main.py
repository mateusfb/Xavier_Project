import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

def split_programs(programs, n_programs):
  programs_list = []
  j = 1

  for i in range(0, int(n_programs)):
    programs_list.append(programs[j:j+13])
    j += 14

  return programs_list

def count_qualis_occurances_for_program(dataframe):
  programs_dict = {}
  programs_list = []

  for i in dataframe.index:
    qualis = dataframe["qualis"][i]
    programs_list = split_programs(dataframe["programas"][i], dataframe["prog._qtd"][i])
    for program in programs_list:
      if program in programs_dict:
        if qualis in programs_dict[program]:
          programs_dict[program][qualis] += 1
        else:
          programs_dict[program][qualis] = 1
      else:
        programs_dict[program] = {}

  return programs_dict

def dict_to_json(dictionary):
  json_dict = json.dumps(dictionary)
  
  with open("dict.json", "w") as file:
    file.write(json_dict)

def dict_from_json(src):
  with open(src) as json_file:
    dictionary = json.load(json_file)

    return dictionary

programs_dict = dict_from_json("dict.json")
print(programs_dict)

"""
pegue uma linha
para x em programas {
	verifique se x é uma chave no dicionario(true){
		verificar se o qualis está no dicionario do programa(true){
			adicionar um ao valor da chave do qualis
		} else {
			adicionar a chave ao dicionario e setar 1
		}
	} se não {
		adiciona o programa com um dicionario vazio
	}
}
"""