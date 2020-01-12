from case.www_python_org.get_title import get_title
from driver.chrome.instance import chrome

# task list
get_title(chrome)

# close browser
chrome.quit()
