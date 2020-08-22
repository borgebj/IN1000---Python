## Klasse for representasjon av noder i en dataklynge
        #
class Node:
        ## Oppretter en node med gitt minne-storrelse og antall prosessorer
        #  @param minne GB minne i den nye noden
        #  @param antPros antall prosessorer i den nye noden
        def __init__(self, minne, antPros):
        pass

        ## Henter antall prosessorer i noden
        #  @return antall prosessorer i noden
        def antProsessorer(self):
        pass

        ## Sjekker om noden har tilstrekkelig minne for et program
        #  @param paakrevdMinne GB minne som kreves for programmet
        #  @return True hvis noden har minst saa mye minne
        def nokMinne(self, paakrevdMinne):
        pass


## Klasse for representasjon av racks i en dataklynge.
#
class Rack:
	## oppretter et rack der det senere kan plasseres noder
	#
	def __init__(self):
		pass

	## Plasserer en ny node inn i racket
	#  @param node noden som skal plasseres inn
	def settInn(self, node):
		pass

	## Henter antall noder i racket
	# @return antall noder
	def getAntNoder(self):
		pass

	## Beregner sammenlagt antall prosessorer i nodene i et rack
	# @return antall prosessorer
	def antProsessorer(self):
		pass

	## Beregner antall noder i racket med minne over gitt grense
	# @param paakrevdMinne antall GB minne som kreves
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		pass





## Klasse for representasjon av dataklynge med racks og noder
#  MERK to alternative konstruktorer, avhengig av om oppgave d) loeses

class Dataklynge:
	## Oppretter tom dataklynge for racks med oppgitt maxtall noder/ rack
	# @param noderPerRack max antall noder som kan plasseres i et rack
	def __init__(self, noderPerRack):
		pass

	## Alternativ konstruktor for de som loser oppgave d). Kan ellers ignoreres
	## Leser data om dataklynge fra fil, bygger datastrukturen.
	# @param filnavn filene der dataene for dataklyngen ligger
#	def __init__(self, filnavn):
#		pass

	## Plasserer en node inn i et rack med ledig plass, eller i et nytt
	# @param node referanse til noden som skal settes inn i datastrukturen
	def settInnNode(self, node):
		pass

	## Beregner totalt antall prosessorer i hele dataklyngen
	# @return totalt antall prosessorer
	def antProsessorer(self):
		pass

	## Beregner antall noder i dataklyngen med minne over angitt grense
	# @param paakrevdMinne hvor mye minne skal noder som telles med ha
	# @return antall noder med tilstrekkelig minne
	def noderMedNokMinne(self, paakrevdMinne):
		pass

	## Henter antall racks i regneklyngen
	# @return antall racks
	def antRacks(self):
		pass


















    