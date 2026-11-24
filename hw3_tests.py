import data
import build_data
import unittest


# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    # test population_total
    def test_population_total_known_counties(self):
        self.assertEqual(hw3.population_total(self.counties), 4000)
        self.assertEqual(hw3.population_total([self.first]), 1000)

    def test_population_total_empty(self):
        self.assertEqual(hw3.population_total([]), 0)
    # Part 2: filter_by_state

    def test_filter_by_state_matches(self):
        result = hw3.filter_by_state(self.counties, "CA")
        self.assertEqual(result, [self.first])
        self.assertIs(result[0], self.first)

        self.assertEqual(
            hw3.filter_by_state(self.counties, "NY"),
            [self.second]
        )

    def test_filter_by_state_no_match_or_empty(self):
        self.assertEqual(hw3.filter_by_state(self.counties, "TX"), [])
        self.assertEqual(hw3.filter_by_state([], "CA"), [])

    # Part 3: population estimates

    def test_population_by_education_known_values(self):
        # 1000 * 10% + 3000 * 30% = 1000 people.
        self.assertAlmostEqual(
            hw3.population_by_education(self.counties, EDUCATION),
            1000.0
        )
        self.assertAlmostEqual(
            hw3.population_by_education([self.first], EDUCATION),
            100.0
        )

    def test_population_by_education_missing_or_empty(self):
        self.assertEqual(
            hw3.population_by_education(self.counties, "missing"),
            0.0
        )
        self.assertEqual(
            hw3.population_by_education([], EDUCATION),
            0.0
        )

    def test_population_by_ethnicity_known_values(self):
        # 1000 * 20% + 3000 * 60% = 2000 people.
        self.assertAlmostEqual(
            hw3.population_by_ethnicity(self.counties, ETHNICITY),
            2000.0
        )
        self.assertAlmostEqual(
            hw3.population_by_ethnicity([self.first], ETHNICITY),
            200.0
        )

    def test_population_by_ethnicity_missing_or_empty(self):
        self.assertEqual(
            hw3.population_by_ethnicity(self.counties, "missing"),
            0.0
        )
        self.assertEqual(
            hw3.population_by_ethnicity([], ETHNICITY),
            0.0
        )

    def test_population_below_poverty_level_known_values(self):
        self.assertAlmostEqual(
            hw3.population_below_poverty_level(self.counties),
            1000.0
        )

    def test_population_below_poverty_level_single_or_empty(self):
        self.assertAlmostEqual(
            hw3.population_below_poverty_level([self.first]),
            100.0
        )
        self.assertEqual(
            hw3.population_below_poverty_level([]),
            0.0
        )

    # Part 4: population-weighted percentages

    def test_percent_by_education_weighted(self):
        # 1000 / 4000 * 100 = 25%, not an unweighted 20%.
        self.assertAlmostEqual(
            hw3.percent_by_education(self.counties, EDUCATION),
            25.0
        )
        self.assertAlmostEqual(
            hw3.percent_by_education([self.first], EDUCATION),
            10.0
        )

    def test_percent_by_education_missing_empty_or_zero(self):
        self.assertEqual(
            hw3.percent_by_education(self.counties, "missing"),
            0.0
        )
        self.assertEqual(
            hw3.percent_by_education([], EDUCATION),
            0.0
        )
        self.assertEqual(
            hw3.percent_by_education([self.zero], EDUCATION),
            0.0
        )

    def test_percent_by_ethnicity_weighted(self):
        self.assertAlmostEqual(
            hw3.percent_by_ethnicity(self.counties, ETHNICITY),
            50.0
        )
        self.assertAlmostEqual(
            hw3.percent_by_ethnicity([self.first], ETHNICITY),
            20.0
        )

    def test_percent_by_ethnicity_missing_empty_or_zero(self):
        self.assertEqual(
            hw3.percent_by_ethnicity(self.counties, "missing"),
            0.0
        )
        self.assertEqual(
            hw3.percent_by_ethnicity([], ETHNICITY),
            0.0
        )
        self.assertEqual(
            hw3.percent_by_ethnicity([self.zero], ETHNICITY),
            0.0
        )

    def test_percent_below_poverty_level_weighted(self):
        self.assertAlmostEqual(
            hw3.percent_below_poverty_level(self.counties),
            25.0
        )

    def test_percent_below_poverty_level_single_empty_or_zero(self):
        self.assertAlmostEqual(
            hw3.percent_below_poverty_level([self.first]),
            10.0
        )
        self.assertEqual(
            hw3.percent_below_poverty_level([]),
            0.0
        )
        self.assertEqual(
            hw3.percent_below_poverty_level([self.zero]),
            0.0
        )

    # Part 5: strict demographic thresholds

    def test_education_greater_than_matches(self):
        self.assertEqual(
            hw3.education_greater_than(self.counties, EDUCATION, 20.0),
            [self.second]
        )

    def test_education_greater_than_boundary_missing_or_empty(self):
        self.assertEqual(
            hw3.education_greater_than(self.counties, EDUCATION, 30.0),
            []
        )
        self.assertEqual(
            hw3.education_greater_than(self.counties, "missing", -1.0),
            []
        )
        self.assertEqual(
            hw3.education_greater_than([], EDUCATION, 20.0),
            []
        )

    def test_education_less_than_matches(self):
        self.assertEqual(
            hw3.education_less_than(self.counties, EDUCATION, 20.0),
            [self.first]
        )

    def test_education_less_than_boundary_missing_or_empty(self):
        self.assertEqual(
            hw3.education_less_than(self.counties, EDUCATION, 10.0),
            []
        )
        self.assertEqual(
            hw3.education_less_than(self.counties, "missing", 100.0),
            []
        )
        self.assertEqual(
            hw3.education_less_than([], EDUCATION, 20.0),
            []
        )

    def test_ethnicity_greater_than_matches(self):
        self.assertEqual(
            hw3.ethnicity_greater_than(self.counties, ETHNICITY, 40.0),
            [self.second]
        )

    def test_ethnicity_greater_than_boundary_missing_or_empty(self):
        self.assertEqual(
            hw3.ethnicity_greater_than(self.counties, ETHNICITY, 60.0),
            []
        )
        self.assertEqual(
            hw3.ethnicity_greater_than(self.counties, "missing", -1.0),
            []
        )
        self.assertEqual(
            hw3.ethnicity_greater_than([], ETHNICITY, 40.0),
            []
        )

    def test_ethnicity_less_than_matches(self):
        self.assertEqual(
            hw3.ethnicity_less_than(self.counties, ETHNICITY, 40.0),
            [self.first]
        )

    def test_ethnicity_less_than_boundary_missing_or_empty(self):
        self.assertEqual(
            hw3.ethnicity_less_than(self.counties, ETHNICITY, 20.0),
            []
        )
        self.assertEqual(
            hw3.ethnicity_less_than(self.counties, "missing", 100.0),
            []
        )
        self.assertEqual(
            hw3.ethnicity_less_than([], ETHNICITY, 40.0),
            []
        )

    def test_below_poverty_level_greater_than_matches(self):
        self.assertEqual(
            hw3.below_poverty_level_greater_than(self.counties, 20.0),
            [self.second]
        )

    def test_below_poverty_level_greater_than_boundary_or_empty(self):
        self.assertEqual(
            hw3.below_poverty_level_greater_than(self.counties, 30.0),
            []
        )
        self.assertEqual(
            hw3.below_poverty_level_greater_than([], 20.0),
            []
        )

    def test_below_poverty_level_less_than_matches(self):
        self.assertEqual(
            hw3.below_poverty_level_less_than(self.counties, 20.0),
            [self.first]
        )

    def test_below_poverty_level_less_than_boundary_or_empty(self):
        self.assertEqual(
            hw3.below_poverty_level_less_than(self.counties, 10.0),
            []
        )
        self.assertEqual(
            hw3.below_poverty_level_less_than([], 20.0),
            []
        )

    # Additional check for original objects and unchanged input.

    def test_filter_order_identity_and_input_unchanged(self):
        before = copy.deepcopy(
            [county.__dict__ for county in self.counties]
        )

        result = hw3.education_greater_than(
            self.counties, EDUCATION, 0.0
        )

        self.assertIsNot(result, self.counties)
        self.assertIs(result[0], self.first)
        self.assertIs(result[1], self.second)
        self.assertEqual(
            [county.__dict__ for county in self.counties],
            before
        )


if __name__ == "__main__":
    unittest.main()
