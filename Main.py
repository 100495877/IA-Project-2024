import numpy as np
from MFIS_Read_Functions import readFuzzySetsFile, readRulesFile, readApplicationsFile
import skfuzzy as skf
import json


def main():
    try:
        # Load the data
        input_fuzzy_sets = readFuzzySetsFile('InputVarSets.txt')
        output_fuzzy_sets = readFuzzySetsFile('Risks.txt')
        rules = readRulesFile('NewRules')
        applications = readApplicationsFile('Applications.txt')


        # Process the applications
        evaluations = evaluateApplication(input_fuzzy_sets, output_fuzzy_sets, rules, applications)

        # Output results
        writeResultsToFile(evaluations, 'Results.txt')

    except Exception as e:
        print(f"An error occurred: {e}")


def evaluateApplication(InputFuzzySets, OutputFuzzySets, rules, applications):
    # Initialize a results dictionary
    results = {}

    # Process each application using the fuzzy logic
    for applicant in applications:
        # Apply fuzzy logic:

        # 1. Fuzzification: Convert crisp values to degrees of membership for each fuzzy set
        fuzzification(applicant, InputFuzzySets)


        # 2. Rule Evaluation: Apply the fuzzy rules to the fuzzified inputs
        rule_evaluation(rules, InputFuzzySets, OutputFuzzySets)
    

        # 3. Aggregation of rule outputs
        output_fuzzy_set = aggregate_outputs(OutputFuzzySets)


        # 4. Defuzzification: Convert the result of fuzzy inference to a crisp output
        l = list(range(0, 100))
        crisp_value = defuzzification(output_fuzzy_set, l)

        results[applicant.appId] = crisp_value  # Directly assigning the crisp value

        # Reset membership degrees for the next application
        reset_membership_degrees(InputFuzzySets)  
        reset_membership_degrees(OutputFuzzySets)

    # Return the compiled results of all applications
    return results


def fuzzification(applicant, FuzzySetsDict):
    for var_value in applicant.data:  # var_value is a sub-list. (eg. [age, 35])
        variable, value = var_value[0], var_value[1]  # (eg. variable = Age, and value = 35)
        for fuzzySet in FuzzySetsDict.items():
            if fuzzySet[0].split('=')[0] == variable:
                # Update degree of membership in the set object´s memDegree attribute.
                fuzzySet[1].memDegree = skf.interp_membership(fuzzySet[1].x, fuzzySet[1].y, value)


# if AND, AND: min(x, y, z) <-- ahora estamos aquí
# if AND, OR: min(x, max(y, z))
#if OR, AND: max(x, min(y, z))
# if OR, OR: maz(x, y, z)
def rule_evaluation(rules, fuzzySetsDict, RisksfuzzySetsDict):
    for rule in rules:
        min_degree = float('inf')  # Start with an infinitely large number
        max_degree = 0
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
        membership_contribution = fuzzySet[1].y * fuzzySet[1].memDegree
        output_fuzzy_set = np.fmax(output_fuzzy_set, membership_contribution)
    # Return the aggregated output fuzzy set.
    return output_fuzzy_set


def defuzzification(output_fuzzy_set, l: list):
    centroid = np.sum(np.array(l) * output_fuzzy_set) / np.sum(output_fuzzy_set)
    return centroid


def reset_membership_degrees(fuzzySetsDict):
    for fuzzySet in fuzzySetsDict.items():
        fuzzySet[1].memDegree = 0

        import json

def writeResultsToFile(results_dict, file_path):
    #Writes the given dictionary to a file specified by file_path in JSON format.
    try:
        with open(file_path, 'w') as file:
            # Convert the dictionary to a JSON string and write it to the file
            json.dump(results_dict, file, indent=4)
        print(f"Results have been successfully written to {file_path}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")



main()

