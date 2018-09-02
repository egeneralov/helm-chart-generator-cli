from setuptools import setup, find_packages

setup(
  name='hcg',
  version='1.0.0',
  license='MIT',
  packages=find_packages(),
  platforms='any',
  zip_safe=False,
  include_package_data=True,
  author='Eduard Generalov',
  author_email='eduard@generalov.net',
  description='cli client for Helm Chart Generator API',
  entry_points = {
    'console_scripts': ['hcg = hcg:cli']
  }
)
