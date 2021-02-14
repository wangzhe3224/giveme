import requests


def giveme(names: [str], system: str='macOS', target: str='./.gitignore'):
    """
    Parameters
    ----------
    names: a list of names. if more than one, concat ignore files
    """
    url = 'https://raw.githubusercontent.com/github/gitignore/master/{}.gitignore'
    content = b''
    for name in names:
        _content = requests.get(url.format(name.capitalize()))
        content += _content.content

    if system:
        _content = requests.get('https://raw.githubusercontent.com/github/gitignore/master/Global/{}.gitignore'.format(system))
        content += b'\n'
        content += _content.content

    with open(target, 'wb') as f:
        f.write(content)


if __name__ == '__main__':

    giveme(['Python'])