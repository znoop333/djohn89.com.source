# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 06:34:28 2018

@author: djohn89
"""

import os

base_dir = r'C:\Users\djohn89\Documents\djohn89.com\rebuilt\djohn89.com.source'

os.chdir(base_dir)

import pelican

import bs4 
from bs4 import BeautifulSoup

import re

soup = BeautifulSoup(open("dave039sprogrammingblog.wordpress.2018-11-03.xml"), "html.parser")

import copy

#print(soup.prettify())

items = soup.find_all('item')

#%% skip all the extra junk at the start

out_dir = os.path.join(base_dir, 'source')

template = """<html>
    <head>
        <title>_TITLE_</title>
        <meta name="tags" content="_WP_ID_" />
        <meta name="date" content="_DATE_" />
        <meta name="category" content="programming" />
        <meta name="authors" content="DJ" />
        <meta name="summary" content="" />
    </head>
    <body>
    _BODY_
    </body>
</html>
"""

#    if item.title.text != 'Happy Cube Numbers':
#        continue

found_first_item = False

for item in items:
    post_id = item.find('wp:post_id').text
    title = item.title.text
    content = item.find('content:encoded').text
    content = content.replace('\n', '\n<br>')                       
    post_date = item.find('wp:post_date').text
    post_name = item.find('wp:post_name').text
    if item.title.text == 'Happy Cube Numbers':
        found_first_item = True
    
    if not found_first_item:
        continue
    
    # print(f"{post_id}, {post_date}, {post_name}, {title}, {content[:40]}")

    content1 = copy.copy(template).replace('_TITLE_', title).replace('_DATE_', post_date)
    content1 = content1.replace('_WP_ID_', post_id).replace('_BODY_', content)
    with open(os.path.join(out_dir, post_name + '.html'), 'w') as f:
        f.write(content1)
    
#.find(text=lambda tag: isinstance(tag, bs4.CData)).string.strip()

    



