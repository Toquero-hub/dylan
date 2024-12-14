import multiprocessing  # Import the multiprocessing module for process management
import threading        # Import the threading module for thread management
import os              # Import os module to access operating system functionalities

def calculate_factorial(num):
    """Calculate and print the factorial of a number."""
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    # Print the factorial of the number along with thread name and process ID
    print(f"Factorial of {num} is {factorial} | Thread Name: {threading.current_thread().name} | PID: {os.getpid()}")

def thread_worker(numbers):
    """Create threads to perform factorial calculations on a list of numbers."""
    threads = []  # List to hold threads
    for num in numbers:
        t = threading.Thread(target=calculate_factorial, args=(num,))
        threads.append(t)  # Add the created thread to the list
        t.start()          # Start the thread
    
    # Wait for all threads to complete
    for t in threads:
        t.join()

def process_worker(numbers):
    """Divide work among processes for factorial calculations."""
    half = len(numbers) // 2  # Calculate halfway point of the list
    first_half = numbers[:half]  # First half of numbers for threading
    second_half = numbers[half:]  # Second half of numbers for multiprocessing

    # Create a process to handle threading for the first half
    thread_process = multiprocessing.Process(target=thread_worker, args=(first_half,))
    
    # Create a separate process for calculating factorials of the second half
    second_process = multiprocessing.Process(target=thread_worker, args=(second_half,))
    
    thread_process.start()  # Start the thread calculation process
    second_process.start()   # Start the second calculation process

    # Wait for both processes to complete before proceeding
    thread_process.join()
    second_process.join()

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]  # List of numbers to be processed
    print(f"Main Process ID: {os.getpid()}")  # Print the main process ID
    
    # Create a new process to handle calculations using the process_worker function
    p = multiprocessing.Process(target=process_worker, args=(numbers,))
    
    p.start()  # Start the process
    p.join()   # Wait for the process to complete before exiting
