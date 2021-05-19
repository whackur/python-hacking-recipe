import requests

login_url = "https://shop.hakhub.net/wp-login.php"
item_url = "https://shop.hakhub.net/wp-comments-post.php"
account_form_data = {"log": "customer01", "pwd": "customer01!!"}

with requests.Session() as s:
    # form-data 형식은 data 인자 생략하여 작성 가능
    r = s.post(login_url, account_form_data)
    comment_form_data = {
        "rating": 5,
        "comment": "댓글 작성 테스트",
        "comment_post_ID": "70",
        "comment_parent": 0,
    }
    # Session 블록 안의 s는 로그인한 쿠키가 유지되어 생략가능
    # r = s.post(item_url, cookies=s.cookies, data=comment_form_data)
    r = s.post(item_url, data=comment_form_data)
    if r.status_code == 200:
        print("댓글을 작성하였습니다.")
    elif r.status_code == 403:
        print("댓글 작성 권한이 없거나 로그인 실패")
    elif r.status_code == 409:
        print("이미 댓글을 작성하였습니다.")
    elif r.status_code == 429:
        print("댓글을 너무 빨리 달고 있습니다.")
    else:
        print(f"댓글 작성 오류코드: {r.status_code}")
