import time
import requests

def get_response_time(url, timeout=5):
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = "https://" + url
    try:
        start = time.perf_counter()
        response = requests.get(url, timeout=timeout)
        end = time.perf_counter()
        return round(end - start, 3)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

'''
if __name__ == "__main__":
    websites_to_monitor = [
        "google.com",
        "openai.com",
        "medium.com"
    ]
    
    for website in websites_to_monitor:
        response_time = get_response_time(website)
        if response_time is not None:
            print(f"{website} - Response Time: {response_time} seconds")
        else:
            print(f"{website} - No response or timeout")
            '''
