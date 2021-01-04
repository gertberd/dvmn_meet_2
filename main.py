import re
from requests_html import HTMLSession
from transliterate import translit
from num2words import num2words


def get_text(url) -> str:
    session = HTMLSession()
    response = session.get(url)
    content = response.html.find('#file-text-md-readme', first=True)
    return content.full_text


if __name__ == '__main__':
    text_url = 'https://gist.github.com/dvmn-tasks/b86f46ee36d888ae6cf6d7cc9bc56640'
    text = get_text(text_url)
    print(translit(text, 'ru'))
    numbers = map(int, re.findall(r'\d+', text))
    for num in numbers:
        num_in_words = num2words(num)
        print(f"{num} - {translit(num_in_words, 'ru')}")


