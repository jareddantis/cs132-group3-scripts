# cs132-group3-scripts

Some scripts to help with Tweet data collection for CS 132.

## Prerequisites

You will need Python 3.8 or later (tested on 3.10). Create a virtualenv and run `pip install -r requirements.txt`.

You will also need a browser supported by [`webdriver_manager`](https://github.com/SergeyPirogov/webdriver_manager). The scripts explicitly use Google Chrome, but feel free to edit them if you prefer another browser. If you're using these scripts in WSL(2), install the browser **in WSL(2).** `webdriver_manager` might not work if you install the browser in Windows.

## Usage

1. Prepare a list of URLs to scrape. The format is one URL per line, for example:

        https://twitter.com/realDonaldTrump/status/1400000000000000000
        https://twitter.com/realDonaldTrump/status/1400000000000000001
        https://twitter.com/realDonaldTrump/status/1400000000000000002
    
    Make sure the URLs are valid and the Tweets are public. Remove any query parameters (e.g. `?s=20`) at the end of the URLs. Save this list to a file named `urls.txt`.
2. Run `python screenshot-tweets.py`. This will screenshot the Tweets and save them as PNG files named after their Tweet IDs. The output file will be overwritten if it already exists.
3. Run `python location-following-count.py`. This will extract data from the users who posted the Tweets and save it as `locations.tsv` (tab-separated values for user locations) and `following-count.csv` (comma-separated values for following counts). The output files will be overwritten if they already exist.

## License
    Copyright (C) 2023 Juris Hannah Adorna, Aurel Jared Dantis, Michael Benjamin Morco

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.