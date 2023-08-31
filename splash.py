import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

'''
만약 인터넷 속도가 너무 느려 크롤링이 잘 안된다면, self.load_time의 값을 높여 페이지 로딩을 더 오래 기다리도록 조정할 수 있습니다.
'''

class SplashNews:
    def __init__(self):
        # 웹 브라우저 제어를 위한 WebDriver 객체 생성
        self.driver = webdriver.Chrome()
        
        # 기사 검색을 위한 기본 URL 및 검색어 설정
        self.url = 'https://splash247.com/page/{}/?s={}'
        self.word = 'vlsfo' 
        
        # 데이터 저장을 위한 리스트 초기화
        self.link_list = [] # 기사 링크
        self.title_list = [] # 기사 제목
        self.date_list = [] # 기사 게시 날짜
        self.content_list = [] # 기사 내용
        
        # 페이지 로딩 대기 시간 (초단위)
        self.load_time = 0

    # 크롤링할 기사의 링크를 수집하는 함수
    def get_link_list(self):
        # 첫 페이지로 접속
        new_url = self.url.format(1, self.word) 
        self.driver.get(new_url)
        time.sleep(self.load_time)  # 페이지 로딩 대기

        # 현재 페이지의 HTML 가져오기
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 마지막 페이지 번호 추출
        last_page_url = soup.select_one('.last-page.first-last-pages a')['href']
        last_page_number = int(last_page_url.split("/page/")[1].split("/")[0])

        print('\n마지막 페이지 번호 추출 완료 [Page Number : {}]\n'.format(last_page_number))

        # 첫 페이지부터 마지막 페이지까지 반복하여 기사의 링크를 수집
        for page in range(1, last_page_number + 1):
            new_url = self.url.format(page, self.word) 
            self.driver.get(new_url)
            time.sleep(self.load_time)

            # 현재 페이지의 HTML 가져오기
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # 해당 페이지의 모든 기사 링크를 가져와 저장
            article_links = soup.select('.post-title a')
            for link in article_links:
                self.link_list.append(link['href'])

            print('{}/{} 페이지 뉴스 기사 링크 추출 완료\n'.format(page, last_page_number))

    # 수집한 링크로 접속하여 기사의 세부 정보 (제목, 날짜, 내용)를 추출하는 함수
    def get_details(self):
        print("기사 추출 시작\n")
        num_of_link = len(self.link_list)
        for num in range(num_of_link):
            link = self.link_list[num]
            self.driver.get(link)
            time.sleep(self.load_time)  # 페이지 로딩 대기

            # 현재 페이지의 HTML 가져오기
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # 기사의 제목과 날짜 추출
            title = soup.select_one('h1.post-title.entry-title').text.strip()
            date = soup.select_one('span.date.meta-item.tie-icon').text.strip()

            # 기사의 내용 추출 (각 문단을 \n으로 구분)
            content_paragraphs = soup.select('div.entry-content.entry.clearfix p')
            content = '\n'.join(p.text for p in content_paragraphs)

            # 각 항목을 리스트에 저장
            self.title_list.append(title)
            self.date_list.append(date)
            self.content_list.append(content)

            print('{}/{} 기사 추출 완료'.format(num+1, num_of_link))
            print('제목:', title)
            print('날짜:', date)
            print('내용:', content[:100] + '...')  # 내용의 처음 100자만 출력
            print('-' * 50)

    # 추출한 데이터를 CSV 파일로 저장하는 함수
    def save_to_csv(self, filename='news_data.csv'):
        with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'Date', 'Link', 'Content'])  # 컬럼명 작성
            for title, date, link, content in zip(self.title_list, self.date_list, self.link_list, self.content_list):
                writer.writerow([title, date, link, content])

news = SplashNews()
news.get_link_list()
news.get_details()
news.save_to_csv()
