# CS229 - Classification and Logistic Regression 

# Introduction 
Logistic regression is an example of classication problem. For binary classification problems the outputs $y$ is either $0$ or $1$, and indeed we can generalise logistic regression to multiple-class case. One real-life example is the classification of breast cancer whether $1$ means positive and $0$ means negative. 

# Logistic Regression 
In logistic regression, we want our hypothesis $h_\theta(x)$ to have output $y \in [0,1]$. Therefore, directly using linear regression result is not valid here. To fix this issue, one is to use $\textbf sigmoid$ function such that 

$$
h_\theta(x) = g( \theta^T x) = \frac{1}{1 + e^{-\theta^Tx} } ,~ g(z) = \frac{1}{1 + e^{-z} },
$$
where $g(z)$ is the sigmoid function. 


# Cost Function of Logistic Regression 
Similar to linear regression, we fit the parameter $\theta$ via optimization such as batch gradient descent or stochastic gradient descent. Before optimizaton process we need to define the cost function. The cost function of logistic regressin can be found using principle of maximal likelihood. First we assume that the data has the following distribution

$$
\begin{align}
P( y = 1| x ;\theta) &= h_\theta (x) \\ 
P( y = 0| x ;\theta) &= 1- h_\theta (x).
\end{align}
$$

In the breast cancer example the distribution $P( y = 1| x ;\theta)$ refers to the cahnce of the tumor being cancerous, which is the same as our hypothesis $h_\theta(x)$, where $x$ and $y$ are the tumor size and degree of being cancerous, respectively. Therefore, it is intuitive to set $P( y = 0| x ;\theta) = 1- h_\theta (x)$
because $y$ can only be 1 or 0 ($y \in \{ 0,1\}$ for binary classification). Therefore, the distribution being not cancerous should be 

$$
P( y = 0| x ;\theta) = 1- P( y = 1| x ;\theta). 
$$

Because of $y \in \{ 0,1\}$, we can combine the above distribution in one line 

$$
P(y \vert x; \theta ) =  h_\theta(x)^{y} ( 1-h_\theta )^{1-y},~ y\in \{0, 1 \}, 
$$

which is the Bernoulli distribution. Having $m$ training examples were generated indepdently, we can write down the likelihood of the parameters as 

$$
\begin{align}
L(\theta) &= P( \vec y \vert X; \theta)  \\ 
&= \prod^m_{i=1} P(y^{(i)} \vert x^{(i)}; \theta ) \\ 
&= \prod^m_{i=1}  h_\theta(x^{(i)})^{y^{(i)}} ( 1-h_\theta(x^{(i)}) )^{1-y^{(i)}}
\end{align}
$$

As before, we optimize the log-likelihood: 

$$
l(\theta) = \sum_{i=1}^m y^{(i)} \log (h_\theta (x^{(i)}))  + (1- y^{(i)}) \log (1 - h_\theta (x^{(i)}))
$$

then the remaining task is to find $\theta$ which maximizes the log-likelihood. 

# Perceptron 