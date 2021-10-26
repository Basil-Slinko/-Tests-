import requests


TOKEN_YA_DISK = ''
FOLDER_PATH = 'New_folder_1'


def create_a_folder():
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {TOKEN_YA_DISK}'
        }
    params = {"path": f'{FOLDER_PATH}'}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code


if __name__ == '__main__':
    create_a_folder()
