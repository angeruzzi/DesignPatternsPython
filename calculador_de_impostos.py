from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):


	def realiza_calculo(self, orcamento, imposto):

		imposto_calculado = imposto.calcula(orcamento)
		print(imposto_calculado)


if __name__ == '__main__':

	from orcamento import Orcamento, Item

	calculador_de_impostos = Calculador_de_impostos()
	orcamento = Orcamento()
	orcamento.adiciona_itens(Item('ITEM - 1', 100.0))
	orcamento.adiciona_itens(Item('ITEM - 2', 50.0))
	orcamento.adiciona_itens(Item('ITEM - 3', 400.0))

	print('ISS e ICMS')
	calculador_de_impostos.realiza_calculo(orcamento, ISS())
	calculador_de_impostos.realiza_calculo(orcamento, ICMS())

	print('ICPP e IKCV')
	calculador_de_impostos.realiza_calculo(orcamento, ICPP())
	calculador_de_impostos.realiza_calculo(orcamento, IKCV())

	print('ICPP_com_IKCV')
	ICPP_com_IKCV = ICPP(IKCV())
	calculador_de_impostos.realiza_calculo(orcamento, ICPP_com_IKCV)