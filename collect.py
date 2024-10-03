from bs4 import BeautifulSoup
import os
import pandas as pd

# Initialize a dictionary to store the extracted data
d = {'title': [], 'price': [], 'link': []}

# Loop through each HTML file in the data directory
for file in os.listdir("data"):
    try:
        with open(f"data/{file}", 'r', encoding='utf-8') as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')

        # Find the title element (modify the tag if needed)
        t = soup.find("span", attrs={"class": "a-size-medium"})  # Adjust class as per your HTML structure
        if t:
            title = t.get_text().strip()
        else:
            title = "N/A"

        # Find the link element (modify the tag if needed)
        l = soup.find("a", href=True)
        if l:
            link = "https://amazon.in" + l['href']
        else:
            link = "N/A"

        # Find the price element (modify the tag if needed)
        p = soup.find("span", attrs={"class": "a-price-whole"})
        if p:
            price = p.get_text().strip()
        else:
            price = "N/A"

        # Append the data to the dictionary
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Create a DataFrame from the dictionary
df = pd.DataFrame(data=d)

# Save the DataFrame to a CSV file
df.to_csv("data.csv", index=False)

print("Data extraction complete!")
