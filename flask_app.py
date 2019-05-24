# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import scrap
import random
import files

from flask import request, Flask, render_template, url_for, redirect

app = Flask(__name__)

urls = files.getNewsDataFromUrls()

len_urls_available = len(urls)
toponyms = []
user_data = []
data_to_store = []
random_news = 0
title = ""
gen_data = []
noticia = ""
random_news_sorted = []
#=====

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/avaliar', methods=['POST','GET'])
def avaliar():
	global toponyms
	global user_data
	global random_news
	global data_to_store
	global title
	global gen_data
	global noticia
	global random_news_sorted
	global aux_data_to_store_firebase
	global aux_file_name

	if request.method == 'POST':
		i=0
		qt_of_tops = len(toponyms)
	
		while qt_of_tops > 0:
			top = request.form.get('top_data_'+str(i))
			conf = request.form.get('confi_data_'+str(i))
			i = i+1
			qt_of_tops = qt_of_tops - 1
			if top is not None:
				if conf is not None:
					user_data.append((top,conf))

		data_to_store.append((urls[random_news][0], user_data))
		aux_data_to_store_firebase = files.dataFromUser(title, data_to_store)
		aux_file_name = title.replace(" ","_")
		
		# data_to_create_json = files.processData(title, urls[random_news][0])
		# #if news is closed then write into a file
		# if data_to_create_json != False:
		# 	files.generateNewsJsonFiles(data_to_create_json, toponyms, urls[random_news][0],title)

		
		del data_to_store[:]
		# limpa os dados, para nao acc 
		del user_data[:]

		if request.form['submit_button'] == 'Do Something':
			if len(random_news_sorted) == len(urls):
				del random_news_sorted[:]	            

			random_news = random.randint(0,(len_urls_available-1)) 
			while random_news in random_news_sorted:
				random_news = random.randint(0,(len_urls_available-1))
			random_news_sorted.append(random_news)

			url = urls[random_news][0]
			gen_data = urls[random_news][1]
			noticia = gen_data[0]
			toponyms = gen_data[1]
			title = scrap.getTitle(url)

			return render_template("avaliar.html", title=title, noticia=noticia, firebase=aux_data_to_store_firebase, firebase_filename=aux_file_name)

		elif request.form['submit_button'] == 'Do Something Else':
			return render_template("validar.html",firebase=aux_data_to_store_firebase, firebase_filename=aux_file_name)

	if request.method == 'GET':
		if len(random_news_sorted) == len(urls):
			del random_news_sorted[:]

		random_news = random.randint(0,(len_urls_available-1)) 
		while random_news in random_news_sorted:
			random_news = random.randint(0,(len_urls_available-1))
		random_news_sorted.append(random_news)

		url = urls[random_news][0]
		gen_data = urls[random_news][1]
		noticia = gen_data[0]
		toponyms = gen_data[1]
		title = scrap.getTitle(url)

		return render_template("avaliar.html", title=title, noticia=noticia)

@app.route('/validar', methods=['post','get'])
def validar():

	if request.method == "POST":
		user_data = request.form.get('comments')
		files.commentsFromUser(user_data)
		user_data = user_data+"$$$$$$$$$"
		return render_template('index.html',user_data=user_data)

	elif request.method == "GET":
		return render_template("validar.html")

if __name__ == '__main__':
	app.run(debug=True)
