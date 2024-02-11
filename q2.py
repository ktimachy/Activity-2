import matplotlib.pyplot as plt

def graphSnowfall(t):
    snowfall_ranges = {'0-10': 0, '11-20': 0, '21-30': 0, '31-40': 0, '41-50': 0}

    # Read data from the file and count snowfall accumulation in each range
    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())
            if snowfall >= 0 and snowfall <= 10:
                snowfall_ranges['0-10'] += 1
            elif snowfall >= 11 and snowfall <= 20:
                snowfall_ranges['11-20'] += 1
            elif snowfall >= 21 and snowfall <= 30:
                snowfall_ranges['21-30'] += 1
            elif snowfall >= 31 and snowfall <= 40:
                snowfall_ranges['31-40'] += 1
            elif snowfall >= 41 and snowfall <= 50:
                snowfall_ranges['41-50'] += 1

    # Extract keys and values for plotting
    ranges = list(snowfall_ranges.keys())
    counts = list(snowfall_ranges.values())

    # Plotting the bar chart
    plt.bar(ranges, counts, color='skyblue')

    # Adding labels and title
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')

    # Display the bar chart
    plt.show()
    plt.savefig('plot.png') 



graphSnowfall('q2.txt')