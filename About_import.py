"""
1.
������|�g�k�H�����ɸ��|���D

python2 ����䤣��h�|�Himport�������ɮת����|��@�ثe���|�A��@���A
�p�G�g������|�A���H�����ɬ�������|�䤣�쪺��
�N�|�۰�
import a.b.c
�ݦ� from . import a.b.c

��python3
�g�����諸�ܡA�N�O�n�ݰ����ɸ��|���D�A�S�o�Ӷq

����۹���|
���੹�W���������ɦP�@�h�A�]���۹���|�ȭ���Φbmodule���A�O�o�˶�?������ɦP�@�h�N����module�h��
�|�X�{ValueError: Attempted relative import in non-package��error
��������|�N�S�t
�N�O���b�����ɸ�a�P�@�h�����p�U
from a import b	�i�H
��
from .a import b �|error
�άO���ӻ��A���۹���|��.py�ɡA���ઽ������A�u��Ψ�import
http://kuanghy.github.io/2016/07/21/python-import-relative-and-absolute
�g���g

-----------------------
from .. import XX.XX �o�Ӽg�k�Pı�N�����D�A
���w�gfrom�F
import ���ӥu���@�h�a?

---------
����python -m xxx.xxx
�N��N�۷��]�@�� python main.py
�M��main.py�̭�import xxx.xxx

"""