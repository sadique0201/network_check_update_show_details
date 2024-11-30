import time
import psutil

def monitor_traffic(interface='Wi-Fi'):
    while True:
        net_io = psutil.net_io_counters(pernic=True)
        traffic = net_io[interface].bytes_sent + net_io[interface].bytes_recv
        if is_high_traffic(traffic):
            print("Unusually high traffic detected!")
        time.sleep(60)  # Monitor every 60 seconds

def is_high_traffic(traffic, threshold=1000000):  #  threshold
    return traffic > threshold


monitor_traffic()
