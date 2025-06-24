import json 
import re 
from collections import Counter, defaultdict
from datetime import datetime 


def analyze_logs(log_file):
    """
    Analyze load balancer logs to extract specific information
    
    Args:
        logs_file(str): Path to the logs file
    
    Returns:
        dict: Analysis results
        
    """

    # init counters and data structures
    total_requests = 0
    redirected_requests = 0
    browsers = set()
    google_seo_requests = 0 
    requests_per_minute = defaultdict(int)
    potential_brute_force = defaultdict(lambda: defaultdict(int))

    # read logs file
    with open(logs_file, 'r') as f:
        for line in f:
            try:
                log_entry = json.loads(line)
                total_requests += 1

                # extract timestamp
                timestamp = log_entry.get('timestamp')
                if timestamp:
                    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    minute_key = dt.strftime('%Y-%M-%d %H:%M')
                    requests_per_minute[minute_key] += 1
                
                # check for redirected requests (status codes 3xx)
                status_code = log_entry.get('status_code')
                if status_code and 300 <= int(status_code) < 400:
                    redirected_requests += 1
                
                # extract browser information from user agent
                user_agent = log_entry.get('user_agent', '')
                if user_agent:
                    browser = extract_browser(user_agent)
                    if browser:
                        browsers.add(browser)
                
                # check for Google SEO bot
                if 'Googlebot' in user_agent or 'Google-Site-Verification' in user_agent:
                    google_seo_requests += 1
                    if status_code and int(status_code) in [403, 429, 503]:
                        google_seo_blocked += 1
                
                # check for potential brute force attempts
                client_ip = log_entry.get('client_ip')
                path = log_entry.get('path', '')
                if client_ip and '/login' or '/admin' in path:
                    potential_brute_force[client_ip][minute_key] += 1
            
            except json.JSONDecodeError:
                continue
    
    # analyze potential brute force attempts
    brute_force_attempts = []
    for ip, timestamp in potential_brute_force.items():
        for minute, count in timestamp.items():
            if count > 10: # threshold for suspicious activity
                brute_force_attempts.append({
                    'ip': ip, 
                    'minute': minute,
                    'attempts': count
                })
    
    # calculate percentage of redirected requests
    redirect_percentage = (redirected_requests / total_requests * 100) if total_requests> 0 else 0

    # calculate requests per minute statistics
    requests_per_minute_list = [
        {'minute': minute, 'count': count}
        for minute, count in sorted(requests_per_minute.items())
    ]

    return {
        'redirected_percentage': round(redirect_percentage, 2),
        'browers': sorted(list(browsers)),
        'google_seo_blocked': google_seo_blocked > 0,
        'brute_force_attmpts': brute_force_attempts,
        'requests_per_minute': requests_per_minute_list
    }


def extract_browser(user_agent):
    """
    Extract browser information from user agent string

    Args:
        user_agent (str): User agent string

    Returns:
        str: Browser name or None
    """
    
    browsers = {
        'Chrome': r'Chrome\/([0-9.]+)',
        'Firefox': r'Firefox\/([0-9.]+',
        'Safari': r'Safari\/([0-9.]+'
    }

    for browser, pattern in browsers.items():
        match = re.search(pattern, user_agent)
        if match:
            return browser
    
    return None

if __name__ == "__main__":
    results = analyze_logs('load_balancer_logs.json')
    print(f"Percentage of redirected requests: {results['redirect_percentage']}%")
    print(f"Browsers used: {', '.join(results['browsers'])}")
    print(f"Are Google SEO requests blocked? {'Yes' if results['google_seo_blocked'] else 'No'}")

    print("\nPotential brute force attempts:")
    for attempt in results['brute_force_attempts']:
        print(f"IP: {attempt['ip']}, Time: {attempt['minute']}, Attempts: {attempt[attempts]}")

        print("\nRequests Per Minute:")
        for rpm in results['requests_per_minute'][:5]: # show first 5 minutes
            print(f"{rpm['minute']}: {rpm['count']} requests")
