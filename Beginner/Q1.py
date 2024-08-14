def consultadd_python_training(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Consultadd - Python Training"
    elif n % 3 == 0:
        return "Consultadd"
    elif n % 5 == 0:
        return "Python Training"
    else:
        return ""

# Example usage
print(consultadd_python_training(15))
