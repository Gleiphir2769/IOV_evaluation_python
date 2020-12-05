import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('experiment_dataset.xlsx', sheet_name=0)
    data = df.values
    edge_set = set()
    user_set = set()
    for item in data:
        edge_set.add(item[5])
        user_set.add(item[6])
    print("the number of edge: ", len(edge_set))
    print("the number of user: ", len(user_set))
