# Pattern printing with minimal loops
# Single loop solution - uses conditional to handle ascending and descending


print("\n TP 1 Exercies Number 1 :  \n")
# Exercise 1: Print a pattern of 'x' 

for i in range(1, 10):
    if i <= 5:
        print('x' * i)
    else:
        print('x' * (10 - i))


print("\n TP 1 Exercies Number 2 :  \n")
# Exercise 2: Extracting digits from a string

input_str = "n45as29@#8ss6"

digits = [char for char in input_str if char.isdigit()]
print("Extracted digits:", digits)

print("\n TP 1 Exercies Number 3 :  \n")
# Exercise 3: Convert integer to binary without using bin()

def int_to_binary(num):
    """Convert an integer to its binary representation as a string."""
    if num == 0:
        return "0"
    
    # Handle negative numbers
    is_negative = num < 0
    num = abs(num)
    
    # Convert to binary by repeatedly dividing by 2
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        #0 si num est pair
        #1 si num est impair
        num = num // 2
    
    return "-" + binary if is_negative else binary


# Test the function
test_numbers = [10, 255, 0, -5, 1024, 7]
for num in test_numbers:
    print(f"{num} -> {int_to_binary(num)}")

print("\n TP 1 Exercies Number 4 :  \n")
# Exercise 4: Fibonacci Sequence - Multiple Approaches

# Approach 1: Iterative (Most efficient)
def fibonacci_iterative(upper_threshold: int) -> list:
    """Generate Fibonacci numbers less than upper_threshold using iteration."""
    if upper_threshold <= 0:
        return []
    
    fib_list = [0]
    if upper_threshold <= 0:
        return []
    
    a, b = 0, 1
    while b < upper_threshold:
        fib_list.append(b)
        c = a + b
        a, b = b, c
    
    return fib_list


# Approach 2: Recursive with helper function
def fibonacci_recursive(upper_threshold: int) -> list:
    """Generate Fibonacci numbers less than upper_threshold using recursion."""
    def fib_helper(n: int) -> int:
        """Generate the nth Fibonacci number recursively."""
        if n <= 1:
            return n
        return fib_helper(n - 1) + fib_helper(n - 2)
    
    fib_list = []
    n = 0
    while True:
        fib_num = fib_helper(n)
        if fib_num >= upper_threshold:
            break
        fib_list.append(fib_num)
        n += 1
    
    return fib_list


# Approach 3: Memoization (Optimized Recursion)
def fibonacci_memoization(upper_threshold: int) -> list:
    """Generate Fibonacci numbers less than upper_threshold using memoization."""
    memo = {}
    
    def fib_helper(n: int) -> int:
        """Generate the nth Fibonacci number with memoization."""
        if n in memo:
            return memo[n]
        
        if n <= 1:
            return n
        
        memo[n] = fib_helper(n - 1) + fib_helper(n - 2)
        return memo[n]
    
    fib_list = []
    n = 0
    while True:
        fib_num = fib_helper(n)
        if fib_num >= upper_threshold:
            break
        fib_list.append(fib_num)
        n += 1
    
    return fib_list


# Test all three approaches
test_threshold = 10
print(f"Fibonacci numbers less than {test_threshold}:")
print(f"Iterative:    {fibonacci_iterative(test_threshold)}")
print(f"Recursive:    {fibonacci_recursive(test_threshold)}")
print(f"Memoization:  {fibonacci_memoization(test_threshold)}")

print(f"\nFibonacci numbers less than 100:")
print(f"Iterative:    {fibonacci_iterative(100)}")
print(f"Recursive:    {fibonacci_recursive(100)}")
print(f"Memoization:  {fibonacci_memoization(100)}")


print("\n TP 1 Exercies Number 4 :  \n")


# Exercise 5: Rock-Paper-Scissors Game


import random

def rock_paper_scissors(n: int) -> None:
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    for round_number in range(1, n + 1):
        print(f"\nRound {round_number}")
        
        computer = random.choice(choices)
        user = input("Choose rock, paper, or scissors: ").lower()
        
        if user not in choices:
            print("Invalid choice. Round skipped.")
            continue
        
        print(f"Computer chose: {computer}")
        
        if user == computer:
            print("It is a tie")
        elif (
            (user == "rock" and computer == "scissors") or
            (user == "paper" and computer == "rock") or
            (user == "scissors" and computer == "paper")
        ):
            print("You win this round")
            user_score += 1
        else:
            print("You lose this round")
            computer_score += 1
        
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
    
    # Final result
    print("\nFinal Result:")
    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("You lose the game!")
    else:
        print("It is a tie!")

#rock_paper_scissors(5)

#Exercise 2.1
# Compare linear and non-linear models, and avoid choosing parameters "at random".
import numpy as np
import time

def create_array_nxn(n: int) -> np.ndarray:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    return np.arange(n*n - 1, -1, -1).reshape(n, n)


def apply_threshold_loop(arr: np.ndarray, threshold: int) -> np.ndarray:
    result = arr.copy()
    
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i, j] < threshold:
                result[i, j] = 0
                
    return result


def apply_threshold_vectorized(arr: np.ndarray, threshold: int) -> np.ndarray:
    result = arr.copy()
    result[result < threshold] = 0
    return result


def compare_performance(n: int, threshold: int) -> None:
    arr = create_array_nxn(n)
    
    # Loop version
    start = time.time()
    apply_threshold_loop(arr, threshold)
    end = time.time()
    loop_time = end - start
    
    # Vectorized version
    start = time.time()
    apply_threshold_vectorized(arr, threshold)
    end = time.time()
    vector_time = end - start
    
    print(f"Loop version time: {loop_time:.6f} seconds")
    print(f"Vectorized version time: {vector_time:.6f} seconds")

#Exercice 2.2

import matplotlib.pyplot as plt

def show_in_digi(input_integer: int) -> None:
    numbs = {
        "1": np.array([[0,1,1],[1,0,1],[0,0,1],[0,0,1],[0,0,1]]),
        "2": np.array([[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]),
        "3": np.array([[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]),
        "4": np.array([[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]),
        "5": np.array([[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]),
        "6": np.array([[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]),
        "7": np.array([[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]),
        "8": np.array([[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]),
        "9": np.array([[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]),
        "0": np.array([[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]])
    }
    
    digits = str(input_integer)
    display = []
    
    for d in digits:
        display.append(numbs[d])
        display.append(np.zeros((5,1)))  # space between digits
    
    final_display = np.concatenate(display[:-1], axis=1)
    
    # plt.imshow(final_display, cmap="gray")
    # plt.axis("off")
    # plt.show()

    plt.figure(figsize=(10,3))
    plt.imshow(final_display, cmap="binary", interpolation="nearest")
    plt.axis("off")
    plt.show()

    #Exercice 2.2 advanced
def show_in_digi(input_number) -> None:
    numbs = {
        "1": np.array([[0,1,1],[1,0,1],[0,0,1],[0,0,1],[0,0,1]]),
        "2": np.array([[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]),
        "3": np.array([[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]),
        "4": np.array([[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]),
        "5": np.array([[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]),
        "6": np.array([[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]),
        "7": np.array([[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]),
        "8": np.array([[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]),
        "9": np.array([[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]),
        "0": np.array([[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]),
        "-": np.array([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]),
        ".": np.array([[0,0,0],[0,0,0],[0,0,0],[0,1,0],[0,1,0]])
    }
    
    digits = str(input_number)
    display = []
    
    for d in digits:
        display.append(numbs[d])
        display.append(np.zeros((5,1)))
    
    final_display = np.concatenate(display[:-1], axis=1)
    
    # plt.imshow(final_display, cmap="gray")
    # plt.axis("off")
    # plt.show()
    plt.figure(figsize=(10,3))
    plt.imshow(final_display, cmap="binary", interpolation="nearest")
    plt.axis("off")
    plt.show()

arr = create_array_nxn(4)
print(arr)

arr = create_array_nxn(4)
print(apply_threshold_loop(arr, 6))

arr = create_array_nxn(20)
r1 = apply_threshold_loop(arr, 50)
r2 = apply_threshold_vectorized(arr, 50)

print(np.array_equal(r1, r2))  # doit afficher True

compare_performance(800, 200000)



# show_in_digi(12345)
# show_in_digi(908)

# show_in_digi(-12.34)
# show_in_digi(0.5)
# show_in_digi(-0.01)

show_in_digi(0)
show_in_digi(8)
show_in_digi(123)
show_in_digi(-456)
show_in_digi(10.25)
show_in_digi(-0.75)



#Exercice 3
import pandas as pd
import matplotlib.pyplot as plt

# Charger le dataset (Colab)
df = pd.read_csv("/content/sample_data/california_housing_train.csv")

# 1) describe
print(df.describe())

# 2) lignes total_bedrooms > 310
print(df[df["total_bedrooms"] > 310])

# 3) supprimer 1ère + dernière ligne
df = df.iloc[1:-1].copy()

# 4) moyenne households + plot points + moyenne
m = df["households"].mean()

plt.figure(figsize=(10, 4))
plt.plot(df.index, df["households"], ".", markersize=2)   # points
plt.axhline(m, linewidth=2)                               # ligne moyenne
plt.xlabel("index")
plt.ylabel("households")
plt.show()

# 5) remplacer NaN par moyenne (par colonne)
df = df.fillna(df.mean(numeric_only=True))

# 6) plot lat/long
plt.figure(figsize=(6, 6))
plt.scatter(df["latitude"], df["longitude"], s=5)
plt.xlabel("lat")
plt.ylabel("long")
plt.show()

# 7) normaliser 2 colonnes (min-max)
for c in ["median_income", "total_rooms"]:
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())

# 8) matrice de corrélation
corr = df.corr(numeric_only=True)
print(corr)

# Tests rapides
assert df.isna().sum().sum() == 0, "Il reste des NaN"
assert (df["median_income"].min() >= 0) and (df["median_income"].max() <= 1), "median_income pas normalisé"
assert (df["total_rooms"].min() >= 0) and (df["total_rooms"].max() <= 1), "total_rooms pas normalisé"
assert corr.shape[0] == corr.shape[1], "corr doit être carrée"

print("✅ OK (tests passés)")