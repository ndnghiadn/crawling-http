import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def crawl_viblo_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        titles = soup.select('.title')  
        views = soup.select('.view-count')

        if len(titles) == len(views):
            data = []
            for i in range(len(titles)):
                title = titles[i].text.strip()
                view_count = int(views[i].text.strip().replace(' views', '').replace(',', ''))  # Chuyển đổi view_count thành số nguyên
                data.append({'title': title, 'view_count': view_count})

            return data
        else:
            print("Không thể trích xuất dữ liệu. Độ dài không khớp.")
    else:
        print("Không thể kết nối tới trang web. Mã trạng thái:", response.status_code)

def draw_chart(data):
    titles = [entry['title'] for entry in data]
    view_counts = [entry['view_count'] for entry in data]

    plt.figure(figsize=(10, 6))
    plt.barh(titles, view_counts, color='skyblue')
    plt.xlabel('Số lượng view')
    plt.title('Số lượng view của các bài viết trên viblo.asia')
    plt.show()

if __name__ == "__main__":
    viblo_url = "https://viblo.asia/"
    data = crawl_viblo_data(viblo_url)

    if data:
        for entry in data:
            print(f"Title: {entry['title']}, View Count: {entry['view_count']}")
        
        draw_chart(data)
    else:
        print("Không có dữ liệu được trích xuất.")