from setuptools import setup

req = open('requirements.txt')
requirements = req.readlines()
req.close()

setup(name='flaskchatterbot',
      version='0.1.0',
      description='An open-source web based Python chat bot in Flask.',
      url='https://github.com/wing3s/flask-chatterbot',
      author='Wen-Hao Lee',
      author_email='wing3s@gmail.com',
      license='BSD',
      install_requires=requirements,
      packages=['flaskchatterbot'],
      keywords=['flask', 'chatbot', 'chat', 'bot'],
      zip_safe=False)
