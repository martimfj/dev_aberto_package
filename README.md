# Aula 10 - Distribuição de programas escritos em Python
Esta é uma atividade da matéria [Desenvolvimento Aberto (2020/2)](https://insper.github.io/dev-aberto), que foi criado 
um pacote Python instalável via pip.

### Exercícios
###### Qual seria o import a ser feito para usar a função *hello* do arquivo `dev_aberto.py`?
- Para acessar uma função X escrita no arquivo `dev_aberto.py`, seria necessário importá-la usando: `from dev_aberto.dev_aberto import X`.

###### Para que serve o arquivo `__init__.py`?
- O arquivo `__init__.py` é utilizado para identificar diretórios como detentores de um pacote Python. Ele pode ser um 
arquivo vazio, como também pode conter código de inicialização do pacote.


### Pacote no PyPi
O projeto se encontra no PiPy Test, um ambiente separado de outras distribuições: https://test.pypi.org/project/dev-aberto-martimfj/

Para utilizar:
```
pip install -i https://test.pypi.org/simple/ dev-aberto-martimfj
```

### Dependências do pacote
As dependências para buildar o pacote podem ser instalada de duas maneiras:

##### Pipenv (`pip install pipenv`)
```
$ pipenv install
$ pipenv shell
```

##### Pip
```
$ pip install -r requirements.txt
```