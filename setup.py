from driver.chrome.instance import chrome
from driver.firefox.instance import firefox
from case.www_python_org.check_browser_title import check_browser_title

# chrome task list
check_browser_title(chrome)

# close chrome
chrome.quit()

# firefox task list
check_browser_title(firefox)

# close firefox
firefox.quit()