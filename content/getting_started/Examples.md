---
title: "Examples"
date: "2022-08-17"
draft: false
weight: 40
---

# Automatic Differentiation in Scientific Computing

It goes without saying that `derivatives` are essential in formulating, hence simulating, physical phenomena. However, in real world problems, they can be complicated or error-prone to be derived analytically, and numerical differentiation can introduce round-off errors in the discretization process and cancellation. These problems become more serious with higher derivatives beside being slow. Automatic differentiation, on the other hand, doesn't have any of these problems. 

Differentiation in general is all about chain rule. We know from Calculus that we can differentiate a given composition $h(g(f(x)))$ via 

$$ \operatorname d h = \frac{dh}{dg} \left(\frac{dg}{df} \left(\frac{df}{dx} \operatorname d x \right) \right) .$$

This method is called `forward-mode` and it is mostly used when there are one input and multiple outputs. While forward-mode differentiation is more efficient than other methods, the Scientific Community has shown more interest in cases where there are multiple inputs and a single output. This can be obtained via reverse-mode differentiation. Rearranging the parentheses in the expression above, we will have

$$ \operatorname d h = \left( \left( \left( \frac{dh}{dg} \right) \frac{dg}{df} \right) \frac{df}{dx} \right) \operatorname d x $$

which we can compute with `reverse-mode` via

$$ \underbrace{\bar x}_{\frac{dh}{dx}} = \underbrace{\bar g \frac{dg}{df}}_{\bar f} \frac{df}{dx} .$$

Enzyme is a primarily targeting reverse-mode differentiation, though it supports the forward-mode as well. In the following examples we show some common use cases in scientific computing with both modes.

## Constant Function

Let's start with the simplest case in calculus: constant functions/values. The following example demonstrates that the derivative of a constant function is, indeed, zero.

```c
// constant_rev.c
//  This function demonstrates the derivative of a constant function.

#include <stdio.h>
extern double __enzyme_autodiff(void *);
double Constant() { return 2.; }
double dConstant() { return __enzyme_autodiff((void *) Constant); }
int main() {
    printf(" Constant  = %f \n dConstant = %f \n", Constant(), dConstant());
}
```

One way to compile this code is with the following arguments:
```bash
$ clang constant_rev.c -Xclang -load -Xclang ./Enzyme/ClangEnzyme-13.so -O2 -flegacy-pass-manager 
```

Output:
```bash
 Constant  = 2.000000 
 dConstant = 0.000000 
```
