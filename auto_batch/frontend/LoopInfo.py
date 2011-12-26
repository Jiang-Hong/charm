import con, sys

class LoopInfo:
	def __init__(self):
		self.loopName = None
		self.loopOverValue = None
		self.varListNoSubscripts = None
		self.varListWithSubscripts = None
		self.expression = None

	def getLoopName(self):
		return self.loopName

	def getLoopOverValue(self):
		return self.loopOverValue

	def getVarListNoSubscripts(self):
		return self.varListNoSubscripts

	def getVarListWithSubscripts(self):
		return self.varListWithSubscripts

	def getExpression(self):
		return self.expression

	def setLoopName(self, loopName):
		if ( (loopName == None) or (type(loopName).__name__ != con.strTypePython) or (len(loopName) == 0) ):
			sys.exit("LoopInfo->setLoopName:  problem with loop name passed in.")

		foundLoopPrefix = False

		for prefix in con.loopPrefixes:
			if (loopName.startswith(prefix) == True):
				foundLoopPrefix = True
				break

		if (foundLoopPrefix == False):
			sys.exit("LoopInfo->setLoopName:  loop name passed in (" + loopName + ") is not one of the supported loop types (" + con.loopPrefixes + ").")
 
		self.loopName = loopName

	def setLoopOverValue(self, loopOverValue):
		if ( (loopOverValue == None) or (type(loopOverValue).__name__ != con.strTypePython) or (len(loopOverValue) == 0) ):
			sys.exit("LoopInfo->setLoopOverValue:  problem with loop over value passed in (" + loopOverValue + ").")

		if (loopOverValue not in con.loopTypes):
			sys.exit("LoopInfo->setLoopOverValue:  loop over value passed in (" + loopOverValue + ") is not one of the supported loop types (" + con.loopTypes + ").")

		self.loopOverValue = loopOverValue

	def setVarListNoSubscripts(self, list):
		if ( (list == None) or (type(list).__name__ != con.listTypePython) or (len(list) == 0) ):
			sys.exit("LoopInfo->setVarListNoSubscripts:  problem with variable list passed in.")

		for varName in list:
			if (type(varName).__name__ != con.stringName):
				sys.exit("LoopInfo->setVarListNoSubscripts:  one of the variable names in the list passed in is not of type " + con.stringName)

			varNameAsString = varName.getStringVarName()
			if (varNameAsString.find(con.loopIndicator) != -1):
				sys.exit("LoopInfo->setVarListNoSubscripts:  one of the variable names (" + varNameAsString + ") has the subscript character in it (" + con.loopIndicator + ").")

		self.varListNoSubscripts = list

	def setVarListWithSubscripts(self, list):
		if ( (list == None) or (type(list).__name__ != con.listTypePython) or (len(list) == 0) ):
			sys.exit("LoopInfo->setVarListWithSubscripts:  problem with variable list passed in.")

		for varName in list:
			if (type(varName).__name__ != con.stringName):
				sys.exit("LoopInfo->setVarListWithSubscripts:  one of the variable names in the list passed in is not of type " + con.stringName)

		self.varListWithSubscripts = list

	def setExpression(self, expression):
		if ( (expression == None) or (type(expression).__name__ != con.strTypePython) or (len(expression) == 0) ):
			sys.exit("LoopInfo->setExpression:  problem with expression passed in.")

		self.expression = expression
