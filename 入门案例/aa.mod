MODULE MainModule
PERS speeddata work := [100,20,200,50];
PERS tooldata tPen := [TRUE,[[270,0,50],[1,0,0,0]],[0.1,[0,0,10],[1,0,0,0],0,0,0]];
PERS wobjdata FUWOb0 := [FALSE, TRUE, "" , [[0, 0, 0],[1, 0, 0, 0]],[[0, 0, 0],[1, 0, 0, 0]]];
PROC Main()
ConfL \On;
ConfJ \On;
MoveAbsJ [[0,0,-20,0,-20,180],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
work := [100,5,200,50];
MoveAbsJ [[-65.375,34.174,59.687,-65.424,-91.608,-3.511],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[-50.67,33.805,62.05,-50.817,-93.707,-4.535],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[-35.216,33.717,62.753,-35.389,-95.283,-3.742],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[-19.694,33.757,62.426,-19.8,-95.82,-2.09],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[-4.328,33.81,62.013,-4.351,-95.806,-0.441],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[10.998,33.784,62.211,11.057,-95.885,1.148],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[26.46,33.718,62.744,26.606,-95.783,2.89],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[42.04,33.726,62.675,42.218,-94.75,4.297],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
MoveAbsJ [[57.253,33.926,61.189,57.357,-92.764,4.306],[9E9,9E9,9E9,9E9,9E9,9E9]],work,z10,tPen \WObj:=FUWOb0;
ENDPROC
ENDMODULE
