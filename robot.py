from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())


#driver.get('https://www3.wipo.int/madrid/monitor/jsp/getData.jsp?qi=3-LTh8fcwhE6X0pxYCHRVN8PBoVeze4noGOad6e9N8X3Y=&ID=ROM.1611367&LANG=en&NO=0&TOT=1')
#driver.get('https://www3.wipo.int/madrid/monitor/jsp/terms.jsp?&terms=true&terms.sort=count&terms.limit=10&terms.prefix=1611367&terms.lower=1611367&terms.fl=IRN&terms.fl=RNS&terms.lower.incl=true&terms.regex.flag=case_insensitive&indent=false&wt=json&type=madrid')

#driver.get('https://www3.wipo.int/madrid/monitor/scripts/pdf-all.11476.min.js')
script = 'alert("hello")'
driver.execute_script(script)
print(dir(driver))
