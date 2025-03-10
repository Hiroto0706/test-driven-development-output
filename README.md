# What is this?
これは「[テスト駆動開発](https://www.amazon.co.jp/%E3%83%86%E3%82%B9%E3%83%88%E9%A7%86%E5%8B%95%E9%96%8B%E7%99%BA-Kent-Beck/dp/4274217884)」のアウトプット用のリポジトリになります。

![alt text](/assets/image.png)

# Requirements this practice

## WyCash 多国通貨システム要件

| 要件 | 説明 |
|------|------|
| 1. 多国通貨対応 | 価格と合計に通貨情報を追加する（USD、CHF など） |
| 2. 通貨換算 | 異なる通貨間の為替レートを定義する |
| 3. 基準通貨計算 | すべての合計を基準通貨（USD など）に換算する |

## 現在の状態と目標

### 現在のシステム
| 銘柄 | 株数 | 価格 | 合計 |
|------|------|------|------|
| IBM | 1000 | 25 | 25000 |
| GE | 400 | 100 | 40000 |
|  |  | 総計 | 65000 |

### 目標システム
| 銘柄 | 株数 | 価格 | 合計 |
|------|------|------|------|
| IBM | 1000 | 25 USD | 25000 USD |
| Novartis | 400 | 150 CHF | 60000 CHF |
|  |  | 総計 | 65000 USD |

### 必要な為替レート定義
| 換算元 | 換算先 | レート |
|--------|--------|--------|
| CHF | USD | 1.5 |
=======
# How to proceed this repo

I develop test code following the book.

Create a repository for each chapter.

For example, for Chapter 1, I will work in a repository called practice_01.

# What I learned
