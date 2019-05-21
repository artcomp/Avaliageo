# -*- coding: utf-8 -*-
import re
import itertools
import random
from itertools import groupby
import collections
import statistics
import numpy 
import ctypes
import json


string = ''' Por G1 DF e TV Globo
12/03/2019 08h10    Atualizado  2019-03-12T14:52:18.586Z
Duas pessoas morrem em acidente entre um ônibus escolar e um carro no DF
Um acidente entre um carro e um ônibus escolar em um trecho da BR-251, que passa pelo <button class="btn style_toponym_in_text" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">Distrito Federal</button>, deixou dois mortos e 16 feridos na manhã desta terça-feira (12).
A batida ocorreu no PAD-DF, região do <button class="btn style_toponym_in_text" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">Paranoá</button>.
Carla Machado da Silva Lemos, 40 anos, e Rosimeire Rodrigues da Silva, 32 anos, que estavam no carro com placa de <button class="btn style_toponym_in_text" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">Unai</button> (<button class="btn style_toponym_in_text" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">MG</button>) morreram na hora, segundo os bombeiros.
 '''

texto = ''' Por G1 SP 

  13/03/2019 11h56    Atualizado  2019-03-13T17:29:45.577Z    

 "A cena mais triste que eu já assisti em toda a minha vida", diz João Dória 

 O governador João Doria (PSDB) visitou a Escola Estadual Raul Brasil, em Suzano, na Grande São Paulo, onde dois assassinos mataram oito pessoas na manhã desta quarta-feira (13). A dupla comete suicídio em seguida. 

 "Foi a cena mais triste que assisti em toda a minha vida", disse o governador. "Fiquei consternado, chocado com o que vi aqui. Nunca tinha visto uma cena igual em toda a minha vida. Então a minha solidariedade a essas famílias. De todos, aos que estão feridos também." 

 Doria cancelou as agendas da tarde e seguiu de helicóptero até a escola, acompanhado dos secretários da Educação, Rossieli Soares, da Segurança, general João Camilo Pires de Campos, e do comandante da Polícia Militar, coronel Marcelo Vieira Salles. 

 Movimentação em frente à escola Raul Brasil, onde atiradores mataram 5 alunos e 1 funcionário — Foto: Reprodução/TV Globo 

 O governador decretou luto oficial de três dias em todo o estado. “Determinei que a secretaria de saúde pudesse enviar aqui para o atendimento às famílias estrutura psicológica e na mobilização dos hospitais. Houve um rápido atendimento para remoção dos feridos aos hospitais”, disse, acrescentando que a Polícia Militar chegou em oito minutos. 

 “Às vítimas, aos pais dessas crianças, aos familiares dessas duas funcionárias da escola, e também aos pais e familiares dos dois homicidas, a nossa solidariedade”, disse Doria. 

 Segundo o Censo Escolar de 2017, a Escola Estadual Raul Brasil possui 358 alunos da segunda etapa do fundamental (6º ao 9º ano) e 693 estudantes do ensino médio. Ela ocupa um quarteirão inteiro na região central da cidade. Lá também funciona um centro de línguas estrangeiras. 

 Arte - ataque a escola em Suzano (SP) — Foto: Juliane Monteiro e Rodrigo Cunha/G1 


Massacre em escola deixa 10 mortos



Vídeo mostra desespero de alunos



Merendeira diz que audou a esconder 50 alunos na cozinha



Quem são os assassinos



Quem são as vítimas



Vídeo mostra assassinos entrando e atirando na escola



'Cena mais triste que assisti em toda a minha vida', diz governador



Cronologia do massacre na escola



Assassino postou fotos com arma minutos antes



Cadernos dos assassinos tinham táticas de jogos de combate



O que se sabe até agora



Ataques em escolas no Brasil



Repercussão nacional



Repercussão internacional



O massacre em Suzano em VÍDEOS



O massacre em Suzano em FOTOS

'''

def putButtonIndex(string):
	split_string =  string.split()
	index_toponimo = 0
	j = 0
	lista = []
	for i in split_string:
		if '<button' in i:
			i = i + ' data-target="quest_'+ str(index_toponimo) +'" '
			lista.append((i,j))
			index_toponimo = index_toponimo + 1
		j = j + 1

	for i in range(len(lista)):
		split_string[lista[i][1]] = lista[i][0]

	return ' '.join(split_string)


# l = ["aaa", "ccc", "bbb", "ddd"]

# # texto = "some bbb then ddd and, at least aaa but no ccc aaa"
# # top = []


def foo(text, tops):
	l = []
	for i in tops:
		if i in text:
			l.append(i)
	return l


def putToponymsInOrder(text, toponym_detected):
	top = []

	for x in text.split():
		if x in toponym_detected:
			top.append(x)
	
	return top

#print foo("some bbb then ddd and, at least aaa but no ccc aaa",["aaa", "ccc", "bbb", "ddd"])


def removeBlankSpace(lista):
	l = []
	for x in lista:
		k = x.replace(" ", "-")
		l.append(k)
	return l


tp = ["SP", "Brasil", "Suzano", "Campos", "São Paulo", "SP"]






def keyToSort(item):
	return item[0]

def sortToponymOccurence(a,b):
	lista = []
	
	# encontra os indices de todos os toponimos no texto(na string)
	for x in b:
		indices_top = [m.start() for m in re.finditer(x, a)]
		lista.append((indices_top, x))
	
	tpn = []

	#add em tpn as repetições dos toponimos
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

texto = '''Por G1 SP </p><p> 13/03/2019 11h56 Atualizado 2019-03-14T23:31:59.272Z </p><p> "A cena mais triste que eu já assisti em toda a minha vida", diz João Dória </p><p> O governador João Doria (PSDB) visitou a Escola Estadual Raul <button data-target="#quest_0"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Brasil</button>, em <button data-target="#quest_1"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Suzano</button>, na Grande <button data-target="#quest_2"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">São Paulo</button>, onde dois assassinos mataram oito pessoas na manhã desta quarta-feira (13). A dupla comete suicídio em seguida. </p><p> "Foi a cena mais triste que assisti em toda a minha vida", disse o governador. "Fiquei consternado, chocado com o que vi aqui. Nunca tinha visto uma cena igual em toda a minha vida. Então a minha solidariedade a essas famílias. De todos, aos que estão feridos também." </p><p> Doria cancelou as agendas da tarde e seguiu de helicóptero até a escola, acompanhado dos secretários da Educação, Rossieli Soares, da Segurança, general João Camilo Pires de <button data-target="#quest_3"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Campos</button>, e do comandante da Polícia Militar, coronel Marcelo Vieira Salles. </p><p> Movimentação em frente à escola Raul <button data-target="#quest_4"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Brasil</button>, onde atiradores mataram 5 alunos e 1 funcionário — Foto: Reprodução/TV Globo </p><p> O governador decretou luto oficial de três dias em todo o estado. “Determinei que a secretaria de saúde pudesse enviar aqui para o atendimento às famílias estrutura psicológica e na mobilização dos hospitais. Houve um rápido atendimento para remoção dos feridos aos hospitais”, disse, acrescentando que a Polícia Militar chegou em oito minutos. </p><p> “Às vítimas, aos pais dessas crianças, aos familiares dessas duas funcionárias da escola, e também aos pais e familiares dos dois homicidas, a nossa solidariedade”, disse Doria. </p><p> Segundo o Censo Escolar de 2017, a Escola Estadual Raul <button data-target="#quest_5"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Brasil</button> possui 358 alunos da segunda etapa do fundamental (6º ao 9º ano) e 693 estudantes do ensino médio. Ela ocupa um quarteirão inteiro na região central da cidade. Lá também funciona um centro de línguas estrangeiras. </p><p> Massacre em escola deixa 10 mortos </p><p> Vídeo mostra desespero de alunos </p><p> Quem são os assassinos </p><p> Quem são as vítimas </p><p> Vítimas são veladas em <button data-target="#quest_6"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Suzano</button> </p><p> Vídeo mostra assassinos entrando e atirando na escola </p><p> 'Cena mais triste que assisti em toda a minha vida', diz governador </p><p> Cronologia do massacre na escola </p><p> O que se sabe até agora </p><p> Ataques em escolas no <button data-target="#quest_7"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Brasil</button> </p><p> O massacre em <button data-target="#quest_8"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Suzano</button> em VÍDEOS </p><p> O massacre em <button data-target="#quest_9"  class="btn style_toponym_in_text" type="button" data-toggle="collapse" aria-expanded="false" aria-controls="collapseExample">Suzano</button> em FOTOS </p><p>
'''

l = [10, 71, 158, 882, 1163, 1594, 1898, 2266, 2461, 2920, 2963, 3005, 3037, 3067, 3273, 3336, 3412, 3453, 3486, 3689, 3895, 4099]

tam_fixo = int (len(l) / 5)
tam = tam_fixo

ll = []

for k in range(len(l)):
	if k == tam:
		ll.append(l[k])
		tam = tam + tam_fixo

l_aux_2 = map(lambda x: x + 4, ll)
l_aux_2.insert(0, 0)

listaa = []

j=1
for i in range(len(l_aux_2)-1):
	listaa.append(texto[l_aux_2[i]:l_aux_2[j]])
	j = j+1



# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

#print list(chunks([1,2,3,4,5,6,7,8], 3))

def createSelectGroup(select_options, qtde_blocks):
	lista = list(chunks(select_options), qtde_blocks)

	ls = []
	string = ""
	for i in lista:
		string = ""
		for j in i:
			string = string + j
		ls.append(string)

	return ls
		

def concat_lists(list1,list2):
	result = [None]*(len(list1)+len(list2))
	result[::2] = list1
	result[1::2] = list2
	return result


def intercala_listas(a, b):
    c = list(zip(a, b))
    return [elt for sublist in c for elt in sublist]



urls = [
	['https://g1.globo.com/sp/mogi-das-cruzes-suzano/noticia/2019/03/13/cena-mais-triste-que-assisti-em-toda-a-minha-vida-diz-doria-sobre-ataque-em-escola-em-suzano.ghtml',""],
	['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml',""],
	['https://g1.globo.com/economia/noticia/2019/03/28/carrefour-cortara-mais-de-1-mil-empregos-na-franca-diz-sindicato.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/22/homem-e-suspeito-de-matar-mulher-em-belo-horizonte.ghtml',""],
	['https://g1.globo.com/natureza/noticia/2019/03/28/como-a-alemanha-faz-para-evitar-que-animais-vivam-abandonados-nas-ruas.ghtml',""],
	['https://g1.globo.com/sc/santa-catarina/noticia/2019/04/02/carga-de-cocaina-e-apreendida-no-porto-de-navegantes.ghtml',""],
	['https://g1.globo.com/pe/pernambuco/noticia/2019/04/06/casal-e-agredido-com-facadas-durante-tentativa-de-assalto.ghtml',""],
	['https://g1.globo.com/pe/pernambuco/noticia/2019/04/05/reducao-de-atendimento-no-expresso-cidadao-de-olinda-causa-transtornos-para-a-populacao.ghtml',""],
	['https://g1.globo.com/go/goias/noticia/2019/04/07/alunos-de-goiania-desenvolvem-robo-para-torneio-internacional-nos-estados-unidos.ghtml',""],
	['https://g1.globo.com/pr/norte-noroeste/noticia/2019/04/08/londrina-recebe-doses-da-vacina-contra-gripe-campanha-comeca-nesta-quarta-feira-10.ghtml',""],
	['https://g1.globo.com/mundo/noticia/2018/10/21/principe-harry-vai-a-evento-sem-meghan-que-reduz-agenda-por-causa-da-gravidez.ghtml',""],
	['https://g1.globo.com/sp/vale-do-paraiba-regiao/noticia/2019/04/05/ministro-diz-que-preservacao-ambiental-nao-pode-ser-uma-agenda-do-bom-mocismo.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/03/onu-lanca-em-sp-plataforma-online-que-auxilia-empresas-na-contratacao-de-refugiados-no-brasil.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/03/20/verao-2019-foi-o-5o-mais-quente-da-historia-outono-tera-temperaturas-pouco-acima-da-media.ghtml',""],
	['https://g1.globo.com/rj/rio-de-janeiro/noticia/2019/03/20/policia-investiga-morte-de-jovem-de-18-anos-com-oito-tiros-na-baixada-fluminense.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/ipva-2019-em-mg-prazo-para-pagar-3a-parcela-termina-quarta.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/camara-de-bh-aprova-em-1o-turno-projeto-que-autoriza-botao-de-panico-em-escolas.ghtml',""],
	['https://g1.globo.com/df/distrito-federal/noticia/2019/04/05/operacao-investiga-grupo-que-desviou-mais-de-r-800-mil-de-clientes-do-bando-de-brasilia.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/08/doria-diz-que-nao-vai-cortar-servicos-nem-fechar-espacos-culturais-de-sp.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/08/mais-de-600-raios-atingem-a-grande-sp-durante-temporal-no-domingo.ghtml',""],
	]




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




# txt_l = '''[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["Patos de Minas PPL", "1"], ["Pouso Alegre Airport AIRP", "1"], ["Santo Antônio Pouso Alegre PPL", "1"], ["Mahajanga PPLA", "1"], ["Santo Antônio Pouso Alegre PPL", "1"], ["Betim PPL", "1"]]]]@[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["Ipatinga PPL", "1"], ["Pouso Alegre PPL", "1"], ["Santo Antônio Pouso Alegre PPL", "1"], ["Mahajanga PPLA", "1"], ["Santo Antônio Pouso Alegre PPL", "1"], ["Patos de Minas PPL", "1"]]]]@[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["Ipatinga PPL", "1"], ["Santo Antônio Pouso Alegre PPL", "1"], ["Pouso Alegre ADM2", "1"], ["Toliara PPLA", "1"], ["Santo Antônio Pouso Alegre PPL", "1"], ["Ipatinga PPL", "1"]]]]@[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["Ipatinga PPL", "1"], ["Nenhuma das Alternativas", "1"], ["Santo Antônio Pouso Alegre PPL", "1"], ["Antsirabe PPLA", "1"], ["Pouso Alegre ADM2", "1"], ["Betim PPL", "1"]]]]@'''

txt_l = '''[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["1 3457153 Minas Gerais ADM1 BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["5 0000000 Nenhuma das Alternativas", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["1 3457153 Minas Gerais ADM1 BR", "1"]]]]@[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["1 3457153 Minas Gerais ADM1 BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["5 0000000 Nenhuma das Alternativas", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["1 3457153 Minas Gerais ADM1 BR", "5"]]]]@[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["1 3457153 Minas Gerais ADM1 BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["5 0000000 Nenhuma das Alternativas", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["1 3457153 Minas Gerais ADM1 BR", "5"]]]]@[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["1 3457153 Minas Gerais ADM1 BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["5 0000000 Nenhuma das Alternativas", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["1 3457153 Minas Gerais ADM1 BR", "5"]]]]@[["https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml", [["1 3457153 Minas Gerais ADM1 BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["5 0000000 Nenhuma das Alternativas", "5"], ["0 3452525 Pouso Alegre PPL BR", "5"], ["1 3457153 Minas Gerais ADM1 BR", "5"]]]]@'''






# l = [[['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml', [['Patos de Minas PPL', '1'], ['Pouso Alegre Airport AIRP', '1'], ['Santo Ant\xc3\xb4nio Pouso Alegre PPL', '1'], ['Mahajanga PPLA', '1'], ['Santo Ant\xc3\xb4nio Pouso Alegre PPL', '1'], ['Betim PPL', '1']]]], [['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml', [['Ipatinga PPL', '1'], ['Pouso Alegre PPL', '1'], ['Santo Ant\xc3\xb4nio Pouso Alegre PPL', '1'], ['Mahajanga PPLA', '1'], ['Santo Ant\xc3\xb4nio Pouso Alegre PPL', '1'], ['Patos de Minas PPL', '1']]]], [['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml', [['Ipatinga PPL', '1'], ['Santo Ant\xc3\xb4nio Pouso Alegre PPL', '1'], ['Pouso Alegre ADM2', '1'], ['Toliara PPLA', '1'], ['Santo Ant\xc3\xb4nio Pouso Alegre PPL', '1'], ['Ipatinga PPL', '1']]]], [['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml', [['Ipatinga PPL', '1'], ['Nenhuma das Alternativas', '1'], ['Santo Ant\xc3\xb4nio Pouso Alegre PPL', '1'], ['Antsirabe PPLA', '1'], ['Pouso Alegre ADM2', '1'], ['Betim PPL', '1']]]]]





def CronbachAlpha(itemscores):
    itemscores = numpy.asarray(itemscores)
    itemvars = itemscores.var(axis=1, ddof=1)
    tscores = itemscores.sum(axis=0)
    nitems = len(itemscores)

    return nitems / (nitems-1.) * (1 - itemvars.sum() / tscores.var(ddof=1))


def calculateAlpha():
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


	# print hash_tops	

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




def groupData():
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

def mean(l):
	return sum(l)/len(l)

def processData(title,url):
	
	minimum_value_to_accept_news = 4
	number_of_decimal_cases_on_std_dev = 4
	std_dev_to_accept = 1.8000

	nl = groupData()
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
				print "return False"
				return False

		# run in all votes for a spacific top and calculate some descriptive statistics
		for j in i:
			if j[0] == ctr[0][0]:
				info_top_to_carry =  j[0]
				aux_l.append(int(j[1]))
		
		mea = mean(aux_l)
		std_dev = round(statistics.stdev(aux_l), number_of_decimal_cases_on_std_dev)

		# verify if std_dev is acceptable
		if std_dev > std_dev_to_accept:
			return False

		mean_stddev.append((info_top_to_carry,mea,std_dev))


 	return mean_stddev
	

def js():

	tps = ['Minas', 'Pouso Alegre', 'Pouso Alegre', 'MG', 'Pouso Alegre', 'Minas']
	url = 'https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml'
	title = 'Funcionários são atropelados por ex-patrão após audiência trabalhista em MG'
	pr = (1.0, [('1 3457153 Minas Gerais ADM1 BR', 5, 0.0), ('0 3452525 Pouso Alegre PPL BR', 5, 0.0), ('0 3452525 Pouso Alegre PPL BR', 5, 0.0), ('5 0000000 Nenhuma das Alternativas', 5, 0.0), ('0 3452525 Pouso Alegre PPL BR', 5, 0.0), ('1 3457153 Minas Gerais ADM1 BR', 4, 1.2649)])
	pd = pr[1]

	# json_news = {
	# 	"title" : "",
	# 	"url" : "",
	# 	"crombach" : "",

	# 	"toponyms" : [{
	# 		"top_find_on_new" : "",
	# 		"top_selected_by_user" : "" ,
	# 		"toponym_geonamesId" : 0,
	# 		"mean_confiability" : 0,
	# 		"std_edv" : 0
			
	# 	}]

	# }

	json_news = {
		"title" : "",
		"url" : "",
		"crombach" : "",
		"toponyms" : []
	}


	json_news["title"] = title
	json_news["url"] = url
	json_news["crombach"] = pr[0]

	js = {}

	for i in range(len(tps)):
		js = {
			"top_find_on_new" : "",
			"top_selected_by_user" : "" ,
			"toponym_geonamesId" : 0,
			"mean_confiability" : 0,
			"std_edv" : 0
			
		}
		js["top_find_on_new"] = tps[i]

		if len(pd[i][0].split()[-2]) == 2:
			js["top_selected_by_user"] = " ".join(pd[i][0].split()[2:-2])
		else:
			js["top_selected_by_user"] = " ".join(pd[i][0].split()[2:-1])
		js["toponym_geonamesId"] = pd[i][0].split()[1]
		js["mean_confiability"] = int(pd[i][1])
		js["std_edv"] = int(pd[i][2])

		json_news['toponyms'].append(js)


	closed_news = json.dumps(json_news, sort_keys=False,indent=4)

	# print closed_news
def countUsers(title):
	# read_f = readFile(title)
	file_data_list = createDataList(txt_l)
	print len(file_data_list)

