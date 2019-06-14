def isElementExist(driver, element):
    flag = True
    try:
        driver.find_element_by_xpath(element)
        return flag
    except:
        flag = False
        return flag
def isElementExistWithCssSelector(driver, element):
    flag = True
    try:
        driver.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag
def isElementExistWithCssName(driver,element):
    flag = True
    try:
        driver.find_element_by_class_name
        return flag
    except:
        flag = False
        return flag
def isElementExistWithLinkText(driver,element):
    flag = True
    try:
        driver.find_element_by_link_text(element)
        return flag
    except:
        flag = False
        return flag