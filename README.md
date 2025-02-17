# EAN-13 Checker com GUI

Este projeto é um validador de códigos de barras EAN-13 com uma interface gráfica simples utilizando Tkinter.

## 📌 Funcionalidades
- Interface gráfica para entrada do código EAN-13
- Cálculo do dígito verificador
- Exibição do EAN completo e do dígito verificador na tela

## 🛠 Tecnologias Utilizadas
- Python 3.x
- Tkinter (GUI)

## 📂 Estrutura do Projeto
```
/
|-- eanchecker.py   # Código principal do validador EAN-13 com GUI
|-- README.md       # Documentação do projeto
```

## 🚀 Como Executar
1. Certifique-se de ter o Python 3.x instalado na sua máquina.
2. Baixe ou clone este repositório.
3. No terminal, navegue até o diretório do projeto e execute:
   ```bash
   python eanchecker.py
   ```
4. Digite um código EAN-13 na interface e pressione `Enter` para validar.

## 📖 Como Funciona
- O usuário insere um código de barras na entrada de texto.
- Ao pressionar `Enter`, o programa calcula o dígito verificador e exibe:
  - O dígito verificador calculado
  - O código EAN-13 completo
- Os resultados aparecem centralizados na interface.

## 🔧 Explicação do Código
### Estrutura principal:
- **Interface Gráfica:** Criada com `Tkinter`, com um campo de entrada (`Entry`) e uma área de texto (`Text`) para exibir os resultados.
- **Função `dv(ean)`:** Calcula o dígito verificador baseado no algoritmo EAN-13.
- **Função `checa(ean)`:** Ajusta o código EAN-13 antes de calcular o dígito verificador.
- **Função `init(ean)`:** Controla a exibição dos resultados na interface.

## 🖥️ Exemplo de Uso
### Entrada:
```
789123456789
```
### Saída:
```
Dígito Verificador: 2
Ean: 7891234567892
```

## 📜 Licença
Este projeto é de código aberto e pode ser usado livremente.

---
Se tiver dúvidas ou sugestões, fique à vontade para contribuir! 😊

