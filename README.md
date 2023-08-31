# SplashNews Web Scraper

## Description
`SplashNews`는 [Splash247](https://splash247.com/) 웹사이트에서 특정 키워드에 대한 뉴스 기사를 크롤링하는 파이썬 스크립트입니다. 제목, 게시 날짜, 기사 내용, 그리고 기사 링크를 추출하며, 추출된 데이터는 CSV 파일로 저장됩니다.

## Features
- 특정 키워드를 사용하여 뉴스 기사 검색
- 각 기사의 제목, 게시 날짜, 내용 및 링크 추출
- 추출된 데이터를 CSV 파일로 저장

## Requirements
- Python 3.x
- BeautifulSoup4
- Selenium
- Chrome WebDriver

## Setup
1. 필요한 라이브러리를 설치합니다.
```bash
pip install beautifulsoup4 selenium
2. Chrome WebDriver를 [여기](https://sites.google.com/a/chromium.org/chromedriver/downloads)에서 다운로드하고 설치 경로를 시스템 PATH에 추가합니다.

## Usage
1. `SplashNews` 클래스의 `word` 변수를 원하는 검색어로 변경합니다.
2. 스크립트를 실행합니다.
```bash
python splash.py
3. 실행이 완료되면 `news_data.csv`라는 이름의 CSV 파일이 생성됩니다. 필요에 따라 파일 이름을 변경할 수 있습니다.

## Note
- 인터넷 연결 상태나 웹사이트의 구조 변경에 따라 크롤링이 제대로 수행되지 않을 수 있습니다.
- 크롤링 대상 웹사이트의 로봇 배제 표준(Robots Exclusion Standard)을 확인하고, 해당 웹사이트의 크롤링 정책을 준수하세요.
