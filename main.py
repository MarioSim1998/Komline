import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a mock dataset
data = pd.DataFrame({
    'year': [2017, 2018, 2019, 2020],
    'annual_projects': [50, 55, 60, 65],
    'annual_customers': [100, 110, 120, 130],
    'gross_margin': [0.35, 0.34, 0.26, 0.37],
    'revenue': [5381, 7682, 8345, 9845],
    'net_income': [750, 1445, 1068, 2456]
})

# Set the title of the app
st.title('Business Intelligence Dashboard')

# Assumptions
st.subheader('Assumptions')
growth_rate_projects = st.slider('Growth Rate for Annual Projects', 0.0, 1.0, 0.05)
growth_rate_customers = st.slider('Growth Rate for Annual Customers', 0.0, 1.0, 0.05)
growth_rate_margin = st.slider('Growth Rate for Gross Margin', 0.0, 1.0, 0.05)
growth_rate_revenue = st.slider('Growth Rate for Revenue', 0.0, 1.0, 0.05)
growth_rate_income = st.slider('Growth Rate for Net Income', 0.0, 1.0, 0.05)

# Calculate forecast
forecast_years = list(range(2021, 2026))
forecast_projects = data['annual_projects'].iloc[-1] * (1 + growth_rate_projects) ** np.arange(1, 6)
forecast_customers = data['annual_customers'].iloc[-1] * (1 + growth_rate_customers) ** np.arange(1, 6)
forecast_margin = data['gross_margin'].iloc[-1] * (1 + growth_rate_margin) ** np.arange(1, 6)
forecast_revenue = data['revenue'].iloc[-1] * (1 + growth_rate_revenue) ** np.arange(1, 6)
forecast_income = data['net_income'].iloc[-1] * (1 + growth_rate_income) ** np.arange(1, 6)

# Create forecast dataframe
forecast_data = pd.DataFrame({
    'year': forecast_years,
    'annual_projects': forecast_projects,
    'annual_customers': forecast_customers,
    'gross_margin': forecast_margin,
    'revenue': forecast_revenue,
    'net_income': forecast_income
})

# Display forecast graphs
st.subheader('Actual and Forecast Over Time')
fig, ax = plt.subplots()

# Create a secondary y-axis for 'gross_margin' and 'annual_customers'
ax2 = ax.twinx()

# Define colors for each metric
colors = {'Annual Projects': 'blue', 'Annual Customers': 'orange', 'Gross Margin': 'green', 'Revenue': 'red', 'Net Income': 'purple'}

# Plot actual data
ax.plot(data['year'], data['annual_projects'], label='Annual Projects', color=colors['Annual Projects'])
ax2.plot(data['year'], data['annual_customers'], label='Annual Customers', color=colors['Annual Customers'])
ax.plot(data['year'], data['revenue'], label='Revenue', color=colors['Revenue'])
ax.plot(data['year'], data['net_income'], label='Net Income', color=colors['Net Income'])

# Plot forecast data
ax.plot(forecast_data['year'], forecast_data['annual_projects'], color=colors['Annual Projects'], linestyle=':')
ax2.plot(forecast_data['year'], forecast_data['annual_customers'], color=colors['Annual Customers'], linestyle=':')
ax2.plot(forecast_data['year'], forecast_data['gross_margin'], color=colors['Gross Margin'], linestyle=':')
ax.plot(forecast_data['year'], forecast_data['revenue'], color=colors['Revenue'], linestyle=':')
ax.plot(forecast_data['year'], forecast_data['net_income'], color=colors['Net Income'], linestyle=':')

# Combine legends
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='center left', bbox_to_anchor=(1, 0.5))

st.pyplot(fig)


