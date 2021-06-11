

# Multiple ODE solving using eigenvalues

### NOTE: we use `t` here instead of `x` for variable.

```js

let y1* = dy1/dt  
let y2* = dy2/dt


let  Y = [ y1,  y2 ] // y1 and y2 are unknown!!

let Y* = [ y1*, y2* ]// known

/*
If you come across a set of equations where you can
put in the matrix form:
*/

Y* = AY // where A is regular matrix,

/*
Then we can guess a solution similar to how we did it before:
*/

// Lets guess ==>
Y = X*e^(λ*t) // Where X is a constant vector.

// this means that
Y* = λ*X*e^(λ*t) // simple differentiation rules

// And from here, we can rewrite initial equation,
// to solve for our lambdas:

Y* = AY
λ*X*e^(λ*t) = A*(X*e^(λ*t)) //   X * e^(λ*t) =/= 0, so we can divide.
λI = A
det(A-λI) = 0 // oooh shit! lambda is eigenvalue!!!!

// Find lambda values
// Boom, you have your general solutions:
y1(t)
y2(t)

// If given initial conditions, solve for the components of vector X.


```