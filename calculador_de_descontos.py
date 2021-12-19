from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

	def calcula(self, orcamento):

		desconto = Desconto_por_cinco_itens(
				Desconto_por_mais_de_quinhentos_reais(
					Sem_desconto()
				)
			).calcula(orcamento)

		return desconto

if __name__ == '__main__':

	from orcamento import Orcamento, Item

	orcamento = Orcamento()
	orcamento.adiciona_itens(Item('ITEM - 1', 100.0))
	orcamento.adiciona_itens(Item('ITEM - 2', 50.0))
	orcamento.adiciona_itens(Item('ITEM - 3', 400.0))

	calculador_de_descontos = Calculador_de_descontos()
	desconto = calculador_de_descontos.calcula(orcamento)

	print('Desconto calculado: %s', desconto)