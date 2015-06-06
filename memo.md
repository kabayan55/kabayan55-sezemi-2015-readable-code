### 実際のコード

recipe_data_txtfile=codecs.open(os.path.dirname(os.path.abspath(__file__))+'/receipe_data.txt','w')
recipe_data_txtfile.write('オムライス'+'\n')


### どうしてリーダブルだと思っているかの説明
*レシピデータをテキストファイルにという意味をこめてのrexipe_data_textfile

### 実際のコード
three_recipes2txtfile.write('オムライス'+'\n')
three_recipes2txtfile.write('親子丼'+'\n')
three_recipes2txtfile.write('杏仁豆腐'+'\n')


### どうしてリーダブルだと思っているかの説明
*threeで3つだとわかる
*2(toの意)としたことで出力していることを伝えたい

### 実際のコード
*three_recipes={1:'オムライス',2:'親子丼',3:'杏仁豆腐'}

### どうしてリーダブルだと思っているかの説明
*idつきでリストにいれている

### 実際のコード
*for recipe_key, recipe_name in three_recipes.items():

### どうしてリーダブルだと思っているかの説明
*recipe_nameでレシピの名前と取って来ているとわかる

---

## 引き継ぎ後 (id: takuti)

### 1

#### 実装

https://github.com/kabayan55/kabayan55-sezemi-2015-readable-code/blob/5b53c919811bcc719a03770e3e1f5c4c54e232f7/recipe.py

#### どうしてリーダブル？

```python
for recipe_key, recipe_name in three_recipes.items():
```

辞書が **recipes** と複数形で、イテレーション変数 **recipe** の単数形と紐付いていてよい。

また、key, valueの両方がイテレーション変数として扱われているため、元データがDictionaryであるということにすぐ気がつく。

#### 気づいたきっかけ

forループの処理を追いたくて、なにをイテレーションしているのか確認したときに気がついた。

### 2

#### 実装

上と同じ

#### どうしてリーダブル？

すでに書かれているが、 `three_recipes2txtfile` というネーミングがとてもよい :like:

- 2 が to の意味というのは慣例に従っているので分かりやすい
- three とデータ数を明示していて自己説明的な変数名
- どのような機能をもっているか（レシピをテキストファイルに書き込むときに使う）ということがとても良くわかる

#### 気づいたきっかけ

コードの大半をこの変数が占めていたので目を惹いて、役割を確認したところわかりやすかった。

### 3

#### 実装

上と同じ

#### どうしてリーダブル？

```python
three_recipes2txtfile.write(str(recipe_key)+': '+ recipe_name +'\n')
```

元データ（辞書）の設計がよく、idが数字であるということがすぐに分かる。それが書き込み時に str() で文字列に変換していることからも明らかで素敵 :sushi:

#### 気づいたきっかけ

元データがどのように扱われているのか考えた時に、すぐに id(int) と recipe(string) の辞書ということがわかった。