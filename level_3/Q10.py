# Q10.py
def customers_walking_away(N, sequence):
    computers = set()
    waiting_customers = set()

    for customer in sequence:
        if customer not in computers:
            if len(computers) < N:
                computers.add(customer)
            else:
                waiting_customers.add(customer)
        else:
            computers.remove(customer)

    return len(waiting_customers)

# Example usage
if __name__ == "__main__":
    N = 3
    sequence = "GACCBDDBAGEE"
    walked_away = customers_walking_away(N, sequence)
    print("Number of customers who walked away:", walked_away)
