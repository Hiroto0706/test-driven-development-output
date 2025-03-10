# What is this?
This is the output repository for 'テスト駆動開発'.

https://www.amazon.co.jp/%E3%83%86%E3%82%B9%E3%83%88%E9%A7%86%E5%8B%95%E9%96%8B%E7%99%BA-Kent-Beck/dp/4274217884

![alt text](/assets/image.png)

# Requirements this practice

## WyCash Multi-Currency System Requirements

| Requirement | Description |
|-------------|-------------|
| 1. Multi-currency support | Add currency information to prices and totals (USD, CHF, etc.) |
| 2. Currency conversion | Define exchange rates between different currencies |
| 3. Base currency calculation | Convert all totals to a base currency (e.g., USD) |

## Current State and Goal

### Current System
| Symbol | Shares | Price | Total |
|--------|--------|-------|-------|
| IBM | 1000 | 25 | 25000 |
| GE | 400 | 100 | 40000 |
|  |  | Grand Total | 65000 |

### Target System
| Symbol | Shares | Price | Total |
|--------|--------|-------|-------|
| IBM | 1000 | 25 USD | 25000 USD |
| Novartis | 400 | 150 CHF | 60000 CHF |
|  |  | Grand Total | 65000 USD |

### Required Exchange Rate Definition
| From | To | Rate |
|------|-----|------|
| CHF | USD | 1.5 |