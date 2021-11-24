import requests
import csv

def import_urls_from_csv(filename):
    # import URLs to check from a file to list
    urls = []
    with open(filename, 'r') as f:
        started = False
        for line in f:
            if started == False:
                started = True
            else:
                urls.append(line.strip())
    return urls


def check_status_codes(urls):
    # Check status codes per url
    results = {}
    for url in urls:
        try:
            r = requests.get(url)
            if r.status_code != 200:
                # Ignore noraml staus code 200
                results[url] = r.status_code
        except Exception as e:
            # Record any error
            results[url] = e
    return results


def save_to_file(results, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        started = False
        for key, value in results.items():
            if started == True:
                writer.writerow([key, value])
            else:
                writer.writerow(['url', 'status'])
                started = True
                writer.writerow([key, value])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    urls = import_urls_from_csv('urls.csv')
    results = check_status_codes(urls)
    save_to_file(results, 'output.txt')
