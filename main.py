import requests
import xlsxwriter

number = 35
url = f'http://numbersapi.com/{number}'
# делаем гет запрос с аргументом url
response = requests.get(url)


# открываем новый файл на запись
workbook = xlsxwriter.Workbook('/Users/fishart/Documents/python/api_request_write_xlsx/numbers.xlsx')
# создаем там "лист"
worksheet = workbook.add_worksheet()
# записываем данные в ячейку
worksheet.write('A1', 'status code')
worksheet.write('A2', f'{response.status_code}')
worksheet.write('B1', 'response text')
worksheet.write('B2', f'{response.text}')
worksheet.write('C1', 'headers')
worksheet.write('C2', f'{response.headers}')
worksheet.write('D1', 'json')
worksheet.write('D2', f'{response.json}')
# сохраняем и закрываем
workbook.close()

print('Done.')
