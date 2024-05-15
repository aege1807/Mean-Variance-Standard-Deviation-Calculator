import numpy as np

def calculate(Hello_World):
    if (len(Hello_World) != 9):
        raise ValueError("List must contain nine numbers.")

    lista = np.array(Hello_World)    
    #Mean
    mean_row = [lista[0:3].mean(), lista[3:6].mean(), lista[6:9].mean()]
    mean_col = [lista[[0,3,6]].mean(), lista[[1,4,7]].mean(), lista[[2,5,8]].mean()]
    #Variance
    var_row = [lista[0:3].var(), lista[3:6].var(), lista[6:9].var()]
    var_col = [lista[[0,3,6]].var(), lista[[1,4,7]].var(), lista[[2,5,8]].var()]
    #Standard deviation
    std_row = [lista[0:3].std(), lista[3:6].std(), lista[6:9].std()]
    std_col = [lista[[0,3,6]].std(), lista[[1,4,7]].std(), lista[[2,5,8]].std()]
    #Max
    max_row = [lista[0:3].max(), lista[3:6].max(), lista[6:9].max()]
    max_col = [lista[[0,3,6]].max(), lista[[1,4,7]].max(), lista[[2,5,8]].max()]
    #min
    min_row = [lista[0:3].min(), lista[3:6].min(), lista[6:9].min()]
    min_col = [lista[[0,3,6]].min(), lista[[1,4,7]].min(), lista[[2,5,8]].min()]
    #sum
    sum_row = [lista[0:3].sum(), lista[3:6].sum(), lista[6:9].sum()]
    sum_col = [lista[[0,3,6]].sum(), lista[[1,4,7]].sum(), lista[[2,5,8]].sum()]    
    return {
        'mean': [mean_col, mean_row, lista.mean()],
        'variance': [var_col, var_row, lista.var()],
        'standard deviation': [std_col, std_row, lista.std()],
        'max': [max_col, max_row, lista.max()],
        'min': [min_col, min_row, lista.min()],
        'sum': [sum_col, sum_row, lista.sum()]
        }