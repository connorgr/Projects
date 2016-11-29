from sys import exit

class Calculator:
    def __init__(self):
        self.__memory = 0
        self.__operators = "+-/*"
        self.__validInput = "0123456789()"+self.__operators

        print "Please start your computation (press 'q' to quit)...."
        while True:
            try:
                calculation = str(raw_input(" > : "))
                if len(calculation) == 0:
                    continue
                calculation = calculation.replace(" ", "").strip()

                if calculation == "q":
                    exit()
                if calculation == "c":
                    self.__memory = 0
                    print "MEMORY CLEARED"
                    continue
                if calculation == "=":
                    print self.__memory
                    continue

                if sum([c in self.__validInput for c in calculation]) != len(calculation):
                    print "ERROR: Invalid input. Please try again."
                    continue

                openParens = [c for c in calculation if c == "("]
                closeParens = [c for c in calculation if c == ")"]
                if len(openParens) != len(closeParens):
                    print "ERROR: NON-MATCHING PARENTHASES"
                    continue

                computationStacks = []
                computationStacks.append([])

                for c in calculation:
                    if c == "(":
                        computationStacks.append([])
                    elif c == ")":
                        result = self.evaluate(computationStacks[-1])
                        del computationStacks[-1]
                        if len(computationStacks) == 0:
                            return result
                        else:
                            computationStacks[-1].append(result)
                    else:
                        computationStacks[-1].append(c)

                if len(computationStacks) != 1:
                    print "ERROR: NON-MATCHING PARENTHASES"
                    continue

                if str(computationStacks[0][0]) in self.__operators:
                    if len(calculation) == 1:
                        print "ERROR: please provide more than just an operator."
                        continue
                    result = self.evaluate([self.__memory] + computationStacks[0])
                else:
                    result = self.evaluate(computationStacks[0])

                print result
                self.__memory = result
            except ZeroDivisionError:
                print "ERROR: You tried dividing by zero. Please try again."
                continue
            except Exception("ERROR"):
                continue


    def evaluate(self, computationList):
        multIdxs = [i for i,v in enumerate(computationList) if v == "*"]
        for mi in multIdxs:
            computationList = computationList[:(mi-1)] + [float(computationList[mi-1])*float(computationList[mi+1])] + computationList[(mi+2):]

        divIdxs = [i for i,v in enumerate(computationList) if v == "/"]
        for di in divIdxs:
            computationList = computationList[:(di-1)] + [float(computationList[di-1])/float(computationList[di+1])] + computationList[(di+2):]

        plusIdxs = [i for i,v in enumerate(computationList) if v == "+"]
        for pi in plusIdxs:
            computationList = computationList[:(pi-1)] + [float(computationList[pi-1])+float(computationList[pi+1])] + computationList[(pi+2):]

        subIdxs = [i for i,v in enumerate(computationList) if v == "-"]
        for si in subIdxs:
            computationList = computationList[:(si-1)] + [float(computationList[si-1])-float(computationList[si+1])] + computationList[(si+2):]

        return computationList[0]




if __name__ == "__main__":
    calculator = Calculator()
