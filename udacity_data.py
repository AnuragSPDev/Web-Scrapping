import requests
from bs4 import BeautifulSoup as bs
import json
import traceback

try:
    url = requests.get('https://www.udacity.com/school-of-data-science', verify=False)
    url.raise_for_status()
    soup = bs(url.content, 'html.parser')
    try:
        data = soup.find('div', class_='upcoming-programs-list_layout__28HUd')
        # print(len(data))

        u_list = data.find('ul')

        main_di = {}
        i = 0
        for item in u_list.children:
            di = {}
            di['start_date'] =item.find_all('div')[0].find('time').get_text()
            di['heading'] = item.find_all('div')[1].find('h3').get_text()
            di['concepts'] = item.find_all('div')[1].find('p').get_text()
            main_di[i] = di
            i += 1

        with open('course_data.json', 'w') as fp:
            json.dump(main_di, fp, indent=4)
    except Exception as e:
        print('Exception Occurred')
        print('{}'.format(traceback.format_exc()))

# Connection error
except requests.ConnectionError as e:
    print('{}'.format(e))

# http status not OK
except requests.exceptions.HTTPError as e:
    print('{}'.format(e))

# invalis url
# except requests.exception.URLError as e:
#     print('{} - URL not found'.format(e))

# except requests.exceptions.RequestException as e:
#     print('{}'.format(e))