# 学んだこと

### 1. Pythonで親クラスを定義する

親クラスを定義するのはめちゃくちゃ基礎中の基礎。
知っておいて損しかないので、覚えておこう。

```python
# 親クラス
class Money:
    def __init__(self, amount: int):
        self._amount = amount

# 子クラス
from money import Money


class Dollar(Money):
    def __init__(self, amount: int):
        super().__init__(amount)

    def times(self, multiplier: int):
        return Dollar(self._amount * multiplier)

    def equals(self, object: "Dollar"):
        dollar = object
        return self._amount == dollar._amount
```

継承自体はめちゃくちゃ簡単。
`Dollar(親クラス)`とするだけ。

また、初期化は親の方でされているので、親クラスのコンストラクタに初期値を渡すために`super().__init__(value)`としよう。

そうすることで、親クラスの方で`__init__`が実行される。