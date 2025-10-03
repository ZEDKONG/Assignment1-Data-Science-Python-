import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Data Preparation ---

# Data from the provided image
data = {
    'month': ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019'],
    'Searches': [50, 53, 59, 56, 62],
    'Direct': [39, 47, 42, 51, 51],
    'Social Media': [70, 80, 90, 87, 92]
}

df = pd.DataFrame(data)

# --- 2. Plotting Setup ---

# number of groups (months) and the bar width
n_groups = len(df['month'])
bar_width = 0.25

# Create the index for the x-axis positions
index = np.arange(n_groups)

# colors for each traffic source
colors = {
    'Searches': '#4FA7D8',  # Blue
    'Direct': '#E87D9A',    # Pink/Red
    'Social Media': '#FFC700' # Yellow/Orange
}

# Set the figure size
plt.figure(figsize=(10, 6))

# --- 3. Creating the Bars ---

# Position for 'Searches' bars
rects1 = plt.bar(index, df['Searches'], bar_width,
                 label='Searches', color=colors['Searches'])

# Position for 'Direct' bars (shifted right by one bar width)
rects2 = plt.bar(index + bar_width, df['Direct'], bar_width,
                 label='Direct', color=colors['Direct'])

# Position for 'Social Media' bars (shifted right by two bar widths)
rects3 = plt.bar(index + 2 * bar_width, df['Social Media'], bar_width,
                 label='Social Media', color=colors['Social Media'])


# --- 4. Adding Labels and Annotations ---

# Function to add the value labels on top of the bars
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate(f'{height:.0f}',
                     xy=(rect.get_x() + rect.get_width() / 2, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom',
                     fontsize=10) # Set font size smaller for better fit

# Apply the function to all bar groups
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

# --- 5. Customizing the Chart ---

# Title
plt.title('Visitors by web traffic sources', fontsize=14)

# Y-axis label and limits
plt.ylabel('visitors\nin thousands', rotation=0, ha='right', va='center', fontsize=12, labelpad=30)
plt.ylim(0, 110) # Set max Y-limit slightly higher than the max value (92)
plt.yticks(np.arange(0, 101, 20)) # Set ticks at 0, 20, 40, 60, 80, 100

# X-axis labels (centered under the groups of bars)
plt.xlabel('months', ha='right', va='center', fontsize=12, labelpad=10)
plt.xticks(index + bar_width, df['month']) # Center the ticks

# Remove the top and right spines (borders) for a cleaner look
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Add a slight gap at the bottom of the y-axis
plt.gca().set_ylim(bottom=-5)

# Legend at the bottom center, similar to the source image
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=3, frameon=False)

# Adjust layout to prevent labels from being cut off
plt.tight_layout()

# Display the chart
plt.show()

#ALFRED POLYCARP BSE-05-0203/204