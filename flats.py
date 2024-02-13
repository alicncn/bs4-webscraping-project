import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR)


def scrape_real_estate_data(url):
    """Scrapes real estate data from the given URL and returns a DataFrame.

    Args:
        url (str): The URL of the ss.com

    Returns:
        pd.DataFrame: A DataFrame containing the scraped data, or None if an error occurs.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = bs(response.content, 'html.parser')

        # Extract data from HTML elements
        listings = soup.find_all('td', class_='msga2-o pp6')
        data = []
        for i in range(0, len(listings), 7):
            try:
                data.append({
                    'Street': listings[i].text,
                    'Rooms': int(listings[i + 1].text),
                    'm²': int(listings[i + 2].text),
                    'Floor': listings[i + 3].text,
                    'Series': listings[i + 4].text,
                    'm² Price': str(listings[i + 5].text[:-1].replace(',', '.')),
                    'Price': str(listings[i + 6].text.replace('€/mon.', '').replace('€', '').replace(',', '.'))
                })
            except (ValueError, TypeError) as e:
                logging.error(f"Error parsing data: {e}, listing: {listings[i].text}")

        # Create DataFrame and format columns
        df = pd.DataFrame(data)
        df.columns = ['Street', 'Rooms', 'm²', 'Floor', 'Series', 'm² Price', 'Price']

        return df

    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL: {e}")
        return None


if __name__ == '__main__':
    base_url = 'https://www.ss.com/en/real-estate/flats/riga/vef/hand_over/page{}.html'
    all_data = []

    for page_number in range(1, 2):
        url = base_url.format(page_number)
        print(f"Scraping page {page_number}...")
        df = scrape_real_estate_data(url)
        if df is not None:
            all_data.append(df)

    # Concatenate DataFrames from all pages if data was successfully retrieved
    if all_data:
        complete_df = pd.concat(all_data, ignore_index=True)
        complete_df.to_excel('vef_rent.xlsx')
    else:
        print("Failed to scrape any data due to errors.")
