def run():
    my_list = [1, 2, "jesus", True, 5.6]
    my_dicts = {'firstname':"jesus", 'lastname':"piedrahita",}

    super_list = [
        {'firstname':"jesus", 'lastname':"piedrahita"},
        {'firstname':"mauricio", 'lastname':"piedrahita"},
        {'firstname':"jose", 'lastname':"piedrahita"},
        {'firstname':"alexander", 'lastname':"colorado"},
        {'firstname':"jorge", 'lastname':"becerra"}
    ]

    super_dict = {
        'natural_num':[1, 2, 3, 4, 5],
        'integer_num':[-0, -1, 0, 1, 2],
        'floating_num':[1.1, 1.0, 0.0, -0.1, -0.2] 
    }

    #for key, value in super_dict.items():
    #    print(key, value)

    for i in super_list:
        print(i)



if __name__ == '__main__':
    run()