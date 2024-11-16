#連想配列を作成(数字にはダブルコーテーション必要なし)
personal_data = {"name":"侍太郎","age":36,"gender":"男性",}
#キー「name」の値を表示
print(personal_data["name"])
#連想配列全体を表示
print(personal_data)
#キー「age」の値を更新36→37に変更
personal_data["age"] = 37
#新しく要素(キーと値)を追加
personal_data["address"] = "東京都"
#連想配列全体を表示
print(personal_data)