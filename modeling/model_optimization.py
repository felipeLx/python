# Load the data
x_data, y_data = load_data()

# Model the data with specified values for parameters a0, a1
y_model = model(x_data, a0=150, a1=25)

# Compute the RSS value for this parameterization of the model
rss = np.sum(np.square(y_data - y_model))
print("RSS = {}".format(rss))

"""
The value we compute for RSS is not meaningful by itself, but later it becomes meaningful in context when we compare it to other values of RSS computed for other parameterizations of the model. More on that next! Some notes about code style; notice you could have done the RSS calculation in a single line of python code, but writing functions than can be re-used is good practice. Notice also that we could have defined a parameter dictionary dict(a0=150, a1=25) and passed it into the model as model(x, **parameters) which would make it easier to pass around all the parameters together if we needed them for other functions
"""
# Complete function to load data, build model, compute RSS, and plot
def compute_rss_and_plot_fit(a0, a1):
    xd, yd = load_data()
    ym = model(xd, a0, a1)
    residuals = ym - yd
    rss = np.sum(np.square(residuals))
    summary = "Parameters a0={}, a1={} yield RSS={:0.2f}".format(a0, a1, rss)
    fig = plot_data_with_model(xd, yd, ym, summary)
    return rss, summary

# Chose model parameter values and pass them into RSS function
rss, summary = compute_rss_and_plot_fit(a0=150, a1=25)
print(summary)

# Loop over all trial values in a1_array, computing rss for each
a1_array = np.linspace(15, 35, 101)
for a1_trial in a1_array:
    y_model = model(x_data, a0=150, a1=a1_trial)
    rss_value = compute_rss(y_data, y_model)
    rss_list.append(rss_value)

# Find the minimum RSS and the a1 value from whence it came
rss_array = np.array(rss_list)
best_rss = np.min(rss_array) 
best_a1 = a1_array[np.where(rss_array==best_rss)]
print('The minimum RSS = {}, came from a1 = {}'.format(best_rss, best_a1))

# Plot your rss and a1 values to confirm answer
fig = plot_rss_vs_a1(a1_array, rss_array)

"""
The best slope is the one out of an array of slopes than yielded the minimum RSS value out of an array of RSS values. Python tip: notice that we started with rss_list to make it easy to .append() but then later converted to numpy.array() to gain access to all the numpy methods.
"""