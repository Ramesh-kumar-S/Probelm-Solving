import pickle

def save_dict(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)
        print(f'Successfully serialized the data.')

def load_dict(path):
    with open(path, "rb") as f:
        data=pickle.load(f)
        print(f'De-Serialized Data : {data} to {type(dict)}')

save_dict({1: 'a', 2: 'b', 3: 'c'}, "Data.pickle")
load_dict("Data.pickle")