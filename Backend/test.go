/*----------- HEADER -----------*/
package main

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17, t18 float64

var P, H float64
var stack [30101999]float64
var heap [30101999]float64

/* --- NATIVAS --- */
/*----------- FUNCION length -----------*/
func length() {
	t4 = 0
L0:
	t3 = heap[int(H)]
	if t3 == -1 {
		goto L1
	}
	t4 = t4 + 1
	H = H + 1
	goto L0
L1:
	stack[int(P)] = t4

	return
}

/* Funcion printArray*/
/*----------- FUNCION printArray -----------*/
func printArray() {
	t8 = P + 1
	t9 = stack[int(t8)]
	t10 = heap[int(t9)]
	fmt.Printf("%c", int(91))
	t11 = t9 + 1
	t12 = 0
L2:
	if t12 != t10 {
		goto L3
	}
	goto L5
L3:
	t13 = heap[int(t11)]
	fmt.Printf("%f", float64(t13))
	t14 = t10 - 1
	if t14 == t12 {
		goto L4
	}
	fmt.Printf("%c", int(44))
	t12 = t12 + 1
	t11 = t11 + 1
	goto L2
L4:
	fmt.Printf("%c", int(93))
	t12 = t12 + 1
	t11 = t11 + 1
	goto L2
L5:
	return
}

func main() {
	/* Declaracion de un array*/
	/* Compilación del array*/
	t0 = H
	t1 = t0 + 1
	heap[int(H)] = 11
	H = H + 12
	heap[int(t1)] = 1
	t1 = t1 + 1
	heap[int(t1)] = 2
	t1 = t1 + 1
	heap[int(t1)] = 3
	t1 = t1 + 1
	heap[int(t1)] = 5
	t1 = t1 + 1
	heap[int(t1)] = 67
	t1 = t1 + 1
	heap[int(t1)] = 78
	t1 = t1 + 1
	heap[int(t1)] = 8
	t1 = t1 + 1
	heap[int(t1)] = 8
	t1 = t1 + 1
	heap[int(t1)] = 65
	t1 = t1 + 1
	heap[int(t1)] = 4
	t1 = t1 + 1
	heap[int(t1)] = 4
	t1 = t1 + 1
	stack[int(0)] = t0
	/* Fin de la compilación del array*/
	t2 = H
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	/* ------- Length ---------*/
	/*----------- NUEVO ENTORNO -----------*/
	P = P + 1
	H = t2
	length()
	t5 = stack[int(P)]
	P = P - 1
	/*----------- RETORNA ENTORNO -----------*/

	fmt.Printf("%f", float64(t5))
	fmt.Printf("%c", int(10.0))
	/* Compilación del array*/
	t6 = H
	t7 = t6 + 1
	heap[int(H)] = 4
	H = H + 5
	heap[int(t7)] = 1
	t7 = t7 + 1
	heap[int(t7)] = 2
	t7 = t7 + 1
	heap[int(t7)] = 3
	t7 = t7 + 1
	heap[int(t7)] = 4
	t7 = t7 + 1
	/* Fin de la compilación del array*/
	t15 = P + 1
	t15 = t15 + 1
	stack[int(t15)] = t6
	/*----------- NUEVO ENTORNO -----------*/
	P = P + 1
	printArray()
	t16 = stack[int(P)]
	P = P - 1
	/*----------- RETORNA ENTORNO -----------*/

	fmt.Printf("%c", int(10.0))
	t17 = H
	heap[int(H)] = 97
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = 98
	H = H + 1
	heap[int(H)] = -1
	H = H + 1
	/* ------- Length ---------*/
	/*----------- NUEVO ENTORNO -----------*/
	P = P + 1
	H = t17
	length()
	t18 = stack[int(P)]
	P = P - 1
	/*----------- RETORNA ENTORNO -----------*/

	fmt.Printf("%f", float64(t18))
	fmt.Printf("%c", int(10.0))
}
