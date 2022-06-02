print ( " Ingrese el costo de la Memoria RAM 4GB para PC: " )

a = input ()

print ( " Ingrese el costo del Pendrive 16B: " )
 
b = input ()

print ( " Ingrese el costo del Disco Rigido Interno de 2TB: " )

c = input ()

cm = float (a)/ 4

P = float (b) / 16

R = float (c) / 2000

d = float (a) / float (b)

e = float (a) / float (c)

f = cm / P

g = cm / R

print ( " El costo de la Memoria RAM 4GB para PC es: ", cm )

print ( " El costo del Pendrive 16GB: ", P )

print ( " El costo del Disco Rigido interno de 2TB: ", R )

print ( " La variacion del costo entre la memoria RAM 4GB para PC y el pendrive de 16GB es del ", d , '% mas cara. ' )

print ( " La variacion del costo entre la memoria RAM 4GB para PC y disco Rigido de 2TB es del ", e , '% mas cara. ' )

print ( " La variacion del costo entre la memoria RAM 4GB para PC y el pendrive de 16GB por giga: " , f )

print ( " La variacion del costo entre la memoria RAM 4GB para PC y disco Rigido de 2TB por giga: " , g ) 
