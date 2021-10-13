from selenium.webdriver.support.ui import Select
import os
import csv
from selenium.webdriver.common.keys import Keys
import time
import requests
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os
import csv
from selenium.webdriver.common.keys import Keys
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get(
    "CHROMEDRIVER_PATH"), options=chrome_options)

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(
#     ChromeDriverManager().install(), options=chrome_options)
#driver = webdriver.Chrome()
notificationDat = "NA"
address = "NA"
Status = "NA"
currencies = []
removelist = []
thisval = ""


def writingfunction(currencies):
    #print("in writing function")
    print("Remaining list .....")
    for i in currencies:
        print(i)
    with open('Input.csv', 'w', newline='') as csvfile:
        fieldnames = ['IRN']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in currencies:
            thisval = i
            writer.writerow(
                {'IRN': thisval})


def Get_text_from_image(pdf_path):
    import pytesseract
    import io
    import gc
    from PIL import Image
    from wand.image import Image as wi
    import gc
    #print("get textfrom image called")
    """ Extracting text content from Image pdf """
    print("   Processing on pdf document   ")
    #pdf_path = "D:\pythonPCT\1496314_pdf.pdf"
    #print("file path is => "+ pdf_path)
    pdf = wi(filename=pdf_path, resolution=300)
    pdfImg = pdf.convert('jpeg')
    imgBlobs = []
    extracted_text = []
    try:
        for img in pdfImg.sequence:
            page = wi(image=img)
            imgBlobs.append(page.make_blob('jpeg'))
            for i in range(0, 5):
                [gc.collect() for i in range(0, 10)]
        for imgBlob in imgBlobs:
            im = Image.open(io.BytesIO(imgBlob))
            text = pytesseract.image_to_string(im, lang='eng')
            text = text.replace(r"\n", " ")
            extracted_text.append(text)

            for i in range(0, 5):
                [gc.collect() for i in range(0, 10)]
        return (''.join([i.replace("\n", " ").replace("\n\n", " ") for i in extracted_text]))
        [gc.collect() for i in range(0, 10)]
    finally:
        [gc.collect() for i in range(0, 10)]
        img.destroy()


def send_mail(pdf):
    import smtplib
    from email.message import EmailMessage
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    print('Starting to send email')
    # start TLS for security
    s.ehlo()
    s.starttls()
    print('Session Created')
    # Authentication
    s.login("result.code.312@gmail.com", "Resultcode@2021")
    print('Logged In')
    # message to be sent
    msg = EmailMessage()
    print('Starting to send email step 1')
    try:
        with open(pdf, 'r', encoding='utf-8') as fp:
            msg.set_content(fp.read())
        print('Starting to send email step 2')

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = f'The contents of {pdf}'
        msg['From'] = 'result.code.312@gmail.com'
        msg['To'] = 'ishfaqkhawaja312@gmail.com'

        # Send the message via our own SMTP server.
        s.send_message(msg)
        s.quit()
        print('Email send')
    except Exception as e:
        print(e)


def main(num):
    irnis = num
    try:
        driver.get("https://www3.wipo.int/madrid/monitor/en/")
        driver.find_element_by_id("AUTO_input").send_keys(irnis)
        driver.find_element_by_id(
            "AUTO_input").send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        print("    Page loading Error....")
        print(".......Close and Run Again..........")
    try:
        driver.find_element_by_id("gridForsearch_pane").click()
        time.sleep(5)
        page_src = driver.page_source
        soup = BeautifulSoup(page_src, "html.parser")
        time.sleep(5)
        containers = soup.findAll('div', {"class": "p"})

        for item in containers:
            # print(item)
            try:
                name = item.find('div', {"class": "inidText"})
                print(name.text)
                textis = item.find('div', {"class": "text"})
                if (name.text == "Name and address of the representative"):
                    address = (textis.text)
                    address = address.strip()
            except Exception as e:
                pass

        indian = soup.find_all("div", {"class": "text"})
        datecheck = 0
        for p in indian:
            if ('<span title="India">IN</span>' in str(p)):
                divTag = p.find_all("a", {"class": "pdfDocLink"})
                for div in divTag:
                    href = div['href']
                    link = (div['href'])
                datecheck = 1
            if (datecheck == 1):
                if (len(p.text) == 10):
                    if ("." in p.text):
                        notificationDate = p.text
                        datecheck = 0
        print(href)
        data = requests.get(href, stream=True)
        file_name = str(irnis)+'.pdf'
        file = open(file_name, 'wb')
        file.write(data.content)
        file.close()
        return file_name

        # send_mail(file_name)
    except:
        pass

    #     response = requests.get(href)
    #     # Parse text obtained
    #     soup = BeautifulSoup(response.text, 'html.parser')
    #     response = requests.get(link)
    #     #print("this is pdf downloading link")
    #     # print(link)
    #     pdf = open(str(irnis) + ".pdf", 'wb')
    #     #print("pdf path is found......")
    #     pdf_path = (os.getcwd() + "/" + str(irnis) + ".pdf")
    #     #print("this ispdf path for the last time and this is not finding")
    #     pdf.write(response.content)
    #     pdf.close()
    #     irnis = irnis.encode('ascii', 'ignore').decode('ascii')
    #     address = address.encode('ascii', 'ignore').decode('ascii')
    #     notificationDate = notificationDate.encode(
    #         'ascii', 'ignore').decode('ascii')
    #     # reading pdf data from here
    #     thispdf = Get_text_from_image(pdf_path)
    #     thispdf = str(thispdf)
    #     #print("this is pdf data")
    #     # print(thispdf)
    #     word = "The Grounds are mentioned as per the Notice(es) of Opposition attached herewith"
    #     second_word = "of filling TM-M"
    #     second_word2 = "of filing TM-M"
    #     findings = thispdf.find(word)
    #     # print(findings)
    #     if thispdf.find(word) != -1:
    #         Status = "Opposition"
    #         #print("this is first part of string")
    #         # print(Status)
    #     elif thispdf.find(second_word) != -1:
    #         Status = "Opposition"
    #         #print("this is second part of string")
    #         # print(Status)
    #     elif thispdf.find(second_word2) != -1:
    #         Status = "Opposition"
    #         #print("this is third part of string")
    #         # print(Status)
    #     else:
    #         #print("this is for else condition")
    #         Status = "Refusal"
    #         # print(Status)
    #     # end of reading pdf data
    #     List = [irnis, address, notificationDate, Status, link]
    #     # writer.writerow(
    #     # {'IRN': irnis, 'Name & Address': address, 'Notification Date': notificationDate, 'Status': Status,'Link':link})
    #     removelist.append(f)
    #     if (f) == last_element:
    #         print("!...Extraction Process completed...!")
    #         print("!...Extraction Process completed...!")

    # except Exception:
    #     for c in removelist:
    #         currencies.remove(c)
    #     writingfunction(currencies)
    #     print("    Page did not load properly     ")
    #     print(".......Close and Run Again..........")
    driver.close()


# if __name__ == '__main__':
#     main(1611367)
