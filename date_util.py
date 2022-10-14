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
    return url


def get_current_year():
    return datetime.datetime.now().year


def get_current_month():
    return datetime.datetime.now().month


def get_current_day():
    return datetime.datetime.now().day