import requests
from bs4 import BeautifulSoup
import time

base_url = "https://opendata.hira.or.kr/op/opc/selectOpenDataList.do?pageIndex="
page = 1
results = []

while True:
    url = base_url + str(page)
    print(f"크롤링 중: 페이지 {page} ...")
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"페이지 {page} 접속 실패 (status: {response.status_code})")
        break

    soup = BeautifulSoup(response.text, "html.parser")
    a_tags = soup.find_all("a", class_="select")
    
    # 페이지에 데이터가 없으면 종료
    if not a_tags:
        print("더 이상 데이터 없음. 종료.")
        break

    for tag in a_tags:
        text = tag.get_text(strip=True)
        results.append(text)

    page += 1
    time.sleep(1)  # 서버 부하 방지

# 결과 출력 또는 저장
print(f"\n총 {len(results)}개 항목 수집 완료!")
for idx, item in enumerate(results, 1):
    print(f"{idx}. {item}")
