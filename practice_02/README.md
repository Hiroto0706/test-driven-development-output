# 学んだこと

### 1. 副作用
副作用とは、以下のような計算を行ったときに「オブジェクトの値そのものが変化してしまい、その結果の血の処理に影響を与えること」を指す。

```python
def test_multiplication():
    five = Dollar(5)
    five.times(2) # ここでfiveのamountの値そのものが変更されてしまっている
    assert five.amount == 10
```

```python
    def times(self, multiplier: int):
        self.amount *= multiplier
```

※クラスメソッドにて、値ごと変えている

そのため、後続処理で以下のようにすると、エラーが起きてしまう。なぜなら、fiveのamountは値ごと変わっているから。

```python
    five.times(3)
    assert five.amount == 15 # エラー！！！
```

それを防ぐには値を直接更新するのではなく、オブジェクトそのものを返すようにする。

```python
    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)
```

そうすることで、後続処理に影響を与えることがなくなる。
このように副作用をなくすために、値の変更を伴う場合はオブジェクトそのものを返すようにするということを覚えておこう。