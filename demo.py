from fpgrowth_py import fpgrowth, fpgrowthFromFile

itemSetList = [['eggs', 'bacon', 'soup'],
                ['eggs', 'bacon', 'apple'],
                ['soup', 'bacon', 'banana']]
freqItemSet, rules = fpgrowth(itemSetList, minSupRatio=0.5, minConf=0.5)
print(freqItemSet)
print(rules)  
# [[{'beer'}, {'rice'}, 0.6666666666666666], [{'rice'}, {'beer'}, 1.0]]
# rules[0] --> rules[1], confidence = rules[2]


# from file
freqItemSet, rules = fpgrowthFromFile('./dataset/tesco2.csv', minSupRatio=0.5, minConf=0.5)
print(freqItemSet)
print(rules)  
