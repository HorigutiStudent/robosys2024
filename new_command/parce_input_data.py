#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import sys
import re

from enum import Enum

#条件分岐で文字列を使用するのを避ける
class Type(Enum):
    INT = 0
    FLOAT = 1
    #--使わなかった--
    #STR = 2
    #DOUBLE = 3
    

class ParceInputData:
    def __init__(self,):
        self.input_data = ""

  
    def get_data(self) -> str:
        """コマンドラインからの入力を読み取る"""
        self.input_data = sys.stdin.read().strip()
        return self.__split() 


    def get_type(self,values:tuple[str,str]) -> Type:
        """Float型を使うかInt型を使うかを判断"""
        for val in values:
            if '.' in val:
              return Type.FLOAT
        
        return Type.INT
      
      
    def to_num(self,strs:list[str,str],type:Type=Type.INT) -> list:
        """文字列から数値に変換"""
        inputs = []
        for num in strs:
            if type == Type.INT:
                inputs.append(int(num))
            elif type == Type.FLOAT:
                inputs.append(float(num))
            else:
                raise KeyError(f"the type {type} is unexpected")
        #最大・最小値が逆に入力されても対応できるようにした
        if inputs[0] > inputs[1]:
            min = inputs[1]
            max = inputs[0]
            inputs = [min,max]
        return inputs
      
      
    def __split(self) -> list[str,str]:
        """入力を欲しい形へ変形する"""
        #正規表現を使ってハイフン(-)で分割
        pattern = r"^-?(\d+(\.\d+)?)-(-?\d+(\.\d+)?)$"
        # pattern = r"(-?\d+\.\d+|-?\d+)-(-?\d+\.\d+|-?\d+)"
        match = re.search(pattern,self.input_data)
        if match:
            n1 = match.group(1)
            n2 = match.group(3)
        else:
            raise ValueError("Input value is invalid")
        
        return n1,n2
          
        
if __name__ == "__main__":
    p = ParceInputData()
    #入力値を読み取っているか
    n1,n2 = p.get_data()
    print(n1,n2)
    #入力値の小数点・整数を区別できているか
    types = p.get_type((n1,n2))
    print(types)
    #入力値を数値に変換できているか
    nums = p.to_num((n1,n2),types)
    print(nums)
    print(type(nums[0]))