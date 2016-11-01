# -*- coding: utf-8 -*-
from templite import Templite

if __name__ == '__main__':
    template = '''\
<h1>Hello {{name|upper}}!</h1>
{% for topic in topics %}
<p>You are interested in {{topic}}.</p>
{% endfor %}
    '''

    templite = Templite(template, {'upper': str.upper})
    text = templite.render({
        'name': 'Ned',
        'topics': ['Python', 'Geometry', 'Juggling']
    })
    print(text)