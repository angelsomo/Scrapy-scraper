# Forum Thread Scraper (Scrapy)

A lightweight **Scrapy** project that crawls a forum section, follows thread links, and extracts comment text into structured outputs (JSON/CSV).

This repository is a cleaned-up, reproducible version of a crawler originally built for research/data collection workflows.

---

## What it does

- Starts from a forum “section” page (a listing of threads)
- Follows thread URLs
- Extracts comment text from each thread page
- Follows pagination on:
  - the thread listing pages
  - the thread pages themselves
- Exports scraped content using Scrapy feed exports

---

## Output schema

Each scraped comment is emitted as:

- `thread_url`: the URL of the thread the comment belongs to
- `content`: the extracted comment text (normalized to a single string)

Example:

```json
{
  "thread_url": "https://example.com/forum/thread/123",
  "content": "Example comment text..."
}
```

---

## Installation

```
pip install -r requirements.txt
```

---

## Usage

1. Edit the spider and set start_urls to your target forum section URL:

- `forum_scraper/spiders/forum_spider.py`

2. Run the spider and export to JSON:

```bash
scrapy crawl forum_threads -O output.json
```

3. Export to CSV:

```bash
scrapy crawl forum_threads -O output.csv
```

---

## Responsible crawling

When crawling third-party sites:

- Respect site Terms of Service
- Consider robots.txt and rate limits
- Use conservative concurrency and download delays
- Avoid unnecessary load on servers

Default settings in this repo are intentionally conservative.

---

## Project structure

```bash
forum_scraper/
  spiders/
    forum_spider.py
  settings.py
  pipelines.py
  items.py
```

---

## Possible improvements

- Make selectors configurable per forum engine/theme
- Add lightweight tests for parsing logic (HTML fixtures)
- Capture additional fields (author, timestamp, post URL)
- Add incremental crawling/checkpointing