# Classes & Pointers 


# Big O notation (Review)
The big O notation access the complexity of a given program, including space and time complexity. Here, we introduce three notation for the following example. Suppose we have an list 

```python
arr =  [1,2,3,4,5,6,7]
```
Our goal is to find '1' in the given array. If we are able to find our target in one iteration, we call the time complexity as $\Omega$. Where the worst case is to scan through all the elements in the given array and return the target, it requires $O$ complexity, denoting the worst case. The average complexity is $\theta$. Here is an example code for $O(n)$ time complexity in Python: 

``` python
# n = 10 for instance
def print_n(n):
    for i in range(n):
        print(i)

print_n(10)
```

This example costs $O(n)$ since we need to print every value one by one. Apart from $O(n)$, there are other kind of complexity such as $O(n^p)$ or $O(\log(n))$. Here is one example for power-law complexity which appears in matrix computations or nested loop : 

```python
def print_items(n): 
    for i in range(n): 
        for j in range(n):
            print(i.j)

print_items(10)
```

Lastly, we dicuss constant time complexity which denotes at $O(1)$. For instance, when we add numbers together, the time complexity is constant time since the addition of numbers does not require loop. Therefore, it can be done in constant time. 



# Classes In Python
Classes are fundamental object in object-oriented programming. Besides, every data structure we created here are based on classes. For instance, we can construct linked list as follow 

```python
class LinkedList:

    def __init__(self,value):
    
    def append(self, value):
    
    def pop(self, value):
    
    def prepend(self, value): 
    
    def insert(self, index, value)

    def remove(self, index)
```


# Pointers (Integer)
If we use any data structure in programming, that data structure must be stored in a certain memory location in our computer. For instance, if we set ```a = 1```, then ```a``` is now stored in the memory whose ```id = 4344963992```. The pointer of different data structure work differently. Let's consider the integer case.

```python
num1 = 1 
num2 = num1 

print("Is num2 points to num1 position?", id(num1) == id(num2)) # retuen True
```
In this example, their ```id```'s match so `num2` indeed points to the same location as `num1`. We can think that there are two arrows pointing to the `id =  4344963992` from both `num1` and `num2`. Next, we are interested in assigning `num2` with different values as `num1`. 

```python 
num1 = 1 
num2 = num1 

num2 = 2 
print("Is num2 points to num1 position?", id(num1) == id(num2)) # return False
```

The questions are: 
1. Will assigning `num2 = 2` change the pointer direction? 
2. Will `num2 = 2` overwrite `num1`, meaning that now `num1 = 2` or `num` points to `id(2)` after this assignment? 

The answers of these questions are: 
1. Yes, now `num2` points to `id(2)` instead of `id(1)`
2. No, `num1` still points at `id(1)` after the assignemnt of `num2 = 2`.

The reason of these is that integer are called **immutable**, which means they cannot be changed. Once `1` is created in certain memory location, we cannot change it, but we can change how `num1` point to other location. 


# Pointers (Dictionary)
Here we investigate the pointer of dictionary. In Python, we can create dictionary as follow

```python
# dictionary with key - value , and contains value - 1 
dict1 = {'value':1}
```

The variable `dict1` points  at the dictionary in memory. Now, we create another dictionary `dict2` by assigning `dict2 = dict1`. 

```python
dict1 = {'value':1}
dict2 = dict1

print(id(dict1)) # output: id = 4347810304
print(id(dict2)) # output: id = 4347810304
```



The varibale `dict2` now points at the same dictionary at memory, similar to integer case. Next, we want to know whether the modification of `dict2` value would overwrite the value in `dict1`. 

```python
dict1 = {'value':1}
dict2 = dict1

# print id of dict1 and dict2
print(id(dict1))
print(id(dict2))



# modify the dict2 value 
dict2['value'] = 2 

# print dict1 and dict2
print(dict1)
print(dict2)

# print id of dict1 and dict2
print(id(dict1))
print(id(dict2))


```

After running above code, we see that the output of `id(dict1) == id(dict2)`  is `True`, meaning that the modification of `dict2` indeed changes the pointer of `dict1`. Most importantly, the `id(dict1)` is as same as before. Besides, if we print them out, they are actually the same 

```python 
# id before modification 
id(dict1) = 4347810304
id(dict2) = 4347810304

#  dict output
dict1 = {'value':2}
dict2 = {'value':2}

#  id after modification 
id(dict1) = 4347810304
id(dict2) = 4347810304

```
Therefore, we can see the fundamental difference between integers and dictionaries. In integer case, integers are immutable and we cannot change the location of memory once they are created. However, for dictionaries we can change the value in that memory location after modification.

Lastly, if we add `dict3` to the code and try to point both `dict1` and `dict2` to `dict3', we have the following in the code. 

```python
dict1 = { 'value':11 }
dict2 = dict1 

# Before  Modification 
print('Before modification')
print('\n dict1 points to ',id(dict1)) # locate at 4310047552
print('dict2 points to ',id(dict2)) # locate at 4310047552




# Change the values 
dict2['value'] = 22 

print("After changeing value, is dict2 points to dict1 memory location?", id(dict1) == id(dict2))


dict3 = {'value': 33} # locate at  4310047552
dict2 = dict3 
dict1 = dict2

# After Modification 
print('After modification')
print('\n dict1 points to ',id(dict1))
print('dict2 points to ',id(dict2))
print('dict3 points to ',id(dict3))
```

After executing this code, now `dict1` and `dict2` points to the memory location of `dict3' after modification with 

```python
dict1 = {'value':33} # locate at  4310047552
dict2 = {'value':33} # locate at  4310047552 
dict3 = {'value':33} # locate at  4310047552
```

However, there is no variables pointing to memory at `id = 4310047552` where `dict1' and `dict2` used before modification. In such case, Python will remove this via garbage collection. 