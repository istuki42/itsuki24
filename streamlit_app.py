def get_fortune(birthday):
    # 誕生日から星座を割り出す
    year, month, day = birthday.split("-")
    zodiac = {
        "1月1日〜1月19日": "山羊座",
        "1月20日〜2月18日": "水瓶座",
        "2月19日〜3月20日": "魚座",
        "3月21日〜4月19日": "牡羊座",
        "4月20日〜5月20日": "牡牛座",
        "5月21日〜6月21日": "双子座",
        "6月22日〜7月22日": "蟹座",
        "7月23日〜8月22日": "獅子座",
        "8月23日〜9月22日": "乙女座",
        "9月23日〜10月22日": "天秤座",
        "10月23日〜11月21日": "蠍座",
        "11月22日〜12月21日": "射手座",
        "12月22日〜12月31日": "山羊座",
    }
    return zodiac[f"{year}-{month}-{day}"]


def main():
    # 誕生日を入力する
    birthday = input("誕生日を入力してください：")

    # 運勢を表示する
    fortune = get_fortune(birthday)
    print(f"{fortune}の運勢は、{fortune}です。")


if __name__ == "__main__":
    main()

import streamlit as st


def main():
    # 誕生日を入力する
    birthday = st.text_input("誕生日を入力してください：")

    # 運勢を表示する
    fortune = get_fortune(birthday)
    st.write(f"{fortune}の運勢は、{fortune}です。")


if __name__ == "__main__":
    main()
