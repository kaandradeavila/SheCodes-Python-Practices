# Display the total population such as, the total population is 203 million people
# Try to write code following best practices


def display_total_population_in_millions(populations):
  """
    This function formats and displays a population number in millions, such as:
    1,000,000 = 1 million
    """
  total_population = calculate_total_population(populations)
  total_population_in_millions = round(total_population / 1000000)

  print(
      f"The total population is {total_population_in_millions} million people."
  )


def calculate_total_population(populations):
  """
    This function converts population strings into integers and returns the total
    """
  total_population = 0

  for population in populations:
    total_population += int(population["population"])

  return total_population


# Initial data of populations
populations = [
    {
        'country': "France",
        "population": "60000000"
    },
    {
        'country': "Spain",
        "population": "50000000"
    },
    {
        'country': "USA",
        "population": "30000000"
    },
    {
        'country': "Australia",
        "population": "25000000"
    },
    {
        'country': "Canada",
        "population": "38000000"
    },
]

# Displaying the total population in the populations list
display_total_population_in_millions(populations)
