def normalize_url(url):
    len_http = len('http://')
    len_https = len('https://')
    if url[:len_http] == 'http://' or url[:len_https] == 'https://':
        if url[:len_http] == 'http://':
            normalized_url = url.replace('http://', 'https://')
        else:
            normalized_url = url
    else:
        normalized_url = f'https://{url}'

    return normalized_url

print(normalize_url('httpsecurity.ru'))