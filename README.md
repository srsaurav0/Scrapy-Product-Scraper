# Product Scraper Scrapy

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Run Application](#run-application)
- [Project Structure](#project-structure)

---

## Introduction

This project scrapes book data from the [books.toscrape.com](https://books.toscrape.com/) website, stores the data in a CSV file.

---

## Features

- Scrapes book titles, prices and ratings from website.
- Stores data in a csv file.

---

## Prerequisites

- Python 3.9+

---

## Setup and Installation

### Clone the repository:
   ```bash
   git clone https://github.com/srsaurav0/Scrapy-Product-Scraper.git
   cd Scrapy-Product-Scraper
   ```

### Create and activate a virtual environment:
- On Linux:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```
- On Windows:
  ```bash
  python -m venv .venv
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  .venv\Scripts\activate
  ```

### **Install Required Dependencies**
```bash
pip install -r requirements.txt
```

---

## Run Application

Run this command to scrape data into csv file:

```bash
scrapy crawl bookscraper
```

Executing this command will scrape the data and store it in **products.csv** file located in ***product_scraper/products.csv***.

---


## Project Structure

```bash
product_scrape
    ├── product_scraper
    │   ├── spiders
    │   │   └──bookscraper.py        # Scrapy spider to scrape data
    │   ├── items.py                 # Items for City and Hotel
    │   ├── middlewares.py           # Middlewares
    │   ├── pipelines.py             # Pipelines
    │   └── settings.py              # Settings
    ├── .gitignore                   # Gitignore file
    ├── products.csv                 # Output file
    ├── README.md                    # Project instructions
    ├── requirements.txt             # Required dependencies
    └── scrapy.cfg                   # Scrapy configuration parameter
```