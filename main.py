import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

def split_programs(programs):
  programs = programs[1:-1]
  return programs.split('-')

def count_qualis_occurances_for_program(dataframe):
  programs_dict = {}
  programs_list = []

  for i in dataframe.index:
    qualis = dataframe["qualis"][i]
    programs_list = split_programs(dataframe["programas"][i])
    for program in programs_list:
      if program in programs_dict:
        if qualis in programs_dict[program]:
          programs_dict[program][qualis] += 1
        else:
          programs_dict[program][qualis] = 1
      else:
        programs_dict[program] = {qualis : 1}
  return programs_dict

def dict_to_json(filename, dictionary):
  json_dict = json.dumps(dictionary)
  
  with open(filename, "w") as file:
    file.write(json_dict)

def dict_from_json(src):
  with open(src) as json_file:
    dictionary = json.load(json_file)

    return dictionary

dataframe = pd.read_csv("Particao_k3_c1_reduced.csv")
dictionary = count_qualis_occurances_for_program(dataframe)
dict_to_json("Particao_k3_c1_reduced.json", dictionary)

def plot_program(program):
	labels, values = zip(*program.items())
	total = sum(values)
	sizes = [qualis_count / total for qualis_count in values]
	fig1, ax1 = plt.subplots()
	ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
	ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
	plt.savefig('graph.png')

plot_program(dict_from_json("Particao_k3_c1_reduced.json")["23001011005P7"])

"""
programs_dict = dict_from_json("dict.json")
print(programs_dict)
"""

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