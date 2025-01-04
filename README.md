# robosys2024

# random コマンド
![test](https://github.com/HorigutiStudent/robosys2024/actions/workflows/test.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) \
<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat"> 

任意の範囲の乱数を入手するコマンド

## テスト済み環境
### Local
- Linux OS
    - Ubuntu 22.04
- Python
    - version:  3.10.12    

### GitHubActions
- Linux OS
    - Ubuntu 22.04
- Python 
    - version: 3.7 ~ 3.10

## Installation
```sh
git clone https://github.com/HorigutiStudent/robosys2024_death.git
```
## Usage
```sh 
cd robosys2024  
echo "数値-数値" | ./random
```
二つの数値の間からランダムな値を出力する.  \
両方の数値が整数の場合出力はInt型、 数値のうちいずれかに小数を含む場合は、float型の値を返す.
#### Examples
```sh
#1から5までの中からランダムなInt型の値を取得する
echo 1-5 | ./random   
#3

#1から10までの中からランダムなFloat型の値を取得する
echo 10.0-1 | ./random
#7.271700553301291
```

## LICENSE
- このソフトウェアパッケージは，MITライセンスの下，再頒布および使用が許可される. \
ライセンスの全文は[LICENSE](https://github.com/HorigutiStudent/robosys2024?tab=MIT-1-ov-file)から確認できる.
- © 2025 Horiguchi Masahumi
