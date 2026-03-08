# Python Cheatsheet

## Strings

```python
s = "hello world"
s.upper()                  # "HELLO WORLD"
s.strip()                  # remove espacos nas pontas
s.split(" ")               # ["hello", "world"]
s.replace("hello", "hi")   # "hi world"
f"valor: {variavel}"       # f-string (formatacao)
"sep".join(["a","b","c"])  # "a sep b sep c"
```

## Listas

```python
lst = [1, 2, 3]
lst.append(4)              # [1, 2, 3, 4]
lst.extend([5, 6])         # [1, 2, 3, 4, 5, 6]
lst.pop()                  # remove e retorna ultimo
lst.insert(0, 99)          # insere na posicao
lst[1:3]                   # slice [2, 3]
lst[::-1]                  # inverte a lista
sorted(lst, key=len)       # ordena com criterio
[x**2 for x in lst if x>2] # list comprehension
```

## Dicts

```python
d = {"a": 1, "b": 2}
d.get("c", 0)              # retorna 0 se nao existir
d.keys() / d.values() / d.items()
d | {"c": 3}               # merge (3.9+)
{k: v for k, v in d.items() if v > 1}  # dict comprehension
```

## Sets

```python
s = {1, 2, 3}
s.add(4)
s1 & s2                    # intersecao
s1 | s2                    # uniao
s1 - s2                    # diferenca
```

## Controle de Fluxo

```python
# ternario
x = "par" if n % 2 == 0 else "impar"

# walrus operator (3.8+)
if (n := len(lst)) > 5:
    print(f"lista grande: {n}")

# match/case (3.10+)
match status:
    case 200: print("ok")
    case 404: print("not found")
    case _:   print("outro")
```

## Funcoes

```python
def func(a, b=10, *args, **kwargs): ...

# lambda
dobro = lambda x: x * 2

# unpacking
a, *rest = [1, 2, 3, 4]   # a=1, rest=[2,3,4]
def f(a, b): ...
f(**{"a": 1, "b": 2})     # unpacking dict como args
```

## Arquivos

```python
with open("file.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()        # tudo
    linhas = f.readlines()     # lista de linhas

from pathlib import Path
p = Path("dir/file.txt")
p.exists() / p.read_text() / p.stem / p.suffix
```

## Uteis do Dia a Dia

```python
# enumerate
for i, val in enumerate(lst, start=1): ...

# zip
for a, b in zip(lista1, lista2): ...

# any / all
any(x > 5 for x in lst)
all(x > 0 for x in lst)

# map / filter
list(map(str, [1,2,3]))        # ["1","2","3"]
list(filter(lambda x: x>2, lst))

# collections
from collections import Counter, defaultdict
Counter("abracadabra")         # {'a':5, 'b':2, ...}
dd = defaultdict(list)
```

## Tratamento de Erros

```python
try:
    resultado = 10 / x
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except (TypeError, ValueError):
    print("tipo ou valor invalido")
finally:
    print("sempre executa")
```

## Tipos (Type Hints)

```python
def soma(a: int, b: int) -> int:
    return a + b

from typing import Optional
def buscar(id: int) -> Optional[str]: ...

# 3.10+
def f(x: int | str) -> None: ...
```

## One-liners Uteis

```python
# achatar lista de listas
flat = [x for sub in nested for x in sub]

# contar ocorrencias
from collections import Counter
Counter(lst).most_common(3)

# remover duplicatas mantendo ordem
list(dict.fromkeys(lst))

# inverter dict
{v: k for k, v in d.items()}
```
