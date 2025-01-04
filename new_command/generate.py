#!/usr/bin/python3

# SPDX-FileCopyrightText: 2025 Horiguchi Masahumi 
# SPDX-License-Identifier: MIT

import random
from typing import Union

from new_command.parce_input_data import Type


class Generate:
    def __init__(self):
        pass
      
      
    def execute(self,min:Union[int,float],max:Union[int,float],type:Type) -> Union[int,float]:
        """ランダムな値を生成する"""
        if type == Type.INT:
            value = random.randint(min,max)
        elif type == Type.FLOAT:
            value = random.uniform(min,max)
        
        return value
      
      
if __name__ == "__main__":
    g = Generate()
    val = g.execute(1.1,10,Type.FLOAT)
    
    print(val)