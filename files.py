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
	path = title.replace(" ","_")
	full_path = "bases/"+path+".txt"
	with open(full_path,"a+") as file:
		json_str = json.dumps(data, ensure_ascii=False).encode('utf8')+"@"
		file.write(json_str)
	return json_str


def readFile(title):
	path = title.replace(" ","_")
	full_path = "bases/"+path+".txt"

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

    si = itemvars.sum()
    st = tscores.var(ddof=1)

    print si
    print st
    
    print nitems / (nitems-1.) * (1 - si / st)
    return nitems / (nitems-1.) * (1 - si / st)

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

	nl = groupData(title)
	l_aux = []
	aux_l = []
	mean_stddev = []
	info_top_to_carry = ""
	
	# run all tops already grouped
	for i in nl:
		# print "-------"
		del l_aux[:]
		del aux_l[:]

		# sort most common top in all votes from users
		for j in i:
			l_aux.append(j[0])
		ctr = collections.Counter(l_aux).most_common(8)
		

		#verify if there are more then one 'most popular'
		if len(ctr) > 1:
			if ctr[0][1] <= ctr[1][1]:
				print ctr[0][1], ctr[1][1]
				print "return False"
				return False

		# run in all votes for a spacific top and calculate some descriptive statistics
		for j in i:
			
			if j[0] == ctr[0][0]:
				
				info_top_to_carry =  j[0]
				
				
				if 'None' in j[1] :
					aux_l.append(int(3))
				else:
					aux_l.append(int(j[1]))
		
		mea = statistics.mean(aux_l)
		std_dev = statistics.stdev(aux_l)

		
		mean_stddev.append((info_top_to_carry,mea,std_dev))

	# VOLTAR AQUIIIIII ---------------------------------------------------------
 	return (calculateAlpha(title), mean_stddev)
	

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

	print closed_news

	path = title.replace(" ","_")
	full_path = 'closedBases/'+path+'.txt'
	print full_path
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



l = [

	'Amazon_libera_ferramentas_da_Alexa_para_desenvolvedores_brasileiros_',
	'''Após_jantar_com_Bolsonaro,_CNA_diz_que_'mal-entendido'_com_países_islâmicos_é_'página_virada'_''',
	'''Avianca_Brasil_pede_suspensão_de_liminar_para_evitar_retomada_de_aviões_''',
	'BCE_mantém_política_monetária_',
	'''Câmara_de_BH_aprova_em_1º_turno_projeto_que_autoriza_botão_de_pânico_em_escolas_''',
	'''Carrefour_cortará_mais_de_1_mil_empregos_na_França,_diz_sindicato_''',
	'Eletrobras_anuncia_conclusão_de_venda_da_Amazonas_Energia_',
	'Em_avanço,_China_promete_maior_abertura_a_empresas_da_União_Europeia_',
	'Ex-presidente_do_BB_e_da_Petrobras_Aldemir_Bendine_deixa_prisão_após_decisão_do_STF_',
	'Funcionários_são_atropelados_por_ex-patrão_após_audiência_trabalhista_em_MG_',
	'Homem_é_suspeito_de_matar_mulher_em_Belo_Horizonte_',
	'IPVA_2019_em_MG:_prazo_para_pagar_3ª_parcela_termina_quarta_',
	'JBS_faz_recall_de_20_toneladas_de_carne_moída_por_contaminação_com_plástico_nos_EUA_',
	'Justiça_Federal_bloqueia_bens_do_ex-governador_Marcelo_Miranda_para_pagar_custos_da_eleição_suplementar_',
	'Mais_de_600_raios_atingem_a_Grande_SP_durante_temporal_no_domingo_',
	'Mega-Sena,_concurso_2.141__ninguém_acerta_as_seis_dezenas_e_prêmio_vai_a_R$_45_milhões_',
	'Operação_investiga_grupo_que_desviou_mais_de_R$_800_mil_de_clientes_de_bancos_do_DF_',
	'Polícia_investiga_morte_de_jovem_de_18_anos_com_oito_tiros_na_Baixada_Fluminense_',
	'Príncipe_Harry_vai_a_evento_sem_Meghan,_que_reduz_agenda_por_causa_da_gravidez_',
	'Verão_2019_foi_o_5º_mais_quente_da_história_em_SP;_outono_terá_temperaturas_pouco_acima_da_média_',

]

calculateAlpha(l[11])