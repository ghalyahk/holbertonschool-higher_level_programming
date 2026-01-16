import requests
import csv

# رابط API
JSONPLACEHOLDER_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """تجيب كل البوستات وتطبع العنوان لكل بوست"""
    try:
        response = requests.get(JSONPLACEHOLDER_URL)
        print(f"Status Code: {response.status_code}")  # طباعة حالة الطلب

        if response.status_code == 200:
            posts = response.json()  # تحويل البيانات JSON
            for post in posts:
                print(post.get("title"))  # طباعة عنوان البوست
        else:
            print("فشل في جلب البيانات")

    except requests.RequestException as e:
        print(f"حدث خطأ: {e}")


def fetch_and_save_posts():
    """تجيب كل البوستات وتخزنها في CSV"""
    try:
        response = requests.get(JSONPLACEHOLDER_URL)
        if response.status_code == 200:
            posts = response.json()

            # تجهيز البيانات بشكل قائمة قواميس
            structured_data = [
                {"id": post["id"], "title": post["title"], "body": post["body"]}
                for post in posts
            ]

            # كتابة البيانات في ملف CSV
            with open("posts.csv", mode="w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()  # كتابة العناوين في أول صف
                for post in structured_data:
                    writer.writerow(post)  # كتابة كل بوست

        else:
            print("فشل في جلب البيانات")

    except requests.RequestException as e:
        print(f"حدث خطأ: {e}")
