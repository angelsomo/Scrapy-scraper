import scrapy


class MotoSpiderClass(scrapy.Spider):
    name = "motoforum2"
    start_urls = [
        'https://www.mybike.gr/forum/109-%CE%BC%CE%BF%CF%84%CE%BF%CF%83%CE%B9%CE%BA%CE%BB%CE%AD%CF%84%CE%B5%CF%82-%CF%83%CF%84%CE%BF-garage/',
    ]

    def parse(self, response):
        threads = response.xpath("//*[@class='ipsType_break ipsContained']")
        for thread in threads:
            thread_absolute_link = thread.xpath(".//a/@href").extract_first()
            yield response.follow(thread_absolute_link, self.parse_thread)
        next_page_url = response.css('li.ipsPagination_next a::attr(href)').get()
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse)

    def parse_thread(self, response):
        comments = response.xpath("//*[@class='ipsColumn ipsColumn_fluid']")
        for comment in comments:
            content = "".join(comment.xpath(".//*[@data-role='commentContent']/p/text()").extract())
            yield {
                1: content
            }
        next_page_url2 = response.css('li.ipsPagination_next a::attr(href)').get()
        if next_page_url2 is not None:
            yield response.follow(next_page_url2, callback=self.parse_thread)
