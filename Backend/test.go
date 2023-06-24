/*----------- HEADER -----------*/
package main;

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16 float64; 

var P, H float64;
var stack[30101999] float64;
var heap[30101999] float64;
/* --- NATIVAS --- */
/* Funcion stringNumber*/
/*----------- FUNCION typeNumber -----------*/
func typeNumber() {
t10 = H;
heap[int(H)]= 78;
H = H + 1;
heap[int(H)]= 117;
H = H + 1;
heap[int(H)]= 109;
H = H + 1;
heap[int(H)]= 98;
H = H + 1;
heap[int(H)]= 101;
H = H + 1;
heap[int(H)]= 114;
H = H + 1;
heap[int(H)]= -1;
H = H + 1;
stack[int(t11)]= t10;
return;
}
/*----------- FUNCION printString -----------*/
func printString() {
	t12 = P + 1;
	t13 = stack[int(t12)];
L6:
	t14 = heap[int(t13)];
	if t14 == -1 {goto L5;}
	fmt.Printf("%c", int(t14));
	t13 = t13 + 1;
	goto L6;
L5:

return;
}

func main() {
	/* Declaracion de un array*/
	/* Compilación del array*/
	t0 = H;
	t1 = t0 + 1;
	heap[int(H)]= 4;
	H = H + 5;
	heap[int(t1)]= 1;
	t1 = t1 + 1;
	heap[int(t1)]= 2;
	t1 = t1 + 1;
	heap[int(t1)]= 3;
	t1 = t1 + 1;
	heap[int(t1)]= 7;
	t1 = t1 + 1;
	stack[int(0)]= t0;
	/* Fin de la compilación del array*/
	/* ------- TypeOf ---------*/
	t2 = 0;
	/* ACCESO ARRAY*/
	t3 = stack[int(0)];
	t4 = heap[int(t3)];
	t5 = 0;
	t6 = t4 - 1;
	t3 = t3 + 1;
	if 0 > t6 {goto L3;}
	goto L0;
	L0:
			if t5 <= t6 {goto L1;}
			goto L3;
	L1:
			if t5 == t2 {goto L2;}
			t5 = t5 + 1;
	t3 = t3 + 1;
	goto L0;
	L2:
			t7 = heap[int(t3)];
	goto L4;
	L3:
			/* ERROR NO SE PUDO ACCESAR AL ARRAY*/
			fmt.Printf("%c", int(69));
			fmt.Printf("%c", int(82));
			fmt.Printf("%c", int(82));
			fmt.Printf("%c", int(79));
			fmt.Printf("%c", int(82));
			fmt.Printf("%c", int(10));
			L4:
	/* Fin del acceso del array*/
	/*----------- NUEVO ENTORNO -----------*/
	P = P + 1;
	t8 = P + 1;
	stack[int(t8)]= t7;
	typeNumber();
	t9 = stack[int(P)];
	P = P - 1;
	/*----------- RETORNA ENTORNO -----------*/

	t15 = P + 1;
	t15 = t15 + 1;
	stack[int(t15)]= t9;
	/*----------- NUEVO ENTORNO -----------*/
	P = P + 1;
	printString();
	t16 = stack[int(P)];
	P = P - 1;
	/*----------- RETORNA ENTORNO -----------*/

	fmt.Printf("%c", int(10.0));
}