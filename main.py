import requests
import re
import time

def gen_random_email():
    cookies = {
        'cf_clearance': 'aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48',
        'cookie_csrf_token': 'cf21a948ae553e1f15314ede3546451b',
        'cookie_sessionhash': 'SHASH%3A22d720d51fee77ce82bbf25cba3cba57',
        'cookie_keepalive_insert': '1',
        'cookie_setlang': 'ja',
        'cookie_failedSlot': '',
        'cookie_last_page_addrlist': '0',
        'cookie_timezone': 'Asia%2FTokyo',
        'cookie_gendomainorder': 'instaddr.uk',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'cf_clearance=aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48; cookie_csrf_token=cf21a948ae553e1f15314ede3546451b; cookie_sessionhash=SHASH%3A22d720d51fee77ce82bbf25cba3cba57; cookie_keepalive_insert=1; cookie_setlang=ja; cookie_failedSlot=; cookie_last_page_addrlist=0; cookie_timezone=Asia%2FTokyo; cookie_gendomainorder=instaddr.uk',
        'priority': 'u=1, i',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"127.0.6533.120"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.120", "Chromium";v="127.0.6533.120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'action': 'addMailAddrByAuto',
        'nopost': '1',
        'by_system': '1',
        'csrf_token_check': 'cf21a948ae553e1f15314ede3546451b',
        'csrf_subtoken_check': 'f6dd1e7ee8737cb287b18faf0e619c04',
        'recaptcha_token': '',
        '_': '1724166440830',
    }

    response = requests.get('https://m.kuku.lu/index.php', params=params, cookies=cookies, headers=headers)

    if response.status_code==200:
        return response.text.replace('OK:', '')
    else:
        return False
    
def send_yonezu_email(email):
    cookies = {
        'referrer': 'https%3A%2F%2Faccount.kenshiyonezu.jp%2Flogin.php%3Fref%3DQkjxt8ETuEi7mdt0hyrDY73RC51z5tYesCuT4p4hhB7%252FBaqMQBfTYyoVG%252F3DwhYI%252BwW7uF4i2QgbB9uzQW%252BLrNXe3zXZ%252FIxBZgATsW%252F3aMPZOlbdkCNUo%252FuWnWkfqKfg74y790k87OUeNfJS%252F3RqylDoG3r9%252FN5%252BqDk0Pzi80g4rfc5OTD7JJCJ5u%252F9l2ZAcggBsaCMINmY%252B%252BU%252BK9x2cS94RyKgXGXKlvmTNChreCc8e5QG3Pet75jzuyhFAwmjZRZ01LxrjBD8WgU4MOqt3blam%252BGwomI5VEDZnBzdtDkEDQu%252FxCvu8v4hSuXdaxZUfWCy4Z9XxL6nPNvNUMvqVPUSzNxjSRPDJhsPU4jC36Nlqq7aQsm4stfdW3nKmzHNtcVEMf%252B5E10lbT5WBxqdlLA%253D%253D',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'referrer=https%3A%2F%2Faccount.kenshiyonezu.jp%2Flogin.php%3Fref%3DQkjxt8ETuEi7mdt0hyrDY73RC51z5tYesCuT4p4hhB7%252FBaqMQBfTYyoVG%252F3DwhYI%252BwW7uF4i2QgbB9uzQW%252BLrNXe3zXZ%252FIxBZgATsW%252F3aMPZOlbdkCNUo%252FuWnWkfqKfg74y790k87OUeNfJS%252F3RqylDoG3r9%252FN5%252BqDk0Pzi80g4rfc5OTD7JJCJ5u%252F9l2ZAcggBsaCMINmY%252B%252BU%252BK9x2cS94RyKgXGXKlvmTNChreCc8e5QG3Pet75jzuyhFAwmjZRZ01LxrjBD8WgU4MOqt3blam%252BGwomI5VEDZnBzdtDkEDQu%252FxCvu8v4hSuXdaxZUfWCy4Z9XxL6nPNvNUMvqVPUSzNxjSRPDJhsPU4jC36Nlqq7aQsm4stfdW3nKmzHNtcVEMf%252B5E10lbT5WBxqdlLA%253D%253D',
        'origin': 'https://account.kenshiyonezu.jp',
        'priority': 'u=0, i',
        'referer': 'https://account.kenshiyonezu.jp/email_validation.php',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    data = {
        'email': email,
    }

    response = requests.post('https://account.kenshiyonezu.jp/email_validation_check.php', cookies=cookies, headers=headers, data=data)
    
    return response.status_code
    
def get_yonezu_first():
    cookies = {
        'cf_clearance': 'aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48',
        'cookie_csrf_token': 'cf21a948ae553e1f15314ede3546451b',
        'cookie_sessionhash': 'SHASH%3A22d720d51fee77ce82bbf25cba3cba57',
        'cookie_setlang': 'ja',
        'cookie_failedSlot': '',
        'cookie_timezone': 'Asia%2FTokyo',
        'cookie_gendomainorder': 'instaddr.uk',
        'cookie_keepalive_insert': '1',
        'cookie_last_page_recv': '0',
        'cookie_last_page_addrlist': '0',
        'cookie_last_page_send': '0',
        'cookie_filter_recv2': '%7B%22filter_mailtype%22%3A%22unread%22%7D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'cf_clearance=aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48; cookie_csrf_token=cf21a948ae553e1f15314ede3546451b; cookie_sessionhash=SHASH%3A22d720d51fee77ce82bbf25cba3cba57; cookie_setlang=ja; cookie_failedSlot=; cookie_timezone=Asia%2FTokyo; cookie_gendomainorder=instaddr.uk; cookie_keepalive_insert=1; cookie_last_page_recv=0; cookie_last_page_addrlist=0; cookie_last_page_send=0; cookie_filter_recv2=%7B%22filter_mailtype%22%3A%22unread%22%7D',
        'priority': 'u=1, i',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"128.0.6613.84"',
        'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.84", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.84"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    response = requests.get(
        'https://m.kuku.lu/recv._ajax.php?&&nopost=1&csrf_token_check=cf21a948ae553e1f15314ede3546451b&csrf_subtoken_check=f6dd1e7ee8737cb287b18faf0e619c04&_=1724482364141',
        cookies=cookies,
        headers=headers,
    )

    html_content = response.text

    start_index = html_content.find("openMailData(")
    if start_index == -1:
        return None

    end_index = html_content.find("from=noreply", start_index)
    if end_index == -1:
        return None

    url_with_text = html_content[start_index:end_index]

    if response.status_code==200:
        return url_with_text.strip()
    else:
        return False

def get_yonezu_second(email, num, key):
    formatted_mail = email.replace('@', '%40')

    cookies = {
        'cf_clearance': 'aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48',
        'cookie_csrf_token': 'cf21a948ae553e1f15314ede3546451b',
        'cookie_sessionhash': 'SHASH%3A22d720d51fee77ce82bbf25cba3cba57',
        'cookie_keepalive_insert': '1',
        'cookie_setlang': 'ja',
        'cookie_failedSlot': '',
        'cookie_last_page_addrlist': '0',
        'cookie_timezone': 'Asia%2FTokyo',
        'cookie_gendomainorder': 'instaddr.uk',
        'cookie_last_q': formatted_mail,
        'cookie_last_page_recv': '0',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'cf_clearance=aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48; cookie_csrf_token=cf21a948ae553e1f15314ede3546451b; cookie_sessionhash=SHASH%3A22d720d51fee77ce82bbf25cba3cba57; cookie_keepalive_insert=1; cookie_setlang=ja; cookie_failedSlot=; cookie_last_page_addrlist=0; cookie_timezone=Asia%2FTokyo; cookie_gendomainorder=instaddr.uk; cookie_last_q=taboho213%40fuwari.be; cookie_last_page_recv=0',
        'origin': 'https://m.kuku.lu',
        'priority': 'u=0, i',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"127.0.6533.120"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.120", "Chromium";v="127.0.6533.120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    data = {
        'num': num,
        'key': key,
        'noscroll': '1',
    }

    response = requests.post('https://m.kuku.lu/smphone.app.recv.view.php', cookies=cookies, headers=headers, data=data)

    html_content = response.text

    start_index = html_content.find("https://account.kenshiyonezu.jp/register.php?")
    if start_index == -1:
        return None

    end_index = html_content.find("</a>", start_index)
    if end_index == -1:
        return None

    url_with_text = html_content[start_index:end_index]

    if response.status_code==200:
        return url_with_text.strip()
    else:
        return False
    
def clear_mails():
    cookies = {
        'cf_clearance': 'aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48',
        'cookie_csrf_token': 'cf21a948ae553e1f15314ede3546451b',
        'cookie_sessionhash': 'SHASH%3A22d720d51fee77ce82bbf25cba3cba57',
        'cookie_setlang': 'ja',
        'cookie_failedSlot': '',
        'cookie_timezone': 'Asia%2FTokyo',
        'cookie_gendomainorder': 'instaddr.uk',
        'cookie_keepalive_insert': '1',
        'cookie_last_page_recv': '0',
        'cookie_last_page_addrlist': '0',
        'cookie_last_page_send': '0',
        'cookie_filter_recv2': '%7B%22filter_mailtype%22%3A%22unread%22%7D',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        # 'cookie': 'cf_clearance=aBKFedk2R8_9l2vyHK71i4Xm06.OfgCi4s9071Gma8g-1724166413-1.2.1.1-kJHn7uCE.I1pn97Yemdtd0.ACv29aLAAVu7cdVZ6YSRTqQuN7CuSlgNlAwh9LLoSwAKpVA_EjBw_g1y7Uop_rFi2h9UvuwC3CgAJ8OIMcdv_4RGTjnoFEnjvO7k_HMETkfKXRaTpfQXHP2f_xi28RO6p8AJ2EP7pp3mAaR0ahR5FpoJ20mlFCFG7KOglTHbCx3MxReB_otiwd1ud_i1RJYvFaW7cYTdr20Ue.If8QhZ4lT4XO1apSChiXUU.BZasR6jrYtmn472pfOQ25VZAyEEGzyo9PrZxSl5GfKq0djIXZBsyoH1UPRviQy1U_WY3Tqw7Fj7abEpN9YRZHtNpU1AASNc73bLUNPjV4nUNxUeAF6bFtQJFLagYcrlfyAVOAVEyZpnawodVGGOnsk7cWuhbYivzEcShuF2HLUydc48; cookie_csrf_token=cf21a948ae553e1f15314ede3546451b; cookie_sessionhash=SHASH%3A22d720d51fee77ce82bbf25cba3cba57; cookie_setlang=ja; cookie_failedSlot=; cookie_timezone=Asia%2FTokyo; cookie_gendomainorder=instaddr.uk; cookie_keepalive_insert=1; cookie_last_page_recv=0; cookie_last_page_addrlist=0; cookie_last_page_send=0; cookie_filter_recv2=%7B%22filter_mailtype%22%3A%22unread%22%7D',
        'priority': 'u=1, i',
        'referer': 'https://m.kuku.lu/',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"128.0.6613.84"',
        'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.84", "Not;A=Brand";v="24.0.0.0", "Google Chrome";v="128.0.6613.84"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    requests.get(
        'https://m.kuku.lu/recv._ajax.php?action=allReadMail&nopost=1&&csrf_token_check=cf21a948ae553e1f15314ede3546451b&csrf_subtoken_check=f6dd1e7ee8737cb287b18faf0e619c04&_=1724483567171',
        cookies=cookies,
        headers=headers,
    )
    
def register_account_first(verify_url):
    formatted_url = verify_url.replace(':', '%3A').replace('/', '%2F').replace('?', '%3F')

    cookies = {
        'referrer': formatted_url,
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'referrer=https%3A%2F%2Faccount.kenshiyonezu.jp%2Femail_validation.php',
        'origin': 'https://account.kenshiyonezu.jp',
        'priority': 'u=0, i',
        'referer': verify_url,
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    data_url = verify_url.replace('https://account.kenshiyonezu.jp/register.php?', '')

    data = {
        'id': data_url,
        'screen_name': '',
        'input_personal': 'true',
        'login_pw': 'Aspw0101010101',
        'login_re': 'Aspw0101010101',
        'name1': 'As',
        'name2': 'pw',
        'name1_kkn': 'アス',
        'name2_kkn': 'ペ',
        'birth_y': '2000',
        'birth_m': '1',
        'birth_d': '1',
        'gender': '1',
        'tel1': '070010101001',
        'country': 'jp',
        'zip1': '265',
        'zip2': '0012',
        'prefecture': '北海道',
        'address1': '佐藤市最高町',
        'address2': '千葉',
    }

    response = requests.post('https://account.kenshiyonezu.jp/register_conf.php', cookies=cookies, headers=headers, data=data)

    html_content = response.text

    start_index = html_content.find('<input type="hidden" name="id2" value="')
    if start_index == -1:
        return None

    end_index = html_content.find('">', start_index)
    if end_index == -1:
        return None

    url_with_text = html_content[start_index:end_index]

    if response.status_code==200:
        return url_with_text.strip()
    else:
        return False
    
def register_account_final(verify_url, idtwo):
    formatted_url = verify_url.replace(':', '%3A').replace('/', '%2F').replace('?', '%3F')

    print(f'formatted url: {formatted_url}')

    cookies = {
        'referrer': formatted_url,
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'referrer=https%3A%2F%2Faccount.kenshiyonezu.jp%2Fregister.php%3F02fa8af9cb984b30d874ea41b773c220',
        'origin': 'https://account.kenshiyonezu.jp',
        'priority': 'u=0, i',
        'referer': 'https://account.kenshiyonezu.jp/register_conf.php',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    }

    data_url = verify_url.replace('https://account.kenshiyonezu.jp/register.php?', '')

    print(f'id: {data_url}')
    print(f'id2: {idtwo}')

    data = {
        'id': data_url,
        'id2': idtwo,
        'checkbox[]': 'on',
    }

    response = requests.post('https://account.kenshiyonezu.jp/register_comp.php', cookies=cookies, headers=headers, data=data)

    if response.status_code==200:
        return True
    else:
        return False

def register_account():
    email = gen_random_email()
    if not email:
        print('Failed to generate email')
        return

    print('Registering account...')
    reg_yonezu = send_yonezu_email(email)
    if not reg_yonezu:
        print(f'Reg yonezu failed with status code: {reg_yonezu}')
        return

    print(f'Reg yonezu status code: {reg_yonezu}, {email}')
    print('Waiting for email... (10s)')
    time.sleep(10)

    print('Trying to get email...')
    got_key_and_num = get_yonezu_first()
    if not got_key_and_num:
        print('Failed to retrieve email')
        return

    try:
        num = re.search(r"'(\d+)'", got_key_and_num).group(1)
        key = re.search(r"'([a-f0-9]{32})'", got_key_and_num).group(1)
        print(f'num: {num}')
        print(f'key: {key}')
    except AttributeError:
        print('Failed to extract num and key from the email')
        return

    yonezu_verify_url = get_yonezu_second(email, num, key)
    if not yonezu_verify_url:
        print('Failed to get yonezu verify URL')
        return

    print(f'Got verify URL: {yonezu_verify_url}')

    idtwo = register_account_first(yonezu_verify_url)
    if not idtwo:
        print('Failed to register first part')
        return

    real_idtwo = idtwo.replace('<input type="hidden" name="id2" value="', '').strip()
    print('Final register part')

    reg_final = register_account_final(yonezu_verify_url, real_idtwo)
    if not reg_final:
        print('Failed to register final part')
        return

    print(f'Registered account! {email}:Aspw0101010101')
    account_info = f'{email}:Aspw0101010101'
    with open("accounts.txt", "a") as f:
        f.write(f"{account_info}\n")
    print('Saved to accounts.txt')

clear_mails()
while (True):
    register_account()
    clear_mails()
    time.sleep(1)