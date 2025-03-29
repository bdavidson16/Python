This dataset is provided by the *[CDC](https://healthdata.gov/ASPR/COVID-19-Treatments/xkzp-zhs7/about_data)* and gives us information about treatments of COVID-19 in the United States. I used Python and SQL to find trends within this information. 

I feel that this analysis can be used by medical providers to know which products are available, especially in their area. This can encourage them to do more research based on these conclusions. Also, patients can use this information to understand their treatment options and understand why they are getting certain treatments over others. There are many other uses with this information, especially when looking at the trends this analysis shows.

## Data/Analysis Info:
The dataset provided included the pharmacy name/provider name, their location down to the latitude and longitude, and which type of treatments they prescribe. To keep the analysis more simple, I removed the details about the provider's location and only kept the state and zip. The dataset went down from *31* to *18* columns.

### Outline:
1. Intro
2. Cleaning
3. EDA
4. Conclusion

## Concluding Points from Analysis:

- USG Lagevrio is commonly prescribed in general pharmacies, such as CVS, Rite Aid, and Walgreens.
- USG Paxlovid is rarely prescribed at general pharmacies and usually administrated through health centers or clinics.
- Also, the amount of centers that do prescribe USG Paxlovid is less than half of those that prescribe USG Lagevrio.
- Commercial Paxlovid and Lagevrio is usually prescribed at general pharmacies, with Paxlovid being more popular as a commercial medication.

## For additional research:
[CDC - COVID-19 Treatments](https://www.cdc.gov/covid/treatment/index.html) 

[FDA - Know Your Treatment Options](https://www.fda.gov/consumers/consumer-updates/know-your-treatment-options-covid-19)
