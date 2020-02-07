# Realestate
This repository contains a set of Python scripts that scrape a real estate webpage, clean and analyze the data, plot visualizations, and perform a multiple linear regression fit.

See also the associated report featured on [Medium - Towards Data Science](https://towardsdatascience.com/house-hunting-in-the-san-francisco-bay-area-deal-hunting-using-machine-learning-3ed6fc8e8991)

## Files

### Web scraping
* `scrapeweb.py`: uses *Requests* to connect to mlslistings, *BeautifulSoup* to pull verification token, *html* to get web content, *Re* to clean the results, and *Pandas* to store scraped content as a dataframe

* `getdata.py`: pulls zipcodes from .csv file, uses `webscrape` function defined in `scrapeweb.py` to scrape content from the webpage and store it in *Pandas* dataframe, and writes a .csv file with the scraped content

### Map plotting
* `plotmaps.py`: pulls .csv file with listing information, uses `price_quintiles` function in `calculatequintiles.py` to place listings into five bins by price, uses `cartoplot_x_price` (`x = bay, sf, eastbay, peninsula, southbay`) functions defined in `cartoplotfunctions.py` to plot data points on a map of the respective region. Also contains scripts to plot commute and school quality data using zip code shapefiles 

* `cartoplotfunctions.py`: pulls data from .csv file and city or zipcode borders from shapefile, uses *Matplotlib.pyplot* and *Cartopy* to plot maps with terrain background and bounded by given set of latitude, longitude coordinates for full Bay Area as well as sub-regions

### Boxplot plotting
* `plotboxplots.py`: pulls data from .csv file and selects cities of interest to plot price information with using *Seaborn* box + strip plots

### Data fitting 
* `fitdata.py`: pulls data from .csv file, filters outliers, uses *Statsmodels.formula.api* to perform ordinary least squares fit and summarize the result, uses *Sklearn.linear_model* to create price predictions using the fitted coefficients, and uses functions defined in `plotfunctions.py` to plot a histogram of the residuals

### Libraries
* [Requests](https://2.python-requests.org/en/master/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)
* [Html](https://pypi.org/project/html/)
* [Re](https://docs.python.org/3/library/re.html)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Cartopy](https://scitools.org.uk/cartopy/docs/latest/)
* [Seaborn](https://seaborn.pydata.org/)
* [Statsmodels](https://www.statsmodels.org/stable/index.html)
* [Scikit-learn](https://scikit-learn.org/stable/)

### Acknowledgement
Written by **Michael Boles** in summer of 2019 with help from the *StackOverflow* community.
