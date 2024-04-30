
import numpy as np
from MFIS_Read_Functions import readFuzzySetsFile, readRulesFile, readApplicationsFile
import skfuzzy as skf


def main():
    try:
        # Load the data
        fuzzy_sets = readFuzzySetsFile()
        rules = readRulesFile()
        applications = readApplicationsFile()

        # Process the applications
        #results = evaluateApplication(fuzzy_sets, rules, applications)
        #for fuzzy in fuzzy_sets.items():
        #print(fuzzy[1].y[0])

        # Output results
        #writeResultsToFile(results)

    except Exception as e:
        print(f"An error occurred: {e}")




def evaluateApplication(fuzzySets, rules, application):
    # Initialize a results dictionary
    results = {}
    
    # Process each application using the fuzzy logic
    for applicant in application:
        # Apply fuzzy logic:

        # 1. Fuzzification: Convert crisp values to degrees of membership for each fuzzy set
        fuzzification(applicant, fuzzySets)

        # 2. Rule Evaluation: Apply the fuzzy rules to the fuzzified inputs
        #rule_evaluation(rules, fuzzySets)

        # 3. Aggregation of rule outputs
        #output_fuzzy_set = aggregate_outputs(fuzzySets)

        # 4. Defuzzification: Convert the result of fuzzy inference to a crisp output
        #crisp_value = defuzzification(output_fuzzy_set, list(fuzzySets.values())[0].x)

        #results[applicant.appId] = crisp_value  # Directly assigning the crisp value
                
        #reset_membership_degrees(fuzzySets)  # Reset membership degrees for the next application
    
    # Return the compiled results of all applications
    return results

def fuzzification(applicant, FuzzySetsDict):
    for var_value in applicant.data: # var_value is a list of lists. (eg. [age, 35])
        variable, value = var_value[0], var_value[1] # (eg. variable = Age, and value = 35)
        for fuzzySet in FuzzySetsDict.items():
            if fuzzySet[0] == variable:  # Match the application variable to the fuzzy set variable
                # Assuming linear membership within ranges defined by a, b, c, d
                if value < fuzzySet[1].x[0] or value > fuzzySet[1].x[-1]:
                    fuzzySet.memDegree = 0  # No membership if out of bounds
                else:
                    for x in fuzzySet[1].x: # We go through the x values of the fuzzy set
                        if value == x: # If the value is in the x values of the fuzzy set
                            fuzzySet.memDegree = fuzzySet[1].y[fuzzySet[1].x.index(x)] # Membership degree corresponds to the y value






''' 
def writeResultsToFile(results, filename="Results.txt"):
    with open(filename, "w") as file:
        for app_id, risk in results.items():
            file.write(f"{app_id}, Risk Level: {risk}\n")


# Mamdani methods

def fuzzification(application, FuzzySetsDict):
    for var_value in application.data:
        variable, value = var_value[0], var_value[1]
        for setid, fuzzySet in FuzzySetsDict.items():
            if fuzzySet.var == variable:  # Match the application variable to the fuzzy set variable
                # Assuming linear membership within ranges defined by a, b, c, d
                if value < fuzzySet.x[0] or value > fuzzySet.x[-1]:
                    fuzzySet.memDegree = 0  # No membership if out of bounds
                else:
                    index = np.where(fuzzySet.x == value)[0][0]  # Find the index of the value in the x array
                    fuzzySet.memDegree = fuzzySet.y[index]  # Membership degree corresponds to the y value


def rule_evaluation(rules, fuzzySetsDict):
    for rule in rules:
        min_degree = float('inf')  # Start with an infinitely large number
        for antecedent in rule.antecedent:
            if antecedent in fuzzySetsDict and fuzzySetsDict[antecedent].memDegree < min_degree:
                min_degree = fuzzySetsDict[antecedent].memDegree
        if min_degree != float('inf'):
            rule.strength = min_degree  # The strength of the rule is the minimum membership degree
            consequent_set = fuzzySetsDict[rule.consequent]
            consequent_set.memDegree = max(consequent_set.memDegree, min_degree)  # Use max to handle multiple rules affecting the same consequent


def aggregate_outputs(fuzzySetsDict):
    output_fuzzy_set = np.zeros_like(list(fuzzySetsDict.values())[0].x)  # Assume all x arrays are the same length
    for setid, fuzzySet in fuzzySetsDict.items():
        output_fuzzy_set = np.fmax(output_fuzzy_set, fuzzySet.y * fuzzySet.memDegree)  # Max membership for each point
    return output_fuzzy_set


def defuzzification(output_fuzzy_set, x):
    crisp_value = skf.defuzz(x, output_fuzzy_set, 'centroid')  # Calculate the centroid of the aggregated fuzzy set
    return crisp_value



def reset_membership_degrees(fuzzySetsDict):
    for fuzzySet in fuzzySetsDict.values():
        fuzzySet.memDegree = 0


if __name__ == "__main__":
    main()

'''
main()