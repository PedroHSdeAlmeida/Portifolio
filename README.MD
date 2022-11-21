•UTILIZANDO A APLICAÇÃO
1. Crie um diretório
   
- Crie um diretório e navegue até ele atraves da linha de comando.

```console
    mkdir <nome do diretório>
    cd <nome do diretório>
```

2. Clone o repositório

```console
    git clone https://github.com/Miguel-C1/portifolio .
```
- Repare que no final tem um ponto, ele é colocado propositalmente para que não seja criado mais um diretório dentro desse recém criado por você.

3. Crie um ambiente virutal

```console
    python -m venv <nome do ambiente>
```
- Utilizamos a variável de ambiente 'python' citada na sessão de instalação, caso esse comando falhe no seu ambiente tente:
```console
    python3 -m venv <nome do ambiente>
```
- Caso mesmo assim o diretório com o nome do ambiente não seja criado assegure-se que o **python está configurado em suas variáveis de ambiente** e tente novamente o processo.

4. Executar o ambiente virtual

- No CMD do Windows:

```console
    cd <nome do ambiente>\Scripts
    activate.bat
```

- No PowerShell do Windows:

```console
    .\<nome do ambiente>\Scripts\Activate.ps1
```  

- No Unix(Linux)/MacOS:
```console
    source <nome do ambiente>/bin/activate
```

5. Instale as dependências:

- Navegue até a raiz do diretório e execute o comando:
```console
    pip install -r requirements.txt
```

6. Executando a aplicação

- Navegue até a pasta src dentro dessa pasta raíz através da linha de comando e execute o arquivo 'app.py'.

```console
    cd src
    python app.py
```