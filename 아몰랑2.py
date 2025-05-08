from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
import time
import csv

# 브라우저 설정
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# 접속
driver.get("https://data.mafra.go.kr/opendata/data/open/indexOpenDataList.do")
time.sleep(2)


# '파일데이터' 탭 클릭
file_tab = driver.find_element(By.CSS_SELECTOR, 'a[data-name="tab3"]')
file_tab.click()
time.sleep(2)

# 전체 결과 저장용
data = []

# 페이지 반복
page = 1
while True:
    print(f"\n📄 페이지 {page} 크롤링 중...")
    time.sleep(2)

    # 항목 수집
    titles = driver.find_elements(By.CSS_SELECTOR, "strong.data-title")
    for title in titles:
        try:
            title_text = title.text.strip()
            if not title_text:
                continue  # 제목이 없으면 무시

            link_elem = title.find_element(By.XPATH, "..")
            link = link_elem.get_attribute("href") or ""  # None일 경우 빈 문자열 처리

            data.append({"title": title_text, "link": link})
            print(f"- {title_text} ({link if link else '링크 없음'})")

        except StaleElementReferenceException:
            continue

    # 다음 페이지 클릭
    try:
        next_page = driver.find_element(By.XPATH, f'//a[text()="{page + 1}"]')
        next_page.click()
        page += 1
    except NoSuchElementException:
        print("\n✅ 마지막 페이지까지 완료")
        break

driver.quit()

# CSV 저장
with open("mafra_filedata_list.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(data)

print(f"\n✅ 총 {len(data)}개 항목이 CSV로 저장되었습니다: mafra_filedata_list.csv")
