import matplotlib.pyplot as plt


# Define the carbon emission values for each factor
emission_values = {
    'transportation': 2.5,  # kg CO2 per mile
    'energy_usage': 0.8,  # kg CO2 per kWh
    'diet': 3.1,  # kg CO2 per day
    'waste_management': 0.2  # kg CO2 per pound of waste
}

# Get user inputs for each factor
transportation_distance = float(input("Enter transportation distance (in miles): "))
energy_consumption = float(input("Enter energy consumption (in kWh): "))
diet_emissions = float(input("Enter diet emissions (in kg CO2 per day): "))
waste_weight = float(input("Enter waste weight (in pounds): "))

# Calculate carbon emissions for each factor
transportation_emissions = transportation_distance * emission_values['transportation']
energy_emissions = energy_consumption * emission_values['energy_usage']
diet_emissions = diet_emissions * emission_values['diet']
waste_emissions = waste_weight * emission_values['waste_management']

# Calculate the total carbon footprint
total_carbon_footprint = transportation_emissions + energy_emissions + diet_emissions + waste_emissions

# Print the total carbon footprint
print("Your total carbon footprint is:", total_carbon_footprint, "kg CO2")


# Define the factors and their corresponding emissions
factors = ['Transportation', 'Energy Usage', 'Diet', 'Waste Management']
emissions = [transportation_emissions, energy_emissions, diet_emissions, waste_emissions]

# Create a bar chart to show the breakdown of emissions by factor
plt.bar(factors, emissions, color='blue')
plt.xlabel('Factors')
plt.ylabel('Carbon Emissions (kg CO2)')
plt.title('Carbon Footprint Breakdown by Factor')
plt.show()

# Display the overall carbon footprint score
print("Your total carbon footprint is:", total_carbon_footprint, "kg CO2")
