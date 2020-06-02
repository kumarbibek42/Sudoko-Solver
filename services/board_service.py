import requests
from bs4 import BeautifulSoup


def get_board(level):
    res = requests.get('https://nine.websudoku.com/?level={}'.format(level))
    print('Fetched Board')
    soup = BeautifulSoup(res.content, 'html.parser')
    ids = generate_element_ids()
    data_grid = [[0 for e in range(9)] for e in range(9)]
    soup_data = []
    for id in ids:
        soup_data.append(soup.find('input', id=id))
    for ind, element in enumerate(soup_data):
        x_index = ind // 9
        y_index = ind % 9
        try:
            data_grid[x_index][y_index] = int(element['value'])
        except Exception:
            pass
    return data_grid


def generate_element_ids():
    ids = []
    for i in range(9):
        for j in range(9):
            ids.append('f{}{}'.format(i, j))
    return ids
