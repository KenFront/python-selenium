from driver.chrome.instance import run_chrome
from driver.firefox.instance import run_firefox
from case.www_python_org.check_browser_title import check_browser_title

chrome = run_chrome()
# chrome task list
check_browser_title(chrome)

# close chrome
chrome.quit()

firefox = run_firefox()
# firefox task list
check_browser_title(firefox)

# close firefox
firefox.quit()
