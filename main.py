__author__ = 'TTChangeTheWorld'
from jinja2 import Environment, FileSystemLoader
import config
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('parallel_page.html')
result = open("index.html", "w", encoding="utf-8")
result.write(template.render(**config.get_config()))
result.close()