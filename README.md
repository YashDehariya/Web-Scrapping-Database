# Amazon Product Scraper

This project is a Python script that scrapes product information from Amazon product pages. It extracts details like product title, price, rating, review count, and availability.

## How it Works

The script reads a list of Amazon product URLs from a file named `url.txt`. For each URL, it fetches the product page, parses the HTML content using BeautifulSoup, and extracts the desired information. The scraped data is then appended to a CSV file named `out.csv`.

## Prerequisites

- Python 3
- `requests` library
- `beautifulsoup4` library
- `lxml` library (or another HTML parser compatible with BeautifulSoup)

## Installation

1.  **Clone the repository (or download the files):**
    ```bash
    # If it were a git repo
    # git clone <repository_url>
    # cd <repository_name>
    ```
    For now, just ensure you have `main.py` and `url.txt` in the same directory.

2.  **Install dependencies:**
    Open your terminal and run:
    ```bash
    pip install requests beautifulsoup4 lxml
    ```

## Usage

1.  **Prepare `url.txt`:**
    Create a file named `url.txt` in the same directory as `main.py`. Add one Amazon product URL per line in this file. For example:
    ```
    https://www.amazon.in/AULA-F75-Mechanical-Swappable-Pre-lubed/dp/B0CYZHC69C/
    https://www.amazon.in/Logitech-Superlight-Lightspeed-Lightweight-Programmable/dp/B0CGDZC2FK/
    ```

2.  **Run the script:**
    Open your terminal in the directory containing `main.py` and `url.txt`, and run:
    ```bash
    python main.py
    ```

3.  **View output:**
    After the script finishes, you will find a file named `out.csv` in the same directory. This file contains the scraped product data in CSV format, with the following columns:
    `Title,Price,Rating,Review Count,Availability`

## Output File (`out.csv`)

The `out.csv` file will store the scraped data. Each row corresponds to a product, and the columns are:

1.  **Product Title:** The name of the product.
2.  **Price:** The price of the product (currency symbol might be included depending on the page).
3.  **Overall Rating:** The average customer rating (e.g., "4.5 out of 5 stars").
4.  **Total Reviews:** The total number of customer reviews.
5.  **Availability:** The availability status of the product (e.g., "In Stock.").

If any information cannot be found on the product page, "NA" will be recorded in the respective field.

## Important Notes

*   **User-Agent:** The script uses a default User-Agent string. Amazon might block requests if it detects unusual traffic. You can change the User-Agent in `main.py` if needed.
*   **Website Structure Changes:** Web scraping is sensitive to changes in website structure. If Amazon changes the layout of their product pages, this script might need to be updated to correctly find the data elements.
*   **Rate Limiting/Blocking:** Scraping websites frequently can lead to your IP address being temporarily or permanently blocked. Be respectful of the website's terms of service and avoid sending too many requests in a short period.
*   **Legality and Ethics:** Always ensure your web scraping activities are legal and ethical. Respect `robots.txt` files and the website's terms of service. This script is provided for educational purposes.

## To Do / Potential Improvements

*   Add error handling for network issues.
*   Implement configurable delays between requests to avoid IP blocking.
*   Allow a User-Agent to be passed as a command-line argument.
*   Support for more e-commerce websites.
*   Option to specify output file name.
*   Clearer logging.
