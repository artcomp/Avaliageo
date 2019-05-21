# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import re
import files

from polyglot.text import Text, Word

def parse_text_toponimo(blob_text):

	text = Text(blob_text)

	loc = ""
	data = []

	#gwt data
	for sent in text.sentences:
		#print(sent)
		for entity in sent.entities:
			#print(str(entity.tag))
			for x in entity:
				if len(entity) > 1:
					loc = loc+x+' '
				else:
					loc = x+' '

			if (loc.find(' - ') > 0):
				loc = loc.replace(' - ', '-')
			loc = loc[:-1]
			data.append((str(entity.tag),loc))
			loc = ""

	# encode to utf-8
	n_data = []
	for i in range(len(data)):
			n_data.append((data[i][0], data[i][1].encode("utf-8")))

	string_list = list()

	# select locations only
	for j in range(len(n_data)):
		if n_data[j][0] == "I-LOC":
			string_list.append(n_data[j][1])

	return string_list


def get_sentence(blob):
	text = Text(blob)
	s=""
	for sent in text.sentences:
		s=s+str(sent)+"\n"
	return s

def print_list(string_list):
	for st in string_list:
		print(st)


def parseTopToUser(strr):
	codecs = [
				('PCLI', '(País'), 
				('ADM1', '(Estado'),
				('ADM2', '(Distrito do Estado'),
				('PPLC', '(Capital do País'),
				('PPLA', '(Capital do Estado'),
				('AIRP', '(Aeroporto'),
				('PPL' , '(Cidade'),
				('RGN' , '(Região'),
				('CONT', '(Continente'),
				('LCTY', '(Local Menor,Misto ou Indefinido'),
				('DAM', '(Barreira Dáqua'),
				('BLDG', '(Prédio'),
				('AGRF','(Instalação Agrícola'),
				('ADM3', '(Distrito da Cidade'),
				('SCH', '(Escola'),
				('LK', '(Lago'),
				('OPRA', '(Casa de Ópera'),
				('AMTH','(Anfiteatro'),
				('PAL', '(Palácio'),
				('STM','(Fluxo de Água'),
				('RVN','(Ravina'),
				('VLC','(Vulcão'),
				('ISL','(Ilha'),
				('BNK','(Banco'),
				('SHOL','(Cardume'),
				('HLL','(Colina'),
				('AREA','(Área'),
				('INLT','(Passagem'),
				('STDM','(Estádio'),
				('UNIV','(Universidade'),
				('PRK','(Parque'),
				('PCLH','(Antiga Entidade Política'),
				('RSV','(Reserva'),
				('SWMP','(Pântano'),
				('BSNU','(Bacia'),
				('MTS','(Montanhas'),
				('MT','(Montanha')
				]

	all_country = files.getTupleCountries()
	
	string = " ".join(strr.split()[2:])
	b = string
	c = string
	for i in codecs:
		if i[0] in string:
			b = string.replace(string.split()[-3],i[1])

	for i in all_country:
		if i[0] == b.split()[-1]:
			c = b.replace(b.split()[-1], '/ '+i[1])

	d = c.replace('---',' ')
	e = d.replace("$$$"," - ")
	
	return e+')'


# nao pega os toponimos mas sim o resultado da consuta nos json
def insertDataIntoSelectTag(data):
	data_list = []
	option_1_to_5 = '<option value="5">5</option> <option value="4">4</option> <option value="3">3</option> <option value="2">2</option> <option value="1">1</option><option value="None" selected>None</option>  </select>'
	index_quest = 0
	string_option = ""
	string_select = ""
	name_select_in_text = "top_data_"
	option_select_in_text = "confi_data_"


	option_none_of_alternatives_and_dont_know = '''<option value="5 0000000 Nenhuma das Alternativas">Nenhuma das Alternativas</option> <option value="6 0000000 Não é um lugar">Não é um lugar</option> <option value="7 0000000 Não Sei">Não Sei</option> <option value="8 0000000 -- None --" selected>-- None --</option>'''

	for i in range(len(data)):
		string_select = string_select + '<select class="form-control style_select" name="'+ name_select_in_text + str(i)+'" id="'+name_select_in_text + str(i)+'">'
		for j in data[i]:
			string_option = string_option+'<option value="'+j+'">' + parseTopToUser(j) + '</option>'
		
		string_select = string_select + string_option+ option_none_of_alternatives_and_dont_know + '</select>'
		data_list.append('''<div class="collapse" id="quest_''' + str(index_quest) + '''"> <div class="well"> <div class="row"> <div style="margin: 0 auto;" class="text-center"><div class="col-md-1">Topônimo:</div> <div class="col-md-6">''' + string_select +''' </div> <div class="col-md-2">  Certeza da Resposta :</div> <div class="col-md-1">'''+ '''<select class="form-control style_select" name="''' +option_select_in_text+str(index_quest)+ '''">'''+option_1_to_5 +''' </div> <div class="col-md-2" style="justify-items: center;"><button class="btn btn-success style="margin-top:5px;" type="button" data-toggle="collapse" data-target="#quest_''' + str(index_quest) +''' " aria-expanded="false" aria-controls=quest_'''+ str(index_quest)+'''>Confirmar</button> ''' +  '''</div></div></div></div></div>''')
		index_quest = index_quest + 1
		
		string_option = ""
		string_select = ""
		
	return data_list

# 
def create_text_button(data):
	bt = []
	index = 0
	for i in data:# i remove aria-controls for test
		bt.append('''<button id="toponym_'''+str(index)+'''" onclick="submitButtonStyle(this)" style="font-size:1em;"class="btn style_toponym_in_text main_form" type="button" data-toggle="collapse" aria-expanded="false" >''' + i + '''</button>''')
		index = index + 1
	return bt

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced    
    i = 0
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString[i])
            i = i + 1
    return  mainString

def putButtonIndex(string):
	split_string =  string.split()
	index_toponimo = 0
	j = 0
	lista = []
	for i in split_string:
		if '<button' in i:
			i = i + ' data-target="#quest_'+ str(index_toponimo) +'" '
			lista.append((i,j))
			index_toponimo = index_toponimo + 1
		j = j + 1

	for i in range(len(lista)):
		split_string[lista[i][1]] = lista[i][0]

	return ' '.join(split_string)


def generate_paragraph(string):
	lista = string.split('\n')
	
	lista2 = []
	for x in range(len(lista)):
		lista2.append("<p>"+lista[x]+"</p>")

	sent = ""
	for x in lista2:
		sent = sent + x

	return sent


def keyToSort(item):
	return item[0]

def sortToponymOccurence(a,b):
	lista = []
	
	# encontra os indices de todos os toponimos no texto(na string)
	for x in b:
		indices_top = [m.start() for m in re.finditer(x, a)]
		lista.append((indices_top, x))
	
	tpn = []

	#add em tpn as repeticoes dos toponimos
	for k in lista:
		lenght = len(k[0])
		index_controle = 0
		while lenght>0:
			tpn.append((k[0][index_controle],k[1]))
			lenght = lenght - 1
			index_controle = index_controle + 1


	result = sorted(tpn, key=keyToSort)
	res = []
	for s in result:
		res.append(s[1])

	return res

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

def createSelectGroup(select_options, qtde_blocks):
	lista = list(chunks(select_options, qtde_blocks))

	ls = []
	string = ""
	for i in lista:
		string = ""
		for j in i:
			string = string + j
		ls.append(string)

	return ls


def intercalateLists(l1, l2):

	size_l1 = len(l1)
	size_l2 = len(l2)

	final = []

	if size_l1 >= size_l2:
		for i in range(len(l2)):
			final.append(l1[i])
			final.append(l2[i])
			i = i + 2

		i = size_l2
		for i in range(size_l2,size_l1):
			final.append(l1[i])

	else: 
		for i in range(len(l1)):
			final.append(l1[i])
			final.append(l2[i])
			i = i + 2

		i = size_l1
		for i in range(size_l1, size_l2):
			final.append(l2[i])

	return final

def generateText(text, select_option):

	qtd_of_blocks = len(select_option)/3


	index_of_paragraphs = [m.start() for m in re.finditer("</p><p>", text)]

	tam_fixo = int (len(index_of_paragraphs) / qtd_of_blocks)
	tam = tam_fixo

	ll = []

	for k in range(len(index_of_paragraphs)):
		if k == tam:
			ll.append(index_of_paragraphs[k])
			tam = tam + tam_fixo

	leen = len(index_of_paragraphs)
	plus1 = index_of_paragraphs[leen-1]
	ll.append(plus1)

	l_aux_2 = map(lambda x: x + 4, ll)
	l_aux_2.insert(0, 0)
	

	listaa = []

	j=1
	for i in range(len(l_aux_2)-1):
		listaa.append(text[l_aux_2[i]:l_aux_2[j]])
		j = j+1

	select_block_size = int(len(select_option)/qtd_of_blocks)
	new_select = createSelectGroup(select_option, select_block_size)
	final_text = intercalateLists(new_select,listaa)
	
	string = ""
	for i in final_text:
		string = string + i
		
	return string
