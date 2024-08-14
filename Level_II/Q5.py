# Q5.py
def analyze_temperatures(readings):
    average_temp = sum(readings) / len(readings)
    highest_temp = max(readings)
    lowest_temp = min(readings)
    return average_temp, highest_temp, lowest_temp

# Example usage
if __name__ == "__main__":
    temperature_readings = [25, 28, 21, 24, 27]
    avg, high, low = analyze_temperatures(temperature_readings)
    print(f"Average Temperature: {avg}")
    print(f"Highest Temperature: {high}")
    print(f"Lowest Temperature: {low}")
