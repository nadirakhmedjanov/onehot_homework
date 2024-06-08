import random
import pandas as pd

# Генерация исходного DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot кодирования
unique_values = list(set(lst))
one_hot_dict = {val: [1 if x == val else 0 for x in lst] for val in unique_values}
one_hot_df = pd.DataFrame(one_hot_dict)

# Переименовываем колонки, чтобы они соответствовали значениям в lst
one_hot_df.columns = ['is_' + col for col in one_hot_df.columns]

# Выводим первые несколько строк
print(one_hot_df.head(20))
