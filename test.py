from MChain import MarkovChain

def main():
    MC = MarkovChain.MarkovChain(10)

    TDict, Tokens = MC.initMTuple('test2.txt')
    MC.initSimpleChain(Tokens,TDict)

    MC.buildProbabilities(TDict)
    print(TDict)
    print(MC.buildText(TDict))

if __name__=='__main__':
    main()