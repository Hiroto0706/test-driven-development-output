# 学んだこと

### 1. `__hash__`と`__eq__`について

この章では Python における**hash**や**eq**がどのような役割を担うのかを学んだ。

#### __hash__について

<details>
<summary>__hash__について</summary>

# Python における`__hash__`メソッドの詳細解説

## 1. `__hash__`とは何か

`__hash__`は、Python の特殊メソッド（ダンダーメソッド）の一つで、オブジェクトのハッシュ値を計算するために使用されます。ハッシュ値とは、オブジェクトを一意に識別するための整数値です。

## 2. なぜ`__hash__`が必要なのか

`__hash__`が必要な主な理由は以下の通りです：

1. **辞書（dict）のキーとして使用するため**：
   Python の辞書は内部的にハッシュテーブルを使用しており、キーのハッシュ値に基づいて値を格納・検索します。

2. **集合（set）の要素として使用するため**：
   集合も辞書と同様にハッシュテーブルを使用しています。

3. **オブジェクトの一意性を効率的に判断するため**：
   ハッシュ値を使うことで、オブジェクトの比較を高速に行えます。

## 3. `__hash__`と`__eq__`の関係

`__hash__`と`__eq__`は密接に関連しています：

- **ルール 1**: 等しいオブジェクト（`a == b`が`True`）は同じハッシュ値を持つ必要がある
- **ルール 2**: 等しくないオブジェクトは異なるハッシュ値を持つことが望ましい（必須ではない）

## 4. 具体例で理解する

### 例 1: 組み込み型のハッシュ

```python
# 整数のハッシュ値
print(hash(42))  # 42

# 文字列のハッシュ値
print(hash("hello"))  # -8469019757955423296（環境により異なる）

# タプルのハッシュ値（イミュータブルなオブジェクトのみ含む場合）
print(hash((1, 2, "three")))  # 2528502973977326415（環境により異なる）

# リストはハッシュ不可能（ミュータブルなため）
try:
    hash([1, 2, 3])
except TypeError as e:
    print(e)  # "unhashable type: 'list'"
```

### 例 2: カスタムクラスでの`__hash__`の実装

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))  # タプルのハッシュを利用

# 使用例
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# 等しいオブジェクトは同じハッシュ値を持つ
print(p1 == p2)  # True
print(hash(p1) == hash(p2))  # True

# 等しくないオブジェクトは異なるハッシュ値を持つ（通常）
print(p1 == p3)  # False
print(hash(p1) == hash(p3))  # False

# 辞書のキーとして使用
point_dict = {p1: "Point 1", p3: "Point 3"}
print(point_dict[p2])  # "Point 1" (p1とp2は等価なので同じキーとみなされる)
```

### 例 3: `__hash__`を実装しない場合の問題

```python
class BadPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, BadPoint):
            return False
        return self.x == other.x and self.y == other.y

    # __hash__を実装していない

# 使用例
bp1 = BadPoint(1, 2)
bp2 = BadPoint(1, 2)

try:
    point_dict = {bp1: "BadPoint 1"}
except TypeError as e:
    print(e)  # "unhashable type: 'BadPoint'"
```

この例では、`__eq__`をオーバーライドしたが`__hash__`を実装しなかったため、オブジェクトはハッシュ不可能になり、辞書のキーとして使用できません。

### 例 4: 通貨変換の例（あなたのコードに近い例）

```python
class CurrencyPair:
    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __eq__(self, other):
        if not isinstance(other, CurrencyPair):
            return False
        return (self.from_currency == other.from_currency and
                self.to_currency == other.to_currency)

    def __hash__(self):
        return hash((self.from_currency, self.to_currency))

class ExchangeRates:
    def __init__(self):
        self.rates = {}  # 辞書を使用して為替レートを保存

    def add_rate(self, from_currency, to_currency, rate):
        pair = CurrencyPair(from_currency, to_currency)
        self.rates[pair] = rate

    def get_rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1.0

        pair = CurrencyPair(from_currency, to_currency)
        return self.rates.get(pair)

# 使用例
rates = ExchangeRates()
rates.add_rate("USD", "EUR", 0.85)
rates.add_rate("EUR", "USD", 1.18)
rates.add_rate("USD", "JPY", 110.0)

# レートの取得
print(rates.get_rate("USD", "EUR"))  # 0.85
print(rates.get_rate("EUR", "USD"))  # 1.18
print(rates.get_rate("USD", "USD"))  # 1.0
```

この例では、`CurrencyPair`クラスが`__hash__`と`__eq__`を適切に実装しているため、辞書のキーとして使用できます。これにより、通貨ペアに基づいて為替レートを効率的に格納・検索できます。

## 5. `__hash__`を実装する際の注意点

1. **イミュータブル性**：
   ハッシュ可能なオブジェクトは通常イミュータブル（変更不可）であるべきです。オブジェクトの状態が変わるとハッシュ値も変わるため、辞書のキーとして使用中に変更されると問題が発生します。

2. **一貫性**：
   オブジェクトの寿命中、`__hash__`は一貫した値を返すべきです。

3. **分布**：
   良いハッシュ関数は、異なるオブジェクトに対して均等に分布したハッシュ値を生成します。

4. **効率性**：
   ハッシュ計算は高速であるべきです。

## 6. まとめ

`__hash__`メソッドは、Python でオブジェクトを辞書のキーや集合の要素として使用するために不可欠です。適切に実装することで、カスタムオブジェクトを効率的に格納・検索できるようになります。

あなたのコードの場合、`Pair`クラスを辞書のキーとして使用するために`__hash__`メソッドが必要でした。これにより、通貨ペアに基づいて為替レートを効率的に管理できるようになります。

</details>

個人的に以下の記事がめちゃくちゃ分かりやすかった。

https://qiita.com/yoichi22/items/ebf6ab3c6de26ddcc09a#%E8%BE%9E%E6%9B%B8%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E3%83%8F%E3%83%83%E3%82%B7%E3%83%A5%E9%96%A2%E6%95%B0%E3%81%AE%E6%84%8F%E7%BE%A9

ハッシュ関数の存在意義としては、辞書において値の取得や設定の際に、`__eq__`による全検索を避け、低コストで処理したいなという要求に応えるために使われる。

例えば、値の設定の場合を例にする。

1. ハッシュ値が一致し、かつ`__eq__`で一致するものがない　 → 　新しいキーの追加
2. ハッシュ値が一致し、かつ`__eq__`で一致するものがある　 → 　既存キーの値の上書き
   というふうに判断し、辞書型に値を追加する。

値を取得する場合を考える。

1. ハッシュ値が一致し、かつ`__eq__`で一致するものがない　 → エラー
2. ハッシュ値が一致し、かつ`__eq__`で一致するものがある　 → 値を返す
   となる。

`__hash__`は dict や set などのハッシュ化されたコレクションに対してオブジェクトを格納したい場合に必要になる。
今回の場合だと、Piar オブジェクトは Bank の rates という辞書に格納される必要があった。

```python
    def add_rate(self, from_c: str, to_c: str, rate: int):
        self.rates[Pair(from_c, to_c)] = rate
```


辞書や set のようなハッシュ化されたコレクションにて、Pair のようなオブジェクトをキーにしたい場合、**ハッシュ可能**である必要がある。
そうしないと、以下のパターンのようにエラーを返してしまうためだ。

> 1. ハッシュ値が一致し、かつ`__eq__`で一致するものがない　 → エラー
<details>
<summary>辞書や集合でオブジェクトをキーにしたい場合、hash関数が必要</summary>

そのとおりです！Python で辞書（dict）や集合（set）のようなハッシュベースのデータ構造にオブジェクトをキーとして使用する場合、そのオブジェクトは「ハッシュ可能」である必要があります。

## ハッシュ可能なオブジェクトの条件

オブジェクトをハッシュ可能にするには：

1. **`__hash__`メソッド**：オブジェクトのハッシュ値を計算する
2. **`__eq__`メソッド**：オブジェクト同士の等価性を判断する

## なぜハッシュが必要なのか

辞書や集合は内部的に「ハッシュテーブル」というデータ構造を使用しています：

1. **高速アクセス**：ハッシュ値を使うことで、O(1)の時間複雑度（定数時間）でキーの検索が可能
2. **効率的なストレージ**：大量のキーを効率的に管理できる

## 具体的な例

```python
# カスタムクラス
class CurrencyPair:
    def __init__(self, from_curr, to_curr):
        self.from_curr = from_curr
        self.to_curr = to_curr

    # 等価性の定義
    def __eq__(self, other):
        if not isinstance(other, CurrencyPair):
            return False
        return (self.from_curr == other.from_curr and
                self.to_curr == other.to_curr)

    # ハッシュ値の計算
    def __hash__(self):
        return hash((self.from_curr, self.to_curr))

# 辞書で使用
rates = {}
rates[CurrencyPair("USD", "JPY")] = 110.0
rates[CurrencyPair("EUR", "USD")] = 1.18

# 検索
pair = CurrencyPair("USD", "JPY")
print(rates[pair])  # 110.0
```

## ハッシュがない場合

`__hash__`を実装せずに`__eq__`だけを実装すると：

```python
class BadPair:
    def __init__(self, from_curr, to_curr):
        self.from_curr = from_curr
        self.to_curr = to_curr

    def __eq__(self, other):
        if not isinstance(other, BadPair):
            return False
        return (self.from_curr == other.from_curr and
                self.to_curr == other.to_curr)

    # __hash__がない！

# 辞書で使おうとすると...
try:
    rates = {BadPair("USD", "JPY"): 110.0}  # エラー！
except TypeError as e:
    print(e)  # "unhashable type: 'BadPair'"
```

## まとめ

1. **辞書や集合のキー**：オブジェクトをキーとして使うには、ハッシュ可能である必要がある
2. **ハッシュ可能の条件**：`__hash__`と`__eq__`の両方が適切に実装されている
3. **一貫性の原則**：等しいオブジェクトは同じハッシュ値を持つべき

あなたのコードでは、`Pair`クラスを辞書のキーとして使うために`__hash__`メソッドが必要だったというわけです。

</details>



#### __eq__について

`__rq__`も`__hash__`と同様にPythonの特殊メソッドである。
これはシンプルに等価性比較を行いたい時に使えるメソッドを定義することができる。

シンプルに、2つのオブジェクトが等しいかどうかを判断する時に使える関数。


<details>
<summary>__eq__について</summary>

# Python における`__eq__`メソッドの詳細解説

## 1. `__eq__`とは何か

`__eq__`は、Python の特殊メソッド（ダンダーメソッド）の一つで、等価性比較演算子`==`の動作を定義します。このメソッドは、2 つのオブジェクトが「等しい」かどうかを判断するために使用されます。

## 2. なぜ`__eq__`が必要なのか

`__eq__`が必要な主な理由は以下の通りです：

1. **カスタムオブジェクトの等価性を定義するため**：
   デフォルトでは、オブジェクトの等価性はメモリ上の同一性（同じオブジェクトかどうか）に基づきますが、値に基づく比較が必要な場合があります。

2. **コレクション内での検索を可能にするため**：
   リスト、辞書、集合などのコレクションで`in`演算子を使用する際、`__eq__`が呼び出されます。

3. **`__hash__`と連携して辞書のキーや集合の要素として使用するため**：
   等しいオブジェクトは同じハッシュ値を持つ必要があります。

## 3. デフォルトの`__eq__`の挙動

Python のオブジェクトは、デフォルトで`is`演算子と同じ挙動をする`__eq__`を持っています：

```python
class DefaultEq:
    pass

a = DefaultEq()
b = DefaultEq()
c = a

print(a == b)  # False（異なるオブジェクト）
print(a == c)  # True（同じオブジェクト）
print(a is b)  # False
print(a is c)  # True
```

## 4. 具体例で理解する

### 例 1: 基本的な`__eq__`の実装

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        # 型チェック
        if not isinstance(other, Person):
            return False

        # 属性の比較
        return self.name == other.name and self.age == other.age

# 使用例
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True（同じ名前と年齢）
print(p1 == p3)  # False（異なる名前と年齢）
print(p1 == "Alice")  # False（異なる型）
```

### 例 2: リスト内での検索

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __str__(self):
        return f"{self.title} by {self.author}"

# 本のリスト
books = [
    Book("1984", "George Orwell"),
    Book("To Kill a Mockingbird", "Harper Lee"),
    Book("The Great Gatsby", "F. Scott Fitzgerald")
]

# 検索
search_book = Book("1984", "George Orwell")
if search_book in books:
    print(f"Found: {search_book}")  # "Found: 1984 by George Orwell"

# タイトルだけで検索したい場合
class BookTitleSearch:
    def __init__(self, title):
        self.title = title

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return False

# タイトルだけで検索
title_search = BookTitleSearch("The Great Gatsby")
for book in books:
    if title_search == book:  # BookTitleSearch.__eq__が呼ばれる
        print(f"Found by title: {book}")  # "Found by title: The Great Gatsby by F. Scott Fitzgerald"
```

### 例 3: `__eq__`と`__hash__`の連携

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# 辞書と集合での使用
points = {
    Point(0, 0): "Origin",
    Point(1, 0): "Unit X",
    Point(0, 1): "Unit Y"
}

# 等価なオブジェクトで検索
p = Point(1, 0)
print(points[p])  # "Unit X"

# 集合での重複排除
point_set = {Point(0, 0), Point(1, 1), Point(0, 0)}
print(len(point_set))  # 2（重複が排除される）
for p in point_set:
    print(p)  # "Point(0, 0)" と "Point(1, 1)"
```

### 例 4: 通貨変換の例（あなたのコードに近い例）

```python
class CurrencyPair:
    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __eq__(self, other):
        # 型チェック
        if not isinstance(other, CurrencyPair):
            return False

        # 通貨コードの比較
        return (self.from_currency == other.from_currency and
                self.to_currency == other.to_currency)

    def __hash__(self):
        return hash((self.from_currency, self.to_currency))

    def __str__(self):
        return f"{self.from_currency}/{self.to_currency}"

# 為替レート管理
exchange_rates = {
    CurrencyPair("USD", "EUR"): 0.85,
    CurrencyPair("EUR", "USD"): 1.18,
    CurrencyPair("USD", "JPY"): 110.0
}

# レート検索
pair1 = CurrencyPair("USD", "EUR")
pair2 = CurrencyPair("USD", "EUR")  # pair1と等価だが異なるオブジェクト

print(pair1 == pair2)  # True
print(exchange_rates[pair1])  # 0.85
print(exchange_rates[pair2])  # 0.85（__eq__のおかげで同じキーとして扱われる）

# 存在しないペアの検索
try:
    print(exchange_rates[CurrencyPair("JPY", "EUR")])
except KeyError:
    print("Rate not found")  # "Rate not found"
```

## 5. `__eq__`実装の注意点

1. **反射性**: `a == a`は常に`True`を返すべき
2. **対称性**: `a == b`が`True`なら、`b == a`も`True`であるべき
3. **推移性**: `a == b`かつ`b == c`なら、`a == c`も`True`であるべき
4. **一貫性**: オブジェクトが変更されない限り、`==`の結果は一貫しているべき
5. **`None`との比較**: `a == None`は通常`False`を返すべき（`is None`を使うのが推奨）

6. **型チェック**: 異なる型との比較を適切に処理するべき

   ```python
   def __eq__(self, other):
       if not isinstance(other, MyClass):
           # Pythonの慣習では、異なる型の場合はNotImplementedを返すこともある
           # これにより、other側の__eq__が試行される
           return NotImplemented
       # 同じ型の場合の比較ロジック
   ```

7. **`__hash__`との整合性**: `__eq__`をオーバーライドする場合、`__hash__`も適切に実装するか、`__hash__ = None`として明示的にハッシュ不可能にするべき

## 6. `__eq__`と他の比較メソッド

Python には他にも比較のための特殊メソッドがあります：

- `__ne__`: `!=`演算子（不等価）
- `__lt__`: `<`演算子（未満）
- `__le__`: `<=`演算子（以下）
- `__gt__`: `>`演算子（超過）
- `__ge__`: `>=`演算子（以上）

Python 3 では、`__eq__`を実装すると、デフォルトで`__ne__`は`__eq__`の否定として自動的に実装されます。

## 7. まとめ

`__eq__`メソッドは、Python でカスタムオブジェクトの等価性を定義するために不可欠です。適切に実装することで：

1. オブジェクトの意味的な等価性を定義できる
2. コレクション内での検索が可能になる
3. `__hash__`と連携して辞書のキーや集合の要素として使用できる

あなたのコードの場合、`Pair`クラスに`__eq__`メソッドを実装することで、通貨ペアの等価性を適切に定義し、辞書のキーとして使用できるようになります。

</details>


__eq__が必要な理由は以下の通り。
1. カスタムオブジェクトの等価性を定義するため
2. コレクション内で検索を可能にするため
3. __hash__と連携して辞書のキーや集合の要素として使用するため

2のコレクション内で検索するためというのは、リスト・辞書・集合などのコレクションでin演算子を使う場合、__eq__が呼び出される。
そのため、コレクション内検索を行いたい場合はこの__eq__の定義が必要なのだ。

3においては等しいオブジェクトは同じハッシュ値を持つ必要があるというルールがあるため。

```python
class DefaultEq:
    pass

a = DefaultEq()
b = DefaultEq()
c = a

print(a == b)  # False（異なるオブジェクト）
print(a == c)  # True（同じオブジェクト）
print(a is b)  # False
print(a is c)  # True
```

こちらの例からもわかるように、同じオブジェクトとは、同じハッシュ値を持っている必要があるということがわかるだろう。