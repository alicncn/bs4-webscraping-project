This document provides a detailed explanation of the Python script for scraping real estate data from [ss.com](https://www.ss.com/).

### Code Structure

The script is organized into two main parts:

1. **`scrape_real_estate_data` function:** This function takes a URL as input and:
    - Fetches the HTML content using the `requests` library.
    - Parses the HTML using BeautifulSoup to extract relevant data from specific HTML elements.
    - Creates a dictionary for each listing containing Street, Rooms, m², Floor, Series, m² Price, and Price information.
    - Converts the data dictionary into a pandas DataFrame and formats the columns.
    - Returns the DataFrame containing the extracted data.

2. **Main section:**
    - Defines the base URL template with a placeholder for page numbers.
    - Employs a `for` loop to iterate through pages 1 to 5 (change the range as needed).
    - Calls the `scrape_real_estate_data` function for each page to fetch data.
    - Appends the resulting DataFrame from each page to a list `all_data`.
    - Concatenates all DataFrames in `all_data` into a single `complete_df`.
    - Saves the `complete_df` to a CSV file named `centre_flats.csv` (change the name if desired).

### Libraries Used

- `requests`: Used for making HTTP requests to fetch the HTML content.
- `BeautifulSoup`: Used for parsing the HTML content and extracting data.
- `pandas`: Used for creating and manipulating DataFrames to store and format the extracted data.

### Error Handling

- While not explicitly implemented in this version, consider adding error handling to manage potential issues like:
    - Network errors during requests.
    - Changes in website structure leading to incorrect data extraction.
    - Invalid data values that cannot be converted.

### Customization

- The script currently scrapes pages 1 to 5. Adjust the `range` in the `for` loop to scrape different page ranges.
- The base URL template (`hand_over`) targets listings marked as "hand over." To target other categories, change the URL accordingly.
- You can modify the scraping logic within the `scrape_real_estate_data` function to extract additional data or handle variations in the HTML structure.
- Remember to respect the website's terms of service and avoid excessive scraping that could overload their servers. Consider adding delays between requests if necessary.

### Additional Notes

- This code represents a basic example of web scraping. For more robust and scalable scraping, consider using dedicated scraping frameworks and libraries.
- Data scraping websites can change their structure and content over time. Be prepared to adapt the script accordingly.
- Ensure you have the necessary libraries (`requests`, `beautifulsoup4`, and `pandas`) installed before running the script.
