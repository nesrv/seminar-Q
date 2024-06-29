# function generator random ip address

def random_ip():
    import random
    import socket
    import struct
    
    # Generate random IP address
    ip = socket.inet_ntoa(struct.pack('>I', random.randint(0, 0xFFFFFFFF)))
    print(ip)
    return ip


# def main():
#     print(random_ip())
    
 
def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


print(get_ip())


def yandex_search(query):
    import requests
    import json

    # Replace with your Yandex API key
    api_key = 'YOUR_API_KEY'

    # Replace with your search engine ID
    search_engine_id = 'YOUR_SEARCH_ENGINE_ID'

    # Construct the API request URL
    url = f'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX{query}&lr={search_engine_id}'

    # Make the API request
    response = requests.get(url)

    # Parse the search results
    results = json.loads(response.text)['items']

    # Print the search results
    for result in results:
        print(result['title'])
        print(result['url'])
        print('---')


