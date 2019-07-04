from pyquery import PyQuery


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    py = PyQuery(url='https://www.zhihu.com/explore', headers=headers)
    items = py('.explore-tab .feed-item').items()
    for item in items:
        h2 = item('h2').text()
        author = item('.author-link').text()
        # answer = item('.content').text()
        answer = py(item.find('.content').html()).text()
        with open('123.txt', 'a', encoding='utf-8') as f:
            f.write('\n'.join([h2, author, answer]))
            f.write('\n' + '=' * 50 + '\n')

main()
