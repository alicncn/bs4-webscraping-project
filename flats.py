import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def scrape_real_estate_data(url):
    """Scrapes real estate data from the given URL and returns a DataFrame.

    Args:
        url (str): The URL of the ss.com

    Returns:
        pd.DataFrame: A DataFrame containing the scraped data.
    """

    response = requests.get(url)
    soup = bs(response.content, 'html.parser')

    # Extract data from HTML elements
    listings = soup.find_all('td', class_='msga2-o pp6')
    data = []
    for i in range(0, len(listings), 7):
        data.append({
            'Street': listings[i].text,
            'Rooms': int(listings[i + 1].text),
            'm²': int(listings[i + 2].text),
            'Floor': listings[i + 3].text,
            'Series': listings[i + 4].text,
            'm² Price': str(listings[i + 5].text[:-1].replace(',', '.')),
            'Price': str(listings[i + 6].text.replace('€/mon.', '').replace('€', '').replace(',', '.'))
        })

    # Create DataFrame and format columns
    df = pd.DataFrame(data)
    df.columns = ['Street', 'Rooms', 'm²', 'Floor', 'Series', 'm² Price', 'Price']

    return df


if __name__ == '__main__':
    base_url = 'https://www.ss.com/en/real-estate/flats/riga/centre/hand_over/page{}.html'
    all_data = []

    for page_number in range(1, 5):  # Iterate through 22 pages
        url = base_url.format(page_number)
        print(f"Scraping page {page_number}...")
        df = scrape_real_estate_data(url)
        all_data.append(df)

    # Concatenate DataFrames from all pages
    complete_df = pd.concat(all_data, ignore_index=True)

    # Further processing or saving the complete DataFrame
    complete_df.to_csv('centre_flats.csv')
