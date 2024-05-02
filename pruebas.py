import numpy as np
from MFIS_Read_Functions import readFuzzySetsFile, readRulesFile, readApplicationsFile
import skfuzzy as skf
#from Main import evaluateApplication
#from Main import fuzzification



def main():
    try:
        # Load the data
        input_fuzzy_sets = readFuzzySetsFile('InputVarSets.txt')
        output_fuzzy_sets = readFuzzySetsFile("Risks.txt")
        rules = readRulesFile('Rules.txt')
        applications = readApplicationsFile('applicants.txt')


        # Process the applications
        return evaluateApplication(input_fuzzy_sets, output_fuzzy_sets, rules, applications)

        # Output results
        #writeResultsToFile(results)

    except Exception as e:
        print(f"An error occurred: {e}")


def evaluateApplication(InputFuzzySets, OutputFuzzySets, rules, applications):
    # Initialize a results dictionary


    # Process each application using the fuzzy logic
    for applicant in applications:
        # Apply fuzzy logic:

        # 1. Fuzzification: Convert crisp values to degrees of membership for each fuzzy set
        fuzzification(applicant, InputFuzzySets)


        # 2. Rule Evaluation: Apply the fuzzy rules to the fuzzified inputs
        rule_evaluation(rules, InputFuzzySets, OutputFuzzySets)
    

        # 3. Aggregation of rule outputs
        output_fuzzy_set = aggregate_outputs(OutputFuzzySets)
        print(output_fuzzy_set) #Debugging purposes



        # 4. Defuzzification: Convert the result of fuzzy inference to a crisp output
        # crisp_value = defuzzification(output_fuzzy_set, list(fuzzySets.values())[0].x)

        # results[applicant.appId] = crisp_value  # Directly assigning the crisp value

        # reset_membership_degrees(fuzzySets)  # Reset membership degrees for the next application

    # Return the compiled results of all applications
        #print(fuzzySets[1].memDegree)



def fuzzification(applicant, FuzzySetsDict):
    for var_value in applicant.data:  # var_value is a sub-list. (eg. [age, 35])
        variable, value = var_value[0], var_value[1]  # (eg. variable = Age, and value = 35)
        for fuzzySet in FuzzySetsDict.items():
            if fuzzySet[0].split('=')[0] == variable:
                # Update degree of membership in the set object´s memDegree attribute.
                fuzzySet[1].memDegree = skf.interp_membership(fuzzySet[1].x, fuzzySet[1].y, value)


def rule_evaluation(rules, fuzzySetsDict, RisksfuzzySetsDict):
    for rule in rules:
        min_degree = float('inf')  # Start with an infinitely large number
        for antecedent in rule.antecedent:
            if antecedent in fuzzySetsDict and fuzzySetsDict[antecedent].memDegree < min_degree:
               min_degree = fuzzySetsDict[antecedent].memDegree
        if min_degree != float('inf'):
           rule.strength = min_degree  # The strength of the rule is the minimum membership degree
           consequent_set = RisksfuzzySetsDict[rule.consequent]
           consequent_set.memDegree = max(consequent_set.memDegree, min_degree)  # Use max to handle multiple rules affecting the same consequent.

def aggregate_outputs(fuzzySetsDict):
    # Initialize an array of zeros. Used to store the aggregated output fuzzy set.
    output_fuzzy_set = np.zeros_like(list(fuzzySetsDict.values())[0].x)

    # Loop over each fuzzy set in the dictionary
    for fuzzySet in fuzzySetsDict.items():
        # For each fuzzy set, calculate the membership function value multiplied by the membership degree.
        # This gives the contribution of this fuzzy set to the output fuzzy set.

        #print(fuzzySet[1].y, fuzzySet[1].memDegree) #DEBUGGING PURPOSES


        membership_contribution = fuzzySet[1].y * fuzzySet[1].memDegree

        #print("Mem degree Debugging",fuzzySet[1].memDegree) #Debugging purposes

        # Combine the calculated membership contribution with the existing output fuzzy set.
        # We use the maximum membership function value at each point (np.fmax).



        output_fuzzy_set = np.fmax(output_fuzzy_set, membership_contribution)

    # Return the aggregated output fuzzy set.
    return output_fuzzy_set



#rules = readRulesFile()
#print(rules[1].antecedent)
#print(rules[1].consequent)

#applications = readApplicationsFile()
#print(applications[0].data[0][1])


main()


