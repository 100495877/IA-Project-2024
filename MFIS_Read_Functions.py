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
    fuzzySetsDict = FuzzySetsDict() # dictionary to be returned
    inputFile = open(fileName, 'r')
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

"""def readRulesFile(filename):
    rules = []
    with open(filename, 'r') as file:
        for line in file:
            conditions = line.strip().split(', ')
            rule = {}
            for condition in conditions:
                variable, value = condition.split('=')
                rule[variable] = value
            rules.append(rule)
    return rules"""
def readRulesFile(filename):
    rules = []
    with open(filename, 'r') as file:
        for line in file:
            conditions = line.strip().split(', ')
            rule = {}
            for condition in conditions:
                if '=' in condition:
                    variable, value = condition.split('=')
                    rule[variable] = value
                else:
                    print(f"Warning: Invalid condition '{condition}' in rule '{line.strip()}'. Condition should be in the format 'variable=value'.")
            rules.append(rule)
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

