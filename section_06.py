user_names = ["侍太郎","侍一郎","侍二郎","侍三郎","侍四郎",]
print(user_names[1])#２番目の要素だけを表示
user_names[1] = "侍花子"#2番目の要素を更新
print(user_names)
user_names.append("侍五郎")#6番目の要素を追加
print(user_names)
user_names.pop(2)#3番目"侍二郎"の要素を削除(0始まりのため2を指定)
print(user_names)

country_names = ("日本","アメリカ","イギリス","フランス")
#3番目の要素(フランス)を取り出す
print(country_names[2])
#すべての要素を取り出す
print(country_names)

country_names = {"日本","アメリカ","イギリス","フランス"}
#セット全体を表示
print(country_names)
#ドイツをセットに追加
country_names.add("ドイツ")
print(country_names)
#セットからイギリスを削除
country_names.remove("イギリス")
print(country_names)