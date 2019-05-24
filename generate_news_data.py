import tutor
import json

urls = [
	['https://g1.globo.com/economia/noticia/2019/03/28/carrefour-cortara-mais-de-1-mil-empregos-na-franca-diz-sindicato.ghtml',""],
	['https://g1.globo.com/sp/mogi-das-cruzes-suzano/noticia/2019/03/13/cena-mais-triste-que-assisti-em-toda-a-minha-vida-diz-doria-sobre-ataque-em-escola-em-suzano.ghtml',""],
	['https://g1.globo.com/mg/sul-de-minas/noticia/2019/03/20/funcionarios-sao-atropelados-por-ex-patrao-apos-audiencia-trabalhista-em-mg.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/22/homem-e-suspeito-de-matar-mulher-em-belo-horizonte.ghtml',""],
	['https://g1.globo.com/mundo/noticia/2018/10/21/principe-harry-vai-a-evento-sem-meghan-que-reduz-agenda-por-causa-da-gravidez.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/03/20/verao-2019-foi-o-5o-mais-quente-da-historia-outono-tera-temperaturas-pouco-acima-da-media.ghtml',""],
	['https://g1.globo.com/rj/rio-de-janeiro/noticia/2019/03/20/policia-investiga-morte-de-jovem-de-18-anos-com-oito-tiros-na-baixada-fluminense.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/ipva-2019-em-mg-prazo-para-pagar-3a-parcela-termina-quarta.ghtml',""],
	['https://g1.globo.com/mg/minas-gerais/noticia/2019/03/20/camara-de-bh-aprova-em-1o-turno-projeto-que-autoriza-botao-de-panico-em-escolas.ghtml',""],
	['https://g1.globo.com/df/distrito-federal/noticia/2019/04/05/operacao-investiga-grupo-que-desviou-mais-de-r-800-mil-de-clientes-do-bando-de-brasilia.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/08/doria-diz-que-nao-vai-cortar-servicos-nem-fechar-espacos-culturais-de-sp.ghtml',""],
	['https://g1.globo.com/sp/sao-paulo/noticia/2019/04/08/mais-de-600-raios-atingem-a-grande-sp-durante-temporal-no-domingo.ghtml',""],
	['https://g1.globo.com/economia/noticia/2019/04/11/eletrobras-anuncia-conclusao-de-venda-da-amazonas-energia.ghtml',""],
	['https://g1.globo.com/pr/parana/noticia/2019/04/10/ex-presidente-do-bb-e-da-petrobras-aldemir-bendine-deixa-prisao-apos-decisao-do-stf.ghtml',""],
	['https://g1.globo.com/loterias/noticia/2019/04/10/mega-sena-concurso-2141-ninguem-acerta-as-seis-dezenas-e-premio-vai-a-r-45-milhoes.ghtml',""],
	['https://g1.globo.com/to/tocantins/noticia/2019/04/10/justica-federal-bloqueia-bens-do-ex-governador-marcelo-miranda-para-pagar-custos-da-eleicao-suplementar.ghtml',""],
	['https://g1.globo.com/economia/blog/joao-borges/post/2019/04/10/para-presidente-da-cna-mal-entendido-com-paises-islamicos-e-pagina-virada.ghtml',""],
	['https://g1.globo.com/economia/tecnologia/noticia/2019/04/10/amazon-libera-ferramentas-da-alexa-para-desenvolvedores-brasileiros.ghtml',""],
	['https://g1.globo.com/economia/noticia/2019/04/10/bce-mantem-politica-monetaria.ghtml',""],
	['https://g1.globo.com/economia/noticia/2019/04/09/avianca-brasil-pede-suspensao-de-liminar-para-evitar-retomada-de-avioes.ghtml',""],
	['https://g1.globo.com/economia/agronegocios/noticia/2019/04/09/jbs-faz-recall-de-20-toneladas-de-carne-moida-contaminada-com-plastico-nos-eua.ghtml',""],
	['https://g1.globo.com/economia/noticia/2019/04/09/em-avanco-china-promete-maior-abertura-a-empresas-da-uniao-europeia.ghtml',""],
	]

def generateNews():
    global urls
    for i in urls:
	    if not i[1]:
		    i[1] = tutor.applicationDev(i[0])

def saveNews():
    global urls

    with open("preProssedNews/news.txt", "w") as file:
        json_str = json.dumps(urls, ensure_ascii=False).encode('utf8')
        file.write(json_str)

if __name__ == '__main__':
    generateNews()
    saveNews()


