import datetime


def make_url_with_current_year_month(url_text):
    now = datetime.datetime.now()
    year_text = str(now.year)
    month = now.month
    if month < 10:
        month_text = "0" + str(month)
    else:
        month_text = str(month)

    url = url_text + year_text + "/" + month_text + "/"
    print(url)
    return url



