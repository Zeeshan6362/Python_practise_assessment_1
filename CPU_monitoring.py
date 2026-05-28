# importing psutil for CPU monitoring and time for sleep intervals
import psutil
# importing time to allow for sleep intervals between CPU usage checks
import time
    
def monitor_cpu(threshold=80.0):
    """
    Monitors the local machine's CPU usage and alerts if it exceeds the threshold.
    """
    print("Monitoring CPU usage...")
    
    try:
        while True:
            # The interval=1 argument is crucial here. 
            # It compares system CPU times elapsed before and after 1 second, 
            # providing a highly accurate percentage.
            cpu_usage = psutil.cpu_percent(interval=1)
            
            if cpu_usage > threshold:
                print(f"Alert! CPU usage exceeds threshold: {cpu_usage}%")
                
    except KeyboardInterrupt:
        # Handles the manual interruption (e.g., pressing Ctrl+C) gracefully
        print("\nMonitoring interrupted by user. Exiting...")
        
    except Exception as e:
        # Catches any other unexpected exceptions during execution
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    # Call the function with the default threshold of 80%
    # You can change this value, e.g., monitor_cpu(threshold=90.0)
    monitor_cpu()