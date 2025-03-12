# 学んだこと

### 1. staticmethodについて

staticmethodはクラスに属するメソッドではあるが、インスタンスの状態やクラスそのものの状態にアクセスしないメソッドのことを指す。

```python
    @staticmethod
    def dollar(amount: int):
        return Dollar(amount)

    @staticmethod
    def franc(amount: int):
        return Franc(amount)
```

このチャプターでは、dollarとfrancというstaticmethodが登場した。
これらは引数を受け取ったのち、新しいインスタンスを返すだけの関数。

クラスの属性にアクセスしていなければ、状態を変えるものでもない。
staticmethodの要件を満たすので、これらの関数はstaticmethodであると言える。

まぁ、とりあえず引数にcls, selfとかを必要としないのであればそれはstaticmethodということ。

### 2. abstractmethodについて

『このメソッドは派生クラスで必ず実装してね』という宣言を行うためのもの。

```python
    @abstractmethod
    def times(multiplier: int):
        pass
```

このように親クラスでabstractmethodを使って宣言することで、このクラスを継承したクラス先でtimesを実装しなければならない。

ちなみにPythonではエラーを出すといった強制力はなく、あくまで「実装してね」という意図を伝えるレベルに過ぎない。
