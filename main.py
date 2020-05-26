import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("Particao_k3_c1_reduced.csv")

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