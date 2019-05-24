#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from polyglot.text import Text, Word
import info_extract
import scrap

def lprint(s):
	for i in s:
		print i

def applicationDev(url):
	
	blob = scrap.get_paragraph(url)

	# todos os toponimos presentes no texto
	topon = info_extract.parse_text_toponimo(blob)

	# remove toponimos repetidos
	newlist_t=[ii for n,ii in enumerate(topon) if ii not in topon[:n]]

	# toponimos na ordem em que aparecem no texto
	toponimos = info_extract.sortToponymOccurence(info_extract.get_sentence(blob), newlist_t)

	# para cada toponimo -> pegar json associado e criar lista
	json_data = scrap.getToponymAndAttachJson(toponimos)
	
	#insere a tag select em cada toponimo
	select_options = info_extract.insertDataIntoSelectTag(json_data)

	# pega todas as frases da noticia
	sentence = info_extract.get_sentence(blob)

	# cria um botao com o nome do toponimo 
	toponym_button_text = info_extract.create_text_button(newlist_t)

	# texto gerado
	inicial_text = info_extract.replaceMultiple(sentence,newlist_t,toponym_button_text)
	
	# texto gerado
	text_with_button = info_extract.putButtonIndex(inicial_text)

	text_with_button_id = info_extract.putIndexInToponyms(text_with_button)
	
	final_text = info_extract.generateText(text_with_button_id, select_options)	

	return (final_text, toponimos)
