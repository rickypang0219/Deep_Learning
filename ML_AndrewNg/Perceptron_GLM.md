# CS229 - Perceptron & Generalized Linear Model 

# Introduction 


# Exponential Family 
We say a class of distributions is in exponential family if it can be written in the form 

$$
P(y ; \eta) =  b(y) \exp( \eta^T T(y) - a(\eta))
$$

where $y$ here is the data. The reason of using $y$ is that the exponential family is used to model the output of the data. Here, $\eta$ is the $\textbf{natural parameter}$; $T(y)$ is the $\textbf{Sufficient Statistics}$; and $a(\eta) is the $\textbf{log partition function}$. To see the reason why $a(\eta)$ is called log-partition function, we can rewrite the above distribution as 

$$
P(y; \eta) = \frac{1}{e^{a(\eta)}} b(y) \exp(\eta^T T(y)),
$$

where $\exp(a(\eta))$ acts like a normalization constant for the distribution, similar to the partition function in statistical physics. Therefore, $a(\eta)$ is log-partition funciton. In here, we will use the exponential family to reverse-engineering Bernoulli distribution. For binary classification, the data has Bernoulli distribution 

$$
\begin{align}
P(y; \phi) =  \phi^y (1-\phi)^{(1-y)}
\end{align}
$$

where $\phi$ is the probability of the an event. 

