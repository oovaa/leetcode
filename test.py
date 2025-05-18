import numpy as np

data = np.random.normal(
    5, 4, 10
)  # Create data with mean=5, std=1 5 is the center 4 is like the distanse from the center allwoed 10 is the numbers to generate
data = np.append(data, 200)  # Add an outlier at the end of the array

print(data)

mean = np.mean(data)
std_dev = np.std(data)
threshold = 3

lower = mean - threshold * std_dev
upper = mean + threshold * std_dev

outlaier = [x for x in data if x < lower or x > upper]


print(lower, upper, outlaier)


# from matplotlib import legend
# import pandas as pd
# import numpy as np

# import matplotlib.pyplot as plt


# x = np.linspace(0, 10, 100)
# y = np.sin(x) + np.random.normal(0, 0.3, size=x.shape)


# window_size = 4
# y_smooth = pd.Series(y).rolling(window=window_size, center=True).mean()

# plt.plot(x, y, label="Noisy")
# plt.plot(x, y_smooth, color="red", label="smoothed")

# plt.legend()
# plt.show()
