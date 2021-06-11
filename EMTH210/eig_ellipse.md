
# Eigenvalues in finding principal axes of ellipses.

The principal axes of an ellipse are axes that have no shearing with respect to
the ellipse. 
<pa_visual.png: The principal axis of this ellipse are `a` and `b`, as vectors >



Lets have an ellipse :

` 4x^2 + 2xy + 4y^2 = 30 `

The ` 2xy ` term immediately tells us that the ellipse is at an angle,
to the x-y axes.


Let us now rewrite the ellipse in matrix form.
(See <pa_matrixform.png>).


To find the principal axes, we will need to diagonalize the matrix:



## Diagonalizing matrices

The diagonal matrix of a matrix  <A>  is defined as:
` D = (P^-1)AP  `,

##### Getting P:
` P^-1 ` is the inverse of matrix P,
and P is made using the eigenvectors of matrix A as coloumns.

##### Getting D:
>>> Cheaty way to get D:
D is a diagonal matrix of eigenvalues from the matrix A.
> The eigenvalues must be in the same order as the eigenvectors in matrix P.
e.g:
```r
P = | 1 2 |     eig_v1 = -3,  ======
    | 3 4 |     eig_v2 = 2        ||
```                               ||
Then D must be:                   ||
```r                              ||
D = |-3 0 |  <<<====================
    | 0 2 |
```

The principal axes of the ellipse will be
```r
 (u, v) = (x, y)*P
```


