#!/usr/bin/env python3
import numpy as np
import skfuzzy as skf
import matplotlib.pyplot as plt
from MFIS_Classes import *

def readFuzzySetsFile(fileName):
    """
    This function reads a file containing fuzzy set descriptions
    and returns a dictionary with all of them
    """
    inputFile = open(fileName,'r')
    fuzzySetsDict = FuzzySetsDict() # dictionary to be returned

    line = inputFile.readline()

    while line != '':
        fuzzySet = FuzzySet()   # just one fuzzy set
        elementsList = line.split(', ')
        setid = elementsList[0]
        var_label=setid.split('=')
        fuzzySet.var=var_label[0]
        fuzzySet.label=var_label[1]

        xmin = int(elementsList[1])
        xmax = int(elementsList[2])
        a = int(elementsList[3])
        b = int(elementsList[4])
        c = int(elementsList[5])
        d = int(elementsList[6])
        
        x = np.arange(xmin,xmax,1)
        y = skf.trapmf(x, [a, b, c, d])
        fuzzySet.x = x
        fuzzySet.y = y
        fuzzySetsDict.update( { setid : fuzzySet } )

        line = inputFile.readline()
    inputFile.close()
    return fuzzySetsDict

def readRulesFile(fileName):
    inputFile = open(fileName, 'r')
    rules = RuleList()
    line = inputFile.readline()
    while line != '':
        rule = Rule()
        line = line.rstrip()
        elementsList = line.split(', ')
        rule.ruleName = elementsList[0]
        rule.consequent = elementsList[1]
        lhs = []
        counter = 1
        for i in range(2, len(elementsList), 1):
            #if elementsList[i][0] != "OP1" and elementsList[i][0] != "OP2":
            lhs.append(elementsList[i])
            counter += 1
        rule.antecedent = lhs
        if counter > 5:
            if rule.antecedent[3] == "OP1=OR":
                rule.op1 = 0
            if rule.antecedent[4] == "OP2=OR":
                rule.op2 = 0
        rules.append(rule)
        line = inputFile.readline()
        if rule.antecedent == "OP1=OR":
            rule.op1 = 0
    inputFile.close()
    return rules

def readApplicationsFile(fileName):
    inputFile = open(fileName, 'r')
    applicationList = []
    line = inputFile.readline()
    while line != '':
        elementsList = line.split(', ')
        app = Application()
        app.appId = elementsList[0]
        app.data = []
        for i in range(1, len(elementsList), 2):
            app.data.append([elementsList[i], int(elementsList[i+1])])
        applicationList.append(app)
        line = inputFile.readline()
    inputFile.close()
    return applicationList

