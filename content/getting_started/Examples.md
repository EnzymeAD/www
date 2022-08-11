# Automatic Differentiation in Scientific Computing

It goes without saying that `derivatives` are essential in formulating, hence simulating, physical phenomena. However, in real world problems, they can be complicated or error-prone to be deriven analytically, and numerical differentiation can introduce round-off errors in the discretization process and cancellation. These problems become more serious with higher derivatives beside being slow. Automatic differentiation, on the other hand, doesn't have any of these problems. 

Differentiation in general is all about chain rule. We know from Calculus that we can differentiate a given composition $h(g(f(x)))$ via 

$$ \operatorname d h = \frac{dh}{dg} \left(\frac{dg}{df} \left(\frac{df}{dx} \operatorname d x \right) \right) .$$

This method is called `forward-mode` and it is mostly used when there are one input and multiple outputs. While forward-mode differentiation is more efficient than other methods, the Scientific Community has shown more interest in cases where there are multiple inputs and a single output. This can be obtained via reverse-mode differentiation. Rearranging the parentheses in the expression above, we will have

$$ \operatorname d h = \left( \left( \left( \frac{dh}{dg} \right) \frac{dg}{df} \right) \frac{df}{dx} \right) \operatorname d x $$

which we can compute with `reverse-mode` via

$$ \underbrace{\bar x}_{\frac{dh}{dx}} = \underbrace{\bar g \frac{dg}{df}}_{\bar f} \frac{df}{dx} .$$

Enzyme is a primarily targeting reverse-mode differentiation, though it supports the forward-mode as well. In the following examples we show some common use cases in scientific computing with both modes.
