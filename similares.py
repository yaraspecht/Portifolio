
from math import sqrt

def sim_euclidiana(avaliacoes, c1, c2):

	mesmos_filmes = {}
	for filme in avaliacoes[c1]:
		if filme in avaliacoes[c2]:
			mesmos_filmes[filme] = 1

	if len(mesmos_filmes) == 0: return 0

	dist_euclidiana = sqrt(sum([pow((avaliacoes[c1][filme] - avaliacoes[c2][filme]), 2) for filme in mesmos_filmes]))

	return 1 / (1 + dist_euclidiana)

def sim_manhattan(avaliacoes, c1, c2):

	mesmos_filmes = {}
	for filme in avaliacoes[c1]:
		if filme in avaliacoes[c2]:
			mesmos_filmes[filme] = 1

	if len(mesmos_filmes) == 0: return 0

	dist_manhattan = sum([abs(avaliacoes[c1][filme] - avaliacoes[c2][filme]) for filme in mesmos_filmes])

	return 1 / (1 + dist_manhattan)


def sim_pearson(avaliacoes, c1, c2):

	mesmos_filmes = {}
	for filme in avaliacoes[c1]:
		if filme in avaliacoes[c2]:
			mesmos_filmes[filme] = 1

	n = len(mesmos_filmes)
	if n == 0: return 0

	media_c1 = sum([avaliacoes[c1][filme] for filme in mesmos_filmes]) / n
	media_c2 = sum([avaliacoes[c2][filme] for filme in mesmos_filmes]) / n
	numerador = sum([((avaliacoes[c1][filme] - media_c1) * (avaliacoes[c2][filme] - media_c2)) for filme in mesmos_filmes])
	denominador = sqrt(sum([pow((avaliacoes[c1][filme] - media_c1), 2) for filme in mesmos_filmes])
						* sum([pow((avaliacoes[c2][filme] - media_c2), 2) for filme in mesmos_filmes]))
	if denominador == 0: return 0
	r = numerador / denominador
	return r

def top_similares(avaliacoes, pessoa, n = 1, medida = sim_euclidiana):
	valores = [(medida(avaliacoes, pessoa, outra), outra) for outra in avaliacoes if outra != pessoa]
	valores.sort()
	valores.reverse()
	return valores[0:n]
	
def inverte(avaliacoes):
	resultado = {}
	for pessoa in avaliacoes:
		for filme in avaliacoes[pessoa]:
			resultado.setdefault(filme, {})
			resultado[filme][pessoa] = avaliacoes[pessoa][filme]

	return resultado
