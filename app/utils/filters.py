def format_date(date):
    # format date to me month/day/year
    return date.strftime('%m/%d/%y')


def format_url(url):
    # keeps only the domain name in the url
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]


def format_plural(amount, word):
    if amount != 1:
        return word + 's'

    return word