from lxml import html
import requests
import time

class AppCrawler:

	def __init__(self, url_inicial, nivel_max):
		self.url_inicial = url_inicial
		self.nivel_max = nivel_max
		self.nivel_atual = 0
		self.links_nivel = []
		self.apps = []

	def get_app_do_link(self, link):
		pagina_inicial = requests.get(link)
		arvore = html.fromstring(pagina_inicial.text)

		nome = arvore.xpath('//h1[@class="product-header__title app-header__title"]/text()')[0].strip()
		desenvolvedor = arvore.xpath('//dd[@class="information-list__item__definition l-column medium-9 large-6"]/text()')[0].strip()
		links = arvore.xpath('//a[@class="we-lockup targeted-link l-column small-2 medium-3 large-2 ember-view"]/@href')

		app = App(nome, desenvolvedor, links)
		
		return app

	def crawl(self):

		app = self.get_app_do_link(self.url_inicial)
		self.apps.append(app)
		self.links_nivel.append(app.links)

		while self.nivel_atual < self.nivel_max:
			links_atuais = []
			for link in self.links_nivel[self.nivel_atual]:
				app_atual = self.get_app_do_link(link)
				links_atuais.extend(app_atual.links)
				self.apps.append(app_atual)
				time.sleep(2)
			self.nivel_atual += 1
			self.links_nivel.append(links_atuais)
		
		return


class App:
	def __init__(self, nome, desenvolvedor, links):
		self.nome = nome
		self.desenvolvedor = desenvolvedor
		self.links = links

	def __str__(self):
		return ("'" + self.nome + "'; '" + self.desenvolvedor + "'")

crawler = AppCrawler('https://itunes.apple.com/br/app/clash-royale/id1053012308', 1)
crawler.crawl()
for app in crawler.apps:
	print(app)
