# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:25:41 2021

@author: win10
"""

from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphones"

wanted_list=["₹58,400","New Apple iPhone 11 (128GB) - Black"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))

# scraper.set_rule_aliases({'':'Title', 'rule':'Price'})
# scraper.keep_rules(['', ''])
# scraper.save('amazon_search')

