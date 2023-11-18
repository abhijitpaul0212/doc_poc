# Project Documentation using SPHINX

## Steps to be followed

1. Ensure the project source code has got the doc-strings created in reStructuredText style
```python
""" This is a reST style. 
:param param1: this is a first param 
:param param2: this is a second param 
:returns: this is a description of what is returned 
:raises keyError: raises an exception 
"""
```

2. Activate virtual environment of the project
3. Install project source as python package using setup.py 
4. Install below python packages
```bash
sphinx
sphinx-rtd-theme
sphinx-code-include
sphinx-autobuild
```

5. Go to <project root> path and create a ‘docs’ folder
6. Go to ‘docs’ and run ‘sphinx-quickstart’ and follow the steps given below
```bash
> Separate source and build directories (y/n) [n]: n
> Project name: Your project's name
> Author name(s): Your name or your team's name
> Project release []: Enter
> Project language [en]: Enter
```
7. Modify the ‘docs\conf.py’ file
```python
# Add in the begining of the file
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# Update the existing 'extensions' variable with below
extensions = [
   'sphinx.ext.todo',
   'sphinx.ext.viewcode',
   'sphinx.ext.autodoc',
   'sphinx.ext.intersphinx',
   'sphinx.ext.coverage',
]

# Update the existing 'html_theme' variable with below
html_theme = 'sphinx_rtd_theme'
```
8. Navigate to the <project root> folder and run sphinx-apidoc -o docs src to generate .rst files
9. Finally, there are two ways to generate Sphinx documentation
```bash
Manual Approach
docs\make.bat html 

[we need to re-run the command everytime there is a change in source code]

Automated Approach
sphinx-autobuild docs docs/_build/html

[automatically re-builds the html files whenever there is a change in source code]
```


## Pycharm Plugin to Generate DocString

1. Install Trelent - AI Docstrings on Demand from JetBrains Marketplace
2. Go to the source code
3. Click after any Python function and use ‘ALT+D’

DocStrings will be generated automatically. 
But the limitation is, we can only generate docString for one function at a time.

Also I have explored gpt4docstrings   to generate DocStrings for one python module at a time. But gpt4docstrings requires Paid subscription of OpenAI, which would need approvals
[https://github.com/MichaelisTrofficus/gpt4docstrings](https://github.com/MichaelisTrofficus/gpt4docstrings)



## Deploying a Sphinx project online

1. Read the Docs [This would be a better choice| Paid version]
2. GitHub Pages [For the sake of POC, I used it]
GitHub Page: [https://abhijitpaul0212.github.io/project_documentation_using_sphinx/index.html](https://abhijitpaul0212.github.io/project_documentation_using_sphinx/)
3. GitLab Pages
4. Netlify
5. Your own server

[Appendix: Deploying a Sphinx project online — Sphinx documentation (sphinx-doc.org)](https://www.sphinx-doc.org/en/master/tutorial/deploying.html)https://www.sphinx-doc.org/en/master/tutorial/deploying.html


### Hosted GitHub Page 

CLICK HERE [https://abhijitpaul0212.github.io/project_documentation_using_sphinx/index.html](https://abhijitpaul0212.github.io/project_documentation_using_sphinx/)

![image](https://github.com/abhijitpaul0212/project_documentation_using_sphinx/assets/9966441/88df9a58-c6b8-4a7b-82d5-481ed16c3c8f)




## Resources:
* [Welcome — Sphinx documentation (sphinx-doc.org)](https://www.sphinx-doc.org/en/master/)
* [Getting started with Sphinx — Read the Docs user documentation](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
* Sphinx-api: [sphinx-apidoc — Sphinx documentation (sphinx-doc.org)](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)
* [https://sphinx-intro-tutorial.readthedocs.io/en/latest/sphinx_first_steps.html](https://sphinx-intro-tutorial.readthedocs.io/en/latest/sphinx_first_steps.html)
* [https://sphinx-intro-tutorial.readthedocs.io/en/latest/sphinx_extensions.html#autobuild-extension](https://sphinx-intro-tutorial.readthedocs.io/en/latest/sphinx_extensions.html#autobuild-extension)
* [https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
* [https://coderefinery.github.io/documentation/gh_workflow/](https://coderefinery.github.io/documentation/gh_workflow/)

### sphinx-apidoc commands:

```bash
sphinx-apidoc -o docs src 
o -> output path for rst files
```
```bash
sphinx-apidoc -e -f -o docs src 
e → to separately create rst file for each 
f  -> to forcefully override and create rst files
```

