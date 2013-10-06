# Lexis Nexis Mass Emailer

This uses a headless browser to email mass news articles in Lexis Nexis's database regarding certain political subjects between specified date ranges to a randomly selected email addresses. This is because downloading files with a headlessbrowser is virtually impossible. It uses parallel processing to email the documents in parallel

## Caution

**Be careful when running multiple instances of this program. You may be blacklisted from Lexis Nexis. This has happened before!**

I successfully ran 3 instances of this script (12 concurrent threads, given the 4 cores) without getting black listed. Your mileage may vary. Just because you're running this on a university network does **NOT** mean your mass traffic will go unnoticed by Lexis Nexis.

## Programming style:

This was written primarily for personal use, so some conventions like line length limits are ignored.

## How to use

You will need to run this on a pre-authorized network like a university connection. You may try to use your university or institution's VPN to run this at home. This program accepts input from four text files, `1.txt`, `2.txt`, `3.txt`, and `4.txt`. Format of the text files should be as follows: `UnitedStates,('04/11/2002', '04/11/2002')`. Essentially `"countryname","tuple of date range"`. You will then want to download the files from the emails with `dl_attachments.py` and optionally rename the documents according to their contents with `rename.py`