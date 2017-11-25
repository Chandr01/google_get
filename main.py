import requests


def get_params(url):
    url = requests.get(url).json()

    return url


def counter(params):
    for i in params['results']:

        name = i['name']
        # location = i['geometry']['location']
        id_ = i['place_id']
        try:
            rating = i['rating']
            print(name, id_, rating)
            with open('tests.txt', 'a') as file:
                file.write('{},{},{} \n'.format(name, id_, rating))
        except:
            rating = 'NONE'
            print(name, id_, rating)
            with open('tests.txt', 'a') as file:
                file.write('{},{},{} \n'.format(name, id_, rating))


def main():
    zapros = 'стоматология'
    key = 'AIzaSyAz4lKlMpg8y2z17MkE72farW6jBd_Ufyo'
    # left_bottom = '55.70,37.54'
    # left_top = '55.79,37.54'
    # right_top = 55.913249, 37.827880
    params = {}
    count_a = 0
    for a in range(1, 30):
        count = 0
        for i in range(1, 100):
            l = 55.79 + count
            lat = 37.54 + count_a
            start_point = '{},{}'.format(l, lat)
            url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}&radius=500&keyword={}&key={}'.format(
                start_point, zapros, key)
            params = get_params(url)
            counter(params)
            print(params['error_message'])
            try:
                if params['error_message'] == 'You have exceeded your daily request quota for this API.':
                    print(count, count_a, 'Konec api')
                    break
            except:
                pass
            count -= 0.001
            print(count)
        try:
            if params['error_message'] == 'You have exceeded your daily request quota for this API.':
                print(count, count_a, 'Konec api')
                break
        except:
            pass
        count_a += 0.01


if __name__ == '__main__':
    main()
