
## Seccção de imports
from collections import Counter
from sklearn.metrics import classification_report
from sklearn import metrics 
import numpy as np

## Secção de funções auxiliares

def distancia_euclidiana(x1, x2):
    """Calcula a distância euclidiana entre dois pontos x1 e x2"""
    dist=np.sqrt(np.sum(np.square(x1-x2)))
    return dist

def normaliza_dados(dados):
    """Implementa o método de normalização usando o Z-score"""
    media = np.mean(dados)

    desvio_padrao = np.std(dados)

    dados_normalizados=[]
    for dado in dados:
        dados_normalizados.append((dado - media)/desvio_padrao)
    return dados_normalizados
        

## Classe K-NN 

class KNN:
    def __init__ (self, k = 1, normalilzation_need = False):
        ## 1º vamos validar se k é um valor positivo, inteiro e maior que zero
        try:
            if not int(k) or k < 1 :
                raise TypeError("O valor de K deve positivo, maior que zero e inteiro")
            if normalilzation_need != True and normalilzation_need != False:
                raise TypeError("O valor de normalilzation_need deve True or False")
        except:
            print("Ocorreu um erro com ao validar os parametros de entrada. Valide que k é um valor inteiro maior ou igual a que 1 e que normalilzation_need é True ou False")


        self.k = k
        self.normalilzation_need = normalilzation_need

    def fit(self, dados, classes):
        """ Treinar os dados"""
        if self.normalilzation_need == True:  
            model = {'dados': np.array(normaliza_dados(dados)), "classes" : classes}
        else:
            model = {'dados': np.array(dados), "classes" : classes}
        
        self.model = model

    def predict(self, x_test):
        """Previsão dos dados"""
        distances = [distancia_euclidiana(x_test, self.model['dados'][x]) for x in range(self.model['dados'].shape[0])]
        index_min = np.argsort(distances)[:self.k]
        return Counter([self.model['classes'][i] for i in index_min]).most_common(1)[0][0]

    def confusion_matrix(self, y_test, y_pred):
        """Calcula a matriz de confusão"""
        classes_distintas = np.unique(y_test)

        confusion_matrix = np.zeros((len(classes_distintas), len(classes_distintas)))

        for i in range(len(classes_distintas)):
            for j in range(len(classes_distintas)):
                confusion_matrix[i, j] = np.sum((y_test == classes_distintas[i]) & (y_pred == classes_distintas[j]))
        
        print("Matriz de Confusão")
        print(confusion_matrix.astype(int))
    
    def recall_precision(self, y_test, y_pred):
        """Métricas de avaliação calculadas através dos resultados obtidos na matriz de confusão."""
        print(metrics.classification_report(y_test, y_pred))

   

