DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'HÃ©ctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    all_platzi_devs = [workers['name'] for workers in DATA if workers['organization'] == 'Platzi']
    all_ages_devs = list(filter(lambda worker: worker['age'] > 18, DATA))
    all_name_age = list(map(lambda worker: worker['name'], all_ages_devs))
    age_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    age_people = list(map(lambda worker: worker['old'] , age_people))
    all_python_devs_filter = list(filter(lambda workers: workers['language'] == 'python', DATA))
    all_python_devs_map = list(map(lambda workers: workers['name'], all_python_devs_filter))
    organization_platzi = list(filter(lambda workers: workers['organization'] == 'Platzi', DATA))
    organization_platzi = list(map(lambda workers: workers['name'], organization_platzi))
    list_age = [worker['name'] for worker in DATA if worker['age'] > 18]
    list_old = [worker | {'old': worker['age'] > 70} for worker in DATA]

    for worker in list_old:
        print(worker)


if __name__ == '__main__':
    run()