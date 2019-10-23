def test_register_data_normalize(data_list):
    file_name_path_list = map(lambda data_row: data_row[2:5], data_list) 
    return file_name_path_list

def test_normalize2(data_list):
    print("data_list:", data_list)
    file_name_path_list = map(lambda data: (data[0].upper(), data[1].lower(), data[2].strip()), data_list) 
    print("file_name_path_list:", list(file_name_path_list))


def test_lambda(data):
    func = lambda data: (data[0].upper(), data[1].lower(), data[2].strip())
    print(func(data))

if __name__ == "__main__":
    data_list = [
    ['1','2','3','4','5','6'],
    ['wr','kdks','kkkds','jdsfls','sDLSDF', 'DKLDFS,DKFKS']
    ]
    print("data_list:", data_list)
    data_list = test_register_data_normalize(data_list)
    test_normalize2(data_list)
    #test_lambda(['jdsfls','sDLSDF', 'DKL DFS,DKFKS'])
