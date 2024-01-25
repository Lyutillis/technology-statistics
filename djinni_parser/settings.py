BOT_NAME = "djinni_parser"

SPIDER_MODULES = ["djinni_parser.spiders"]
NEWSPIDER_MODULE = "djinni_parser.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
