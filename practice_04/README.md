# 学んだこと

### 1. pythoでプライベート変数にするときの注意点

これはテスト駆動とは関係ないのだが、pythonではクラスの変数をプライベートにしたいときはアンダースコアを使う必要がある。

```python
    def equals(self, object: "Dollar"):
        dollar = object
        return self._amount == dollar._amount # ここも！
```

そして、自分が引っかかったのはobjectを代入したdollarの`_amount`。
ここもプライベート変数にする必要があるので覚えておこう。

そうじゃないと、`amountなんてプロパティないぞ！`って怒られる。