import numpy as np
from MFIS_Read_Functions import readFuzzySetsFile, readRulesFile, readApplicationsFile
import skfuzzy as skf
#from Main import evaluateApplication
#from Main import fuzzification



def main():
    try:
        # Load the data
        fuzzy_sets = readFuzzySetsFile()
        rules = readRulesFile()
        applications = readApplicationsFile()

        # Process the applications
        return evaluateApplication(fuzzy_sets, rules, applications)

        # Output results
        #writeResultsToFile(results)

    except Exception as e:
        print(f"An error occurred: {e}")


def evaluateApplication(fuzzySets, rules, applications):
    # Initialize a results dictionary


    # Process each application using the fuzzy logic
    for applicant in applications:
        # Apply fuzzy logic:

        # 1. Fuzzification: Convert crisp values to degrees of membership for each fuzzy set
        fuzzification(applicant, fuzzySets)

        # 2. Rule Evaluation: Apply the fuzzy rules to the fuzzified inputs
        # rule_evaluation(rules, fuzzySets)

        # 3. Aggregation of rule outputs
        # output_fuzzy_set = aggregate_outputs(fuzzySets)

        # 4. Defuzzification: Convert the result of fuzzy inference to a crisp output
        # crisp_value = defuzzification(output_fuzzy_set, list(fuzzySets.values())[0].x)

        # results[applicant.appId] = crisp_value  # Directly assigning the crisp value

        # reset_membership_degrees(fuzzySets)  # Reset membership degrees for the next application

    # Return the compiled results of all applications
        print(fuzzySets[1].memDegree)



def fuzzification(applicant, FuzzySetsDict):
    for var_value in applicant.data:  # var_value is a sub-list. (eg. [age, 35])
        variable, value = var_value[0], var_value[1]  # (eg. variable = Age, and value = 35)
        for fuzzySet in FuzzySetsDict.items():
            if fuzzySet[0].split('=')[0] == variable:
                # Update degree of membership in the set object´s memDegree attribute.
                fuzzySet[1].memDegree = skf.interp_membership(fuzzySet[1].x, fuzzySet[1].y, value)
        
#rules = readRulesFile()
#print(rules[1].antecedent)
#print(rules[1].consequent)

#applications = readApplicationsFile()
#print(applications[0].data[0][1])
main()


