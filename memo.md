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