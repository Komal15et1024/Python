import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a simple dataset
data = {'Name': ['Ko', 'An', 'Bh'], 'Score': [85, 90, 95]}
df = pd.DataFrame(data)

# Display the dataset
print(df)

# Plot the scores
plt.bar(df['Name'], df['Score'])
plt.title('Scores')
plt.show()
