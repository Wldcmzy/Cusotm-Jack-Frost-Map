import numpy as np
from .MapDict import mapdict
from .Objects import PLAYER1, PLAYER2
from pathlib import Path

class Map:
    mapbase = '''
<level>
<ground>
{ground}
</ground>
<objects>
{objects}
</objects>
<bg>
{bg}
</bg>
<paths>
</paths>
<signs>
</signs>
</level>
'''.strip()

    def __init__(self, size: tuple[int]):
        self.initial(size)
    
    def initial(self, size: tuple[int]):
        self.default = np.zeros(size, dtype=np.int8)
        self.ground = self.default.copy()
        self.objects = self.default.copy()
        r, c = size
        if c > 36: print('不建议地图宽度大于36, 可能会出问题')
        
    def fill_row(self, row: int):
        '''
        完全填充一行
        row=行号
        '''
        r, c = self.ground.shape
        self.ground[-row] = np.ones((1, c))

    def fill_bottom(self):
        '''完全填充地图底部'''
        self.fill_row(1)
    
    def seprate_row(self, row: int, length: tuple[int], prefix: int = 0):
        '''
        填充一条有间隔的线
        row=行号
        lenght=(每段填充长度,每段间隔长度)
        prefix=前导间隔长度
        '''
        o, z = length
        r, c = self.ground.shape
        x:list = [1] * o + [0] * z
        y = x.copy()
        while len(y) < c:
            y.extend(x)
        self.ground[-row] = np.array(([0] * prefix + y)[ : c])
    
    def set_object(self, pos: tuple[int], index: int):
        '''在指定位置放置生物或物体'''
        r, c = pos
        self.objects[-r][c - 1] = index
    
    def set_start_pos(self, player1: tuple[int] = (2, 1), player2: tuple[int] = (2, 3)):
        '''设置玩家初始位置, 默认左下角(2, 1), (2, 3)'''
        self.set_object(player1, PLAYER1)
        self.set_object(player2, PLAYER2)
    
    def matrix2xml(self, matrix: np.ndarray) -> str:
        ret = f''
        for row in matrix:
            ret += f"<row>{str(row.tolist())[1 : -1].replace(' ', '')}</row>\n"
        return ret.strip()

    def warp(self) -> str:
        return self.mapbase.format(
            ground = self.matrix2xml(self.ground),
            objects = self.matrix2xml(self.objects),
            bg = self.matrix2xml(self.default),
        )
    
    def toxml(self, index: int, path: str = '../areas/'):
        '''生成xml文件'''
        filename = mapdict[index]
        print(filename)
        with open(path + filename, 'w', encoding='utf-8') as f:
            f.write(self.warp())