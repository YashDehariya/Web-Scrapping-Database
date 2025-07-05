# importing libraries
from bs4 import BeautifulSoup
import requests
import time
import random

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    # Add more user agents if needed
]

def main(URL):
    File = open("out.csv", "a")
    HEADERS = {
    'User-Agent': random.choice(USER_AGENTS),
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'DNT': '1',  # Do Not Track Request Header
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.google.com/'
    }

    # Making the HTTP Request
    webpage = requests.get(URL, headers=HEADERS)

    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # Check if request was successful
    if webpage.status_code != 200:
        print("Failed to retrieve page")
        File.write("NA,NA,NA,NA,NA,\n")
        File.close()
        return

    # Check for bot detection
    if "captcha" in webpage.text.lower():
        print("Blocked by Amazon (captcha detected)")
        File.write("NA,NA,NA,NA,NA,\n")
        File.close()
        return

    # retrieving product title
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_string = title.get_text(strip=True).replace(',', '') if title else "NA"
    except Exception:
        title_string = "NA"
    print("product Title = ", title_string)
    File.write(f"{title_string},")

    # retrieving price (try multiple selectors)
    price = "NA"
    price_selectors = [
        ("span", {"id": "priceblock_ourprice"}),
        ("span", {"id": "priceblock_dealprice"}),
        ("span", {"id": "priceblock_saleprice"}),
        ("span", {"class": "a-price-whole"}),
    ]
    for tag, attrs in price_selectors:
        price_tag = soup.find(tag, attrs=attrs)
        if price_tag:
            price = price_tag.get_text(strip=True).replace(',', '')
            break
    print("Products price = ", price)
    File.write(f"{price},")

    # retrieving product rating
    # retrieving product rating
    rating = "NA"
    try:
        # Try the most common location first
        rating_tag = soup.find("span", attrs={'class': 'a-icon-alt'})
        if rating_tag:
            rating = rating_tag.get_text(strip=True).replace(',', '')
        else:
            # Fallback: look for any element with class containing 'a-icon-alt'
            rating_tag = soup.find(attrs={'class': lambda x: x and 'a-icon-alt' in x})
            if rating_tag:
                rating = rating_tag.get_text(strip=True).replace(',', '')
    except Exception:
        rating = "NA"
    print("Overall rating = ", rating)
    File.write(f"{rating},")

    # retrieving review count
    try:
        review_tag = soup.find("span", attrs={'id': 'acrCustomerReviewText'})
        review_count = review_tag.get_text(strip=True).replace(',', '') if review_tag else "NA"
    except Exception:
        review_count = "NA"
    print("Total reviews = ", review_count)
    File.write(f"{review_count},")

    # print availability status
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").get_text(strip=True).replace(',', '') if available else "NA"
    except Exception:
        available = "NA"
    print("Availability = ", available)
    File.write(f"{available},\n")

    # saving the availability and closing the line
    File.write(f"{available},\n")

    # closing the file
    File.close()


if __name__ == '__main__':
    import time
    file = open("url.txt", "r")
    for links in file.readlines():
        main(links)
        time.sleep(random.randint(3, 7))