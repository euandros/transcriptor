# Transcriptor

![Segmento](https://img.shields.io/badge/Segmento_:-Inteligência_de_Áudio-darkblue?style=flat-square) 
![Fase](https://img.shields.io/badge/Fase_:-Experimental-lightgreen?style=flat-square) 
![Tecnologias](https://img.shields.io/badge/Tecnologias_:-Pydub,_Tkinter,_Vosk-lightgreen?style=flat-square) 
![Versão](https://img.shields.io/badge/versão_:-1.0-darkgreen?style=flat-square)

<p style='text-align: justify;'> Transcriptor é uma aplicação gráfica em Python que permite a transcrição offline de arquivos de áudio para texto utilizando o modelo de reconhecimento de fala Vosk. A aplicação suporta diversos formatos de áudio, como MP3, OGG, FLAC e WAV, e permite salvar a transcrição resultante em um arquivo de texto.</p>

## Índice

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Licença](#licença)

## Recursos

- **Suporte a vários formatos de áudio**: MP3, OGG, FLAC, WAV.
- **Transcrição offline** utilizando o modelo Vosk.
- **Interface gráfica** amigável e intuitiva construída com Tkinter.
- **Conversão automática** de arquivos de áudio estéreo para mono, se necessário.
- **Barra de progresso** para acompanhar o andamento da transcrição.
- **Mensagens de log** para acompanhar o status do processo.
- **Salvamento da transcrição** em um arquivo de texto.

## Instalação

### Pré-requisitos

1. **Python 3.7 ou superior** deve estar instalado no sistema.

2. **Dependências Python**: As dependências listadas na seção [Dependências](#dependências) podem ser instaladas usando o `pip`.

3. **Modelo Vosk**: Baixe o modelo de linguagem Vosk para português (ou outro idioma de sua escolha) e extraia o conteúdo para o diretório `models` dentro do projeto.

   ```bash
   mkdir -p models
   cd models
   wget https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip
   unzip vosk-model-small-pt-0.3.zip

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/euandros/transcriptor.git
   cd transcriptor

2. **Crie um abiente virtual:**

   ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate  # Windows

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
 
4. **Atualize o caminho do modelo:**

   ```bash
   model_path = "/caminho/para/vosk-model"  

## Uso

1. **Executar a aplicação:**
   
   ```bash
   python transcriptor.py

![image](https://github.com/user-attachments/assets/bb2d9bfa-f8fe-4ef8-867c-f08caeaf4f07)

<p style='text-align: justify;'> Na interface gráfica que será aberta:</p>

<p style='text-align: justify;'> Clique em "Procurar" para selecionar o arquivo de áudio que deseja transcrever.</p>

![image](https://github.com/user-attachments/assets/b6b0a625-fcfb-4ecc-8705-7a2ab1539ef3)

<p style='text-align: justify;'> Após a conclusão, você pode salvar a transcrição em um arquivo de texto clicando em "Salvar".</p>

2. **Transcrever o áudio:**

<p style='text-align: justify;'>Clique em "Transcrever" para iniciar o processo de transcrição. A barra de progresso mostrará o andamento da transcrição.</p>

![image](https://github.com/user-attachments/assets/99579c73-5b7e-4be5-9fd1-d4d6f6869328)

<p style='text-align: justify;'> Ao fim da transcrição, caso bem sucedida, uma mensagem será exibida na área de log da interface.</p>

![image](https://github.com/user-attachments/assets/75867c43-2d02-4d40-b6ae-e75853686907)
  
4. **Salvar a transcrição:**

<p style='text-align: justify;'> Clique em "Salvar" para armazenar o texto transcrito em um arquivo .txt.</p>

![image](https://github.com/user-attachments/assets/fab09b4b-ac38-4bf1-a0e0-3aa8b2a657ad)

## Contribuição

<p style='text-align: justify;'> Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.</p>

## Licença

<p style='text-align: justify;'> Este projeto é licenciado sob a MIT License.</p>
