# Web Scraper for The Verge
This is a Python script that scrapes articles from The Verge website and stores them in both a CSV file and an SQLite database. The script can be run on a cloud service, such as AWS, to save the articles daily on the server in a SQL database.

## Setup
To run this script, you'll need Python 3 installed on your machine, as well as the following Python packages:

1. beautifulsoup4
2. requests
3. csv
4. sqlite3
5. datetime
You can install these packages using pip:

## bash
Copy code
pip install beautifulsoup4 requests csv sqlite3 datetime


## Usage
To use this script, you can follow these steps:

##Clone or download the repository to your local machine.
Navigate to the repository directory in your terminal or command prompt.
Run the following command to execute the script: 

## bash
Copy code
python scrape.py
This will scrape the articles from The Verge website and save them in a CSV file and an SQLite database in the same directory as the script.

# AWS Setup
To run this script on AWS, you can follow these steps:

1. Launch an EC2 instance on AWS.
2. Connect to the instance using SSH.
3. Install Python 3 and the required packages on the instance using the same steps as above.
4. Upload the scrape.py file to the instance using scp or a similar tool.
5. Run the script using the same command as above.
To save the articles daily on the server in a SQL database, you can set up a cron job on the EC2 instance to run the script at a specified time each day. Here's an example cron job that runs the script every day at 8am:

## ruby
Copy code
0 8 * * * /usr/bin/python3 /path/to/scrape.py
This will automatically execute the script each day at 8am and store the articles in the SQL database.

# Conclusion
That's it! This script can be used to scrape articles from The Verge website and store them in a CSV file and an SQLite database. By running it on a cloud service like AWS, you can save the articles daily on the server in a SQL database and ensure that you always have the latest data.
