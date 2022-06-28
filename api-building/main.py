from fastapi import FastAPI
import pickle
import pandas as pd
import json


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'rb')
    arquivo_lido = pickle.load(arquivo)
    return arquivo_lido


def criar_dicionario(arquivo_recomendacoes):
    print(arquivo_recomendacoes)
    print()

    df_dict = {
        'Title': [i for i in arquivo_recomendacoes['title']],
        'genres': [i for i in arquivo_recomendacoes['genres']],
        'total_de_votos': [i for i in arquivo_recomendacoes['total_de_votos']],
        'nota_media': [f'{i:.2f}' for i in arquivo_recomendacoes['nota_media']]
    }
    return df_dict


def separar_filmes(df_dict):
    filmes = []
    i = 0
    while (i < 10):
        dicionario = dict()
        dicionario['title'] = df_dict['Title'][i]
        dicionario['genres'] = df_dict['genres'][i]
        dicionario['total_de_votos'] = df_dict['total_de_votos'][i]
        dicionario['nota_media'] = df_dict['nota_media'][i]
        filmes.append(dicionario)
        i += 1
    return filmes
    

arquivo_recomendacoes = ler_arquivo('modelo-recomendacao/filmes_recomendados (1).pkl')

df_dict = criar_dicionario(arquivo_recomendacoes)
lista_dicionarios = separar_filmes(df_dict)

with open('data.json', 'w') as json_file:    
    json.dump(lista_dicionarios, json_file)
        

app = FastAPI()

@app.get("/filmes/recomendados")
def get_recomendados():
    return lista_dicionarios

