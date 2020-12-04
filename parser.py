import requests
#pip install requests
from bs4 import BeautifulSoup
#pip install BeautifulSoup
import csv
from datetime import datetime
from multiprocessing import Pool

#получение кода html - getting html-code
def get_html(url):
    r = requests.get(url) #объект Response
    return r.text

#ф-я для получения ссылок которые есть на страницу в ячейках таблиц
def get_all_links(html):
	soup = BeautifulSoup(html, 'lxml') #(html code, parser) парсер, которые используется системой
	#list of objects Soup, parameters are html-tags
	tds = soup.find('table', id = 'grid-data').find_all('td', class_='text-left')
	links = []
	for td in tds:
		a = td.find('a').get('href') #string
		link = 'http://dom.mingkh.ru/sverdlovskaya-oblast/ekaterinburg' + a
		links.append(link)	
	return links

#ф-я для транслита слов
def transliterate(name):
   # Слоаврь с заменами
    slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'cz','ш':'sh','щ':'scz','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ja', 'А':'a','Б':'b','В':'v','Г':'g','Д':'d','Е':'e','Ё':'e',
      'Ж':'zh','З':'z','И':'i','Й':'i','К':'k','Л':'l','М':'m','Н':'n',
      'О':'o','П':'p','Р':'r','С':'s','Т':'t','У':'u','Ф':'f','х':'h',
      'Ц':'c','Ч':'ch','Ш':'sh','Щ':'scz','Ъ':'','Ы':'y','Ь':'','Э':'e',
      'Ю':'u','Я':'ja',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e'}
    for key in slovar:
        name = name.replace(key, slovar[key])

    return name
    
#получение информации	
def get_page_data(html):
	#создание объекта Soup
	soup = BeautifulSoup(html, 'lxml')  #(html code, parser) парсер, которые используется системой
	try:
		dirty_data = soup.find('table', id = 'grid-data').find_all('td', class_='text-left').text.strip()
	except:
		dirty_data = ''
	#СОЗДАНИЕ СПЛИТОВ ДЛЯ РАЗДЕЛЕНИЯ ДАННЫХ НА ПЕРЕМЕННЫЕ	
	address = dirty_data.split()
	#добавление переменных в список
	data = {'name':var,
		'price':price} #словарь
	return data

# lib XlsxWriter
def export_to_excel(filename, data):
	workbook = xlsxwriter.Workbook(filename)
	worksheet = workbook.add_worksheet()
	#использование списка(кортеж), для заполнеия excel 
	field_names = ('Адрес','','','','')
	for i, var in enumerate(field_names):	
	fields = ('','','','','')
	for row,d in enumerate(data, start=1):
		for col, field in enumerate(fields):
			worksheet.write(row,col,d[field])			
		for teach in d['teachs']:
			col += 1
			worksheet.write(row,col,teach)
	#worksheet.write(row,col,'content')
	workbook.close()
	
'''   
def write_csv(data):
	with open('.csv','a') as f:
		#объект писателя
		writer = csv.writer(f)
		writer.writerow((data['name']),
				data['price'])
		print(data['name'], 'parsed')
'''	

def make_all(url):
	#export_to_excel(data.xlxs,get_page_data(get_html(url)))
	html = get_html(url)
	data = get_page_data (html)
	export_to_excel(data.xlxs,data)

def mail():
	start = datetime.now()
	url = 'http://dom.mingkh.ru/sverdlovskaya-oblast/ekaterinburg/#stats'
	#все сслыки
	all_links = get_all_links(get_html(url))
	#for index, url in enumerate(all_links):
	#	write_csv(get_page_data(get_html(url)))
	#	print(index)
	
	'''
	for index, url in enumerate(all_links):
		html = get_html(url)
		data = get_page_data (html)
		export_to_excel(data.xlxs,data)
		print (index)
	'''
	with Pool(40) as p:
		#map(function, list_)
		p.map(make_all,all_links)	
	end = datetime.now()
	total = end - start
	print(str(total))

#точка входа
if __name__ == '__main__':
  main()
