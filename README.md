1- Methodology
The analysis is divided into six main sections:

Data Collection:

Selenium was used to scrape eBay tech deals data. The script navigated through eBay's website, extracted product details (e.g., title, price, timestamp), and saved the data into a CSV file (ebay_tech_deals.csv).

The raw data was cleaned and processed using Python (clean_data.py) to handle missing values, format columns, and compute new features like discount_percentage.

Time Series Analysis:

The timestamp column was converted to datetime format, and the data was sorted by time.

The hour of the day was extracted, and the number of deals per hour was visualized using a bar chart.

Price and Discount Analysis:

The distribution of product prices was analyzed using histograms and boxplots.

A scatter plot was created to compare original_price and price.

The distribution of discount_percentage was visualized to understand how discounts vary.

Shipping Information Analysis:

The frequency of different shipping options was counted and visualized using a bar chart.

Text Analysis on Product Titles:

A set of keywords (e.g., "Apple", "Samsung", "Laptop") was defined, and their frequencies in the title column were counted and visualized.

Price Difference Analysis:

A new column for the absolute discount (original_price - price) was computed, and its distribution was visualized using a histogram.

Discount Analysis:

The dataset was sorted by discount_percentage, and the top 5 deals with the highest discounts were identified.

2- Key Findings
Time Series Analysis:

Data indicates that the highest number of deals occurs at 1 AM, with 150 deals, and the lowest is at 8 AM with no deals. There is a noticeable increase in deals during the evening hours, peaking at 9 PM with 21 deals. 

Price and Discount Analysis:

This distribution shows that the majority of products are priced in the lower range, with 30 products priced till 200. As the price increases, the number of products decreases, with only 5 products priced above $1000.

Shipping Information Analysis:

The majority of deals offer standard shipping options, with a smaller proportion offering free or expedited shipping.

Text Analysis on Product Titles:

This indicates that "apple" is the most frequently used keyword in product titles, followed by "samsung" and "laptop." 


3- Challenges Faced
Missing Data:

The original_price column was missing in the raw dataset, requiring the creation of this column and handling of missing values.

Some shipping information was missing or incomplete, which was replaced with a default message.

Data Cleaning:

The price and original_price columns required cleaning (e.g., removing "US $" and commas) before analysis.

Outliers:

Extreme values in the price and discount_percentage columns required careful handling to avoid skewing the analysis.

Text Analysis:

Case-insensitive keyword matching was necessary to ensure accurate counts of keyword frequencies.

4- Potential Improvements
Advanced Time Series Analysis:

Analyze trends over days to identify seasonal patterns in deal frequency.

Categorical Analysis:

Group products by category and analyze price and discount trends within each category.

