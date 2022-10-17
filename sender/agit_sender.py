import configparser
import requests
import json

_headers = {'Content-Type': 'Application/json'}

config = configparser.ConfigParser()
config.read("config.ini")
agit_url = config["AGIT"]["test"]


def send_message(message, webhook_url=agit_url, headers=None):
    payload = {"text": message[:50000]}
    if headers is not None:
        _headers.update(headers)
    return send(payload, webhook_url, _headers)


def send(payload, webhook_url, headers=None):
    if headers is not None:
        _headers.update(headers)
    return requests.post(webhook_url, data=json.dumps(payload), headers=_headers, verify=False)


def apply_h1(text):
    return f"# {text}\n"


def apply_h2(text):
    return f"## {text}\n"


def apply_bold(text):
    return f"*{text}*"


def apply_italic(text):
    return f"_{text}_"


def apply_strike(text):
    return f"~{text}~"


def apply_text_box(text):
    return "> " + text.replace("\n", "\n> ")


def apply_code_bock(text):
    return f"```\n{text}```\n"


def apply_inline(text):
    return f"`{text}`\n"


def apply_user_mention(text):
    return f"@{text} "


def apply_group_mention(text):
    return f"@@{text} "


def apply_hash_tag(text):
    return f"#{text.replace(' ', '_')}"


def apply_link_text(text, link):
    return f"[{text}]({link})"
