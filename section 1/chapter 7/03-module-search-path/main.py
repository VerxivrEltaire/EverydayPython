# Viewing the search path
import sys

print('Current Module Search Path:')
for path in sys.path:
    print(path)

# Output:
# Current Module Search Path:
# /Everyday Python A Comprehensive Guide to Scripting and Rapid Application Development/Content/10 Projects/Everyday Python/section 1/chapter 7/03-module-search-path
# /Everyday Python A Comprehensive Guide to Scripting and Rapid Application Development/Content/10 Projects/Everyday Python
# /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_display
# /Library/Frameworks/Python.framework/Versions/3.11/lib/python311.zip
# /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11
# /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/lib-dynload
# /Everyday Python A Comprehensive Guide to Scripting and Rapid Application Development/Content/10 Projects/Everyday Python/venv/lib/python3.11/site-packages
# /Applications/PyCharm.app/Contents/plugins/python/helpers/pycharm_matplotlib_backend