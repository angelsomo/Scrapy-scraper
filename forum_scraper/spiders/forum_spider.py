import scrapy


class ForumThreadSpider(scrapy.Spider):
    """
    Generic forum thread/comment crawler.

    Set start_urls to the forum section you want to crawl.
    """
    name = "forum_threads"

    start_urls = [
        "https://example.com/forum/section/",  # <-- replace with your target locally
    ]

    def parse(self, response):
        # Thread links (adjust selectors per forum theme)
        threads = response.xpath("//*[@class='ipsType_break ipsContained']")
        for thread in threads:
            thread_url = thread.xpath(".//a/@href").get()
            if thread_url:
                yield response.follow(thread_url, callback=self.parse_thread)

        next_page = response.css("li.ipsPagination_next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_thread(self, response):
        # Comment blocks (adjust selector per forum theme)
        comments = response.xpath("//*[@class='ipsColumn ipsColumn_fluid']")
        for comment in comments:
            text_parts = comment.xpath(".//*[@data-role='commentContent']//text()").getall()
            content = " ".join(t.strip() for t in text_parts if t.strip())

            if content:
                yield {
                    "thread_url": response.url,
                    "content": content,
                }

        next_page = response.css("li.ipsPagination_next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_thread)