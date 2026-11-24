import data


def population_total(counties: list[data.CountyDemographics]) -> int:
    total = 0
    for county in counties:
        total += county.population["2014 Population"]
    return int(total)



def filter_by_state(
    counties: list[data.CountyDemographics], state: str
) -> list[data.CountyDemographics]:
    result = []
    for county in counties:
        if county.state == state:
            result.append(county)
    return result


def population_by_education(
    counties: list[data.CountyDemographics], key: str
) -> float:
    total = 0.0
    for county in counties:
        percentage = county.education.get(key, 0.0)
        total += county.population["2014 Population"] * percentage / 100
    return total



def population_by_ethnicity(
    counties: list[data.CountyDemographics], key: str
) -> float:
    total = 0.0
    for county in counties:
        percentage = county.ethnicities.get(key, 0.0)
        total += county.population["2014 Population"] * percentage / 100
    return total


def population_below_poverty_level(
    counties: list[data.CountyDemographics]
) -> float:
    total = 0.0
    for county in counties:
        percentage = county.income.get("Persons Below Poverty Level", 0.0)
        total += county.population["2014 Population"] * percentage / 100
    return total



def percent_by_education(
    counties: list[data.CountyDemographics], key: str
) -> float:
    total = population_total(counties)
    if total == 0:
        return 0.0
    return 100 * population_by_education(counties, key) / total



def percent_by_ethnicity(
    counties: list[data.CountyDemographics], key: str
) -> float:
    total = population_total(counties)
    if total == 0:
        return 0.0
    return 100 * population_by_ethnicity(counties, key) / total



def percent_below_poverty_level(
    counties: list[data.CountyDemographics]
) -> float:
    total = population_total(counties)
    if total == 0:
        return 0.0
    return 100 * population_below_poverty_level(counties) / total


def education_greater_than(
    counties: list[data.CountyDemographics], key: str, threshold: float
) -> list[data.CountyDemographics]:
    result = []
    for county in counties:
        if key in county.education and county.education[key] > threshold:
            result.append(county)
    return result


def education_less_than(
    counties: list[data.CountyDemographics], key: str, threshold: float
) -> list[data.CountyDemographics]:
    result = []
    for county in counties:
        if key in county.education and county.education[key] < threshold:
            result.append(county)
    return result


def ethnicity_greater_than(
    counties: list[data.CountyDemographics], key: str, threshold: float
) -> list[data.CountyDemographics]:
    result = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] > threshold:
            result.append(county)
    return result


def ethnicity_less_than(
    counties: list[data.CountyDemographics], key: str, threshold: float
) -> list[data.CountyDemographics]:
    result = []
    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] < threshold:
            result.append(county)
    return result


def below_poverty_level_greater_than(
    counties: list[data.CountyDemographics], threshold: float
) -> list[data.CountyDemographics]:
    result = []
    key = "Persons Below Poverty Level"
    for county in counties:
        if key in county.income and county.income[key] > threshold:
            result.append(county)
    return result


def below_poverty_level_less_than(
    counties: list[data.CountyDemographics], threshold: float
) -> list[data.CountyDemographics]:
    result = []
    key = "Persons Below Poverty Level"
    for county in counties:
        if key in county.income and county.income[key] < threshold:
            result.append(county)
    return result
