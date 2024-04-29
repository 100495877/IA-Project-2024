import numpy as np
from MFIS_Read_Functions import readFuzzySetsFile, readRulesFile, readApplicationsFile
import skfuzzy as skf
from Main import evaluateApplication
from Main import fuzzification



        # Load the data
fuzzy_sets = readFuzzySetsFile()
rules = readRulesFile()
applications = readApplicationsFile()

        # Process the applications
results = evaluateApplication(fuzzy_sets, rules, applications)


def evaluateApplication(fuzzySets, rules, application):
    # Initialize a results dictionary


    # Process each application using the fuzzy logic
    for applicant in application:
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
    for var_value in applicant.data:  # var_value is a list of lists. (eg. [age, 35])
        variable, value = var_value[0], var_value[1]  # (eg. variable = Age, and value = 35)
        for fuzzySet in FuzzySetsDict.items():
            if fuzzySet[0] == variable:  # Match the application variable to the fuzzy set variable
                # Assuming linear membership within ranges defined by a, b, c, d
                if value < fuzzySet[1].x[0] or value > fuzzySet[1].x[-1]:
                    fuzzySet.memDegree = 0  # No membership if out of bounds
                #else:
                    #index = np.where(fuzzySet.x == value)[0][0]  # Find the index of the value in the x array
                    #fuzzySet.memDegree = fuzzySet.y[index]  # Membership degree corresponds to the y value

#rules = readRulesFile()
#print(rules[1].antecedent)
#print(rules[1].consequent)

#applications = readApplicationsFile()
#print(applications[0].data[0][1])
