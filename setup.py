from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
   requirements = fh.read()

setup(
   name = 'FX_Rate_tool',
   version = '0.0.4',
   author = 'Yukti Sareen',
   author_email = 'yuktisareen02@gmail.com',
   description = 'Project to build a CLI tool to extract foreign exchange references rates using the Frankfurter API',
   long_description = long_description,
   long_description_content_type = "text/markdown",
   url = 'https://github.com/YSAREEN/FX_CLI',
   py_modules = ['FX_Rate_tool'],
   packages = find_packages(),
   install_requires = [requirements],
   python_requires='>=3.8',
   classifiers=[
       "Programming Language :: Python :: 3.8",
       "Operating System :: OS Independent",
   ],
   entry_points = '''
       [console_scripts]
       exrates=FX_Rate_tool:cli
   '''
)
