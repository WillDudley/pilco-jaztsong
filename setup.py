# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pilco_gpytorch_will2', 'pilco_gpytorch_will2.models']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pilco-gpytorch-will2',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'WillDudley',
    'author_email': 'Will2346@live.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
