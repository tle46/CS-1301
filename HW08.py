"""
Georgia Institute of Technology - CS1301
HW08 -  API
"""

import requests

#########################################

"""
Function Name: averagePopulation()
Parameters: regionalBloc(str)
Returns: average population(float)
"""
def averagePopulation(regionalBloc):
    response = requests.get("https://restcountries.com/v2/regionalbloc/{}".format(regionalBloc))
    totalPop = 0
    countryCount = 0
    for country in response.json():
        totalPop += country["population"]
        countryCount += 1
    return round(totalPop/countryCount, 2)

#########################################

"""
Function Name: commonCountries()
Parameters: langTup1(tuple), langTup2(tuple)
Returns: list of countries(list)
"""
def commonCountries(langTup1, langTup2):
    response = requests.get("https://restcountries.com/v2/lang/{}".format(langTup2[0]))
    countryList = []
    for country in response.json():
        languageList = []
        for language in country["languages"]:
            languageList.append(language["name"])
        if langTup1[1] in languageList:
            countryList.append(country["name"])
        countryList.sort()
    return countryList
    
#########################################

"""
Function Name: uniqueRegions()
Parameters: countryList(list)
Returns: True or False(bool) or Error Message(str)
"""
def uniqueRegions(countryList):
    try:
        response = (requests.get("https://restcountries.com/v2/alpha/{}".format(countryList[0])))
        pastRegion = response.json()["region"]
        isUnique = False
        for country in countryList:
            response = requests.get("https://restcountries.com/v2/alpha/{}".format(country))
            infoDict = response.json()
            if infoDict["region"] != pastRegion:
                isUnique = True
        return isUnique
    except:
        return "Invalid country code!"        

#########################################

"""
Function Name: organizeCapitals()
Parameters: capitalList(list)
Returns: Dictionary mapping regions to a list of countries(dict)
"""
def organizeCapitals(capitalList):
    regionDict = {}
    for capital in capitalList:
        try:
            response = requests.get("https://restcountries.com/v2/capital/{}".format(capital))
            infoDict = response.json()[0]
            try:
                regionDict[infoDict["region"]] += [infoDict["name"],]
            except:
                regionDict[infoDict["region"]] = [infoDict["name"]]
        except:
            continue
    return regionDict

#########################################

"""
Function Name: visitableCountries()
Parameters: countryCodeList(list)
Returns: list of country names(list)
"""
def visitableCountries(countryCodeList):
    countryList = []
    for index, countryCode in enumerate(countryCodeList):
        response = requests.get("https://restcountries.com/v2/alpha/{}".format(countryCode))
        infoDict = response.json()            
        if index == 0:            
            countryList.append(infoDict["name"])            
            pastCountry = infoDict["alpha3Code"]
        else:
            if pastCountry in infoDict["borders"]:
                countryList.append(infoDict["name"])
                pastCountry = infoDict["alpha3Code"]
            else:
                break
    return countryList



