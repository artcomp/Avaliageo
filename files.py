# -*- coding: utf-	8 -*-
import json
import collections
import statistics
import numpy 
#import ctypes
#import ast

def getNewsDataFromUrls():
    with open("preProssedNews/news.txt","r") as file:
        string = file.read();

    return json.loads(string)

def dataFromUser(title, data):
	path = title.replace(" ","-")
	full_path = "bases/"+path
	with open(full_path,"a+") as file:
		json_str = json.dumps(data, ensure_ascii=False).encode('utf8')+"@"
		file.write(json_str)
	return json_str


def readFile(title):
	path = title.replace(" ","-")
	full_path = "bases/"+path

	with open(full_path,"r") as file:
		string = file.read();
	return string

def printDataFromUser(data):
	for i in data:
		print i[0]
		for j in i[1]:
			print j[0], j[1]

def createDataList(string):
	data = string.split('@')
	del data[-1]
	l = []
	for i in data:
		l.append(eval(i))

	return l

def keyValue(item):
	return item[1]

def lprint(l):
	for i in l:
		print i

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]


def CronbachAlpha(itemscores):
    itemscores = numpy.asarray(itemscores)
    itemvars = itemscores.var(axis=1, ddof=1)
    tscores = itemscores.sum(axis=0)
    nitems = len(itemscores)

    return nitems / (nitems-1.) * (1 - itemvars.sum() / tscores.var(ddof=1))

def calculateAlpha(title):
	txt_l =  readFile(title)
	file_data_list = createDataList(txt_l)
	
	aux_l = []
	news = []
	hash_tops = []
	number_of_tops = len(file_data_list[0][0][1])

	for i in file_data_list:
		for j in i:
			for k in j[1]:
				aux_l.append(k[0])
	
	news = list(chunks(aux_l,number_of_tops))
	for i in news:
		hash_tops.append(list(map(lambda x: int(x.split()[0]), i)))

	return CronbachAlpha(hash_tops)

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(n))

def createDataList(string):
	data = string.split('@')
	del data[-1]
	l = []
	for i in data:
		l.append(eval(i))

	return l

def countUsers(title):
	read_f = readFile(title)
	file_data_list = createDataList(read_f)
	return len(file_data_list)

def groupData(title):
	txt_l =  readFile(title)
	file_data_list = createDataList(txt_l)
	number_of_tops = len(file_data_list[0][0][1])
	nl = []
	aux = []
	count = 0

	while count < number_of_tops:
		for i in file_data_list:
			aux.append(i[0][1][count])

		count = count + 1
	
	nl = list(split(aux, number_of_tops))

	return nl

def processData(title,url):
	
	minimum_value_to_accept_news = 2
	std_dev_to_accept = 10

	nl = groupData(title)
	l_aux = []
	aux_l = []
	mean_stddev = []
	info_top_to_carry = ""
	

	if len(nl[0]) < minimum_value_to_accept_news:
		return False

	# run all tops already grouped
	for i in nl:
		# print "-------"
		del l_aux[:]
		del aux_l[:]

		# sort most common top in all votes from users
		for j in i:
			l_aux.append(j[0])
		ctr = collections.Counter(l_aux).most_common(8)
		# print "Most Popular : ", ctr[0][1],"2nd : ", ctr[1][1]

		#verify if there are more then one 'most popular'
		if len(ctr) > 1:
			if ctr[0][1] <= ctr[1][1]:
				# print "return False"
				return False

		# run in all votes for a spacific top and calculate some descriptive statistics
		for j in i:
			if j[0] == ctr[0][0]:
				info_top_to_carry =  j[0]
				aux_l.append(int(j[1]))
		
		mea = statistics.mean(aux_l)
		std_dev = statistics.stdev(aux_l)

		# verify if std_dev is acceptable
		if std_dev > std_dev_to_accept:
			return False

		mean_stddev.append((info_top_to_carry,mea,std_dev))

	# print mean_stddev
	# VOLTAR AQUIIIIII ---------------------------------------------------------
 	return (1.0, mean_stddev)
	

def generateNewsJsonFiles(processData, tops, url,title):

	pd = processData[1]
	number_of_decimal_cases = 4

 	json_news = {
		"title" : "",
		"url" : "",
		"cronbach" : "",
		"number_of_voters" : 0,
		"toponyms" : []
	}

	json_news["title"] = title
	json_news["url"] = url
	json_news["cronbach"] = round(processData[0],4)
	json_news["number_of_voters"] = countUsers(title)

	js = {}

	for i in range(len(tops)):
		js = {
			"top_find_on_new" : "",
			"top_selected_by_user" : "" ,
			"toponym_geonamesId" : 0,
			"mean_confiability" : 0,
			"std_deviation" : 0
			
		}
		js["top_find_on_new"] = tops[i]
		
		if len(pd[i][0].split()[-2]) != 2:
			js["top_selected_by_user"] = " ".join(pd[i][0].split()[2:-2])
		else:
			js["top_selected_by_user"] = " ".join(pd[i][0].split()[2:-2])

		js["toponym_geonamesId"] = pd[i][0].split()[1]
		js["mean_confiability"] = round(float(pd[i][1]),number_of_decimal_cases)
		js["std_deviation"] = round(float(pd[i][2]),number_of_decimal_cases)

		json_news['toponyms'].append(js)

	# , ensure_ascii=False).encode('utf8'
	closed_news = json.dumps(json_news, sort_keys=False,indent=4, ensure_ascii=False).encode('utf8')


	path = title.replace(" ","-")
	full_path = "bases/"+path
	with open(full_path,"w+") as file:
		file.write(closed_news)

def commentsFromUser(data):
	_dict = dict()
	_dict['user_comment'] = data
	data_to_json = json.dumps(_dict, sort_keys=False,indent=4, ensure_ascii=False).encode('utf8')

	with open("userComments/comments.txt","a+") as file:
		file.write(data_to_json)


def getTupleCountries():
    tp = []
    with open("paises-gentilicos-google-maps.json", "r") as f:
        str = eval(f.read())
    for i in str:
        tp.append((i['sigla'],i['nome_pais']))
    
    return tp

def parse_state():
    tp = []
    with open("estados-cidades.json", "r") as f:
        str = json.loads(f.read())[0]
    for i in str['estados']:
        tp.append((i['sigla'],i['nome']))
    print (tp)





