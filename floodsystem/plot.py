from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):
    """ A function that displays a plot (using Matplotlib) of the water level
    data against time for a station, and includes on the plot lines for the
    typical low and high levels """
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()
