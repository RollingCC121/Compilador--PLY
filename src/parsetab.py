
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE EQUALS IDENTIFIER LPAREN MINUS NUMBER PLUS RPAREN TIMESstatement : IDENTIFIER EQUALS expressionexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expressionexpression : LPAREN expression RPARENexpression : NUMBER'
    
_lr_action_items = {'IDENTIFIER':([0,],[2,]),'$end':([1,4,6,12,13,14,15,16,],[0,-1,-7,-2,-3,-4,-5,-6,]),'EQUALS':([2,],[3,]),'LPAREN':([3,5,7,8,9,10,],[5,5,5,5,5,5,]),'NUMBER':([3,5,7,8,9,10,],[6,6,6,6,6,6,]),'PLUS':([4,6,11,12,13,14,15,16,],[7,-7,7,7,7,7,7,-6,]),'MINUS':([4,6,11,12,13,14,15,16,],[8,-7,8,8,8,8,8,-6,]),'TIMES':([4,6,11,12,13,14,15,16,],[9,-7,9,9,9,9,9,-6,]),'DIVIDE':([4,6,11,12,13,14,15,16,],[10,-7,10,10,10,10,10,-6,]),'RPAREN':([6,11,12,13,14,15,16,],[-7,16,-2,-3,-4,-5,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([3,5,7,8,9,10,],[4,11,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IDENTIFIER EQUALS expression','statement',3,'p_statement_assign','analizadorSintactico.py',6),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','analizadorSintactico.py',10),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','analizadorSintactico.py',11),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','analizadorSintactico.py',12),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','analizadorSintactico.py',13),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','analizadorSintactico.py',17),
  ('expression -> NUMBER','expression',1,'p_expression_number','analizadorSintactico.py',21),
]