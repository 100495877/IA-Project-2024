import numpy as np
from MFIS_Read_Functions import readFuzzySetsFile, readRulesFile, readApplicationsFile
import skfuzzy as skf
from Main import evaluateApplication
from Main import fuzzification



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
        print (fuzzySets[1].memDegree)


def fuzzification(applicant, FuzzySetsDict):
    k = 1
    for var_value in applicant.data:  # var_value is a list of lists. (eg. [age, 35])
        print(k,"th iteration. the var_value = ", var_value)
        variable, value = var_value[0], var_value[1]  # (eg. variable = Age, and value = 35)
        for fuzzySet in FuzzySetsDict.items():
            print("This is the fuzzy set of",fuzzySet[0])
            print("And the fuzzy set object is", fuzzySet[1])
            print("And fuzzySet[1].x is", fuzzySet[1].x)
            if fuzzySet[0].split('=')[0] == variable:  
                # Match the application variable to the fuzzy set variable
                # We split the string, so that we only get the variable part (eg. "Age", instead of "Age=young")
                if value < fuzzySet[1].x[1] or value > fuzzySet[1].x[4]:
                    print("fuzzySet[1].x[1] is ", fuzzySet[1].x[1], "and fuzzySet[1].x[4] is ", fuzzySet[1].x[4])
                    print("The var_value", var_value,"of", variable, "is out of bounds")
                    fuzzySet[1].memDegree = 0  # No membership if out of bounds
                    print("memdegree of fuzzyset", fuzzySet, "was put as 0.")
                #else:
                    #index = np.where(fuzzySet.x == value)[0][0]  # Find the index of the value in the x array
                    #fuzzySet.memDegree = fuzzySet.y[index]  # Membership degree corresponds to the y value
        k += 1
#rules = readRulesFile()
#print(rules[1].antecedent)
#print(rules[1].consequent)

#applications = readApplicationsFile()
#print(applications[0].data[0][1])
main()