# Transcriptor

Transcriptor é uma aplicação de transcrição de áudio desenvolvida em Python com uma interface gráfica (GUI). O programa permite a transcrição de arquivos de áudio em texto, convertendo o áudio para o formato `.wav`, processando-o para extrair a transcrição e, por fim, salvando o texto em um arquivo. A aplicação também oferece a funcionalidade de busca por palavras-chave dentro da transcrição gerada.

## Funcionalidades

- **Conversão de Áudio:** Converte automaticamente arquivos de áudio em diferentes formatos (.mp3, .ogg, .flac, .wav) para o formato `.wav`.
- **Transcrição:** Utiliza o modelo Vosk para realizar a transcrição do áudio, suportando múltiplos canais e convertendo-os para mono se necessário.
- **Progresso em Tempo Real:** Exibe uma barra de progresso durante o processo de transcrição.
- **Armazenamento em Cache:** O texto transcrito é armazenado em cache e pode ser salvo em um arquivo de texto.
- **Busca por Palavra-Chave:** Permite buscar palavras específicas na transcrição e fornece o timestamp aproximado de onde cada palavra foi mencionada no áudio.
- **Interface Gráfica:** Interface amigável construída com `tkinter`, tornando a ferramenta acessível a usuários com pouca experiência em programação.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python:
  - `pydub`
  - `tkinter`
  - `vosk`
  - `wave`
  - `re`
  - `json`
  - `os`
  - `threading`
  - `datetime`
  - `tkinter.ttk`

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/euandros/transcriptor.git
   cd transcriptor-vansor

2. **Baixe o modelo vosk:**

   ```bash
   mkdir -p vosk-model
   cd vosk-model
   wget https://alphacephei.com/vosk/models/vosk-model-small-pt-0.3.zip
   unzip vosk-model-small-pt-0.3.zip
   
3. **Atualize o caminho do modelo:**

   ```bash
   model_path = "/caminho/para/vosk-model"  

## Uso

1. **Executar a aplicação:**
   
   ```bash
   python transcriptor_vansor.py

![image](https://github.com/user-attachments/assets/4dfa4b13-f4a6-4918-998c-9c182d9a579b)

2. **Selecionar o arquivo de áudio:**

Clique no botão "Procurar" e selecione o arquivo de áudio que deseja transcrever.

![image](https://github.com/user-attachments/assets/b6b0a625-fcfb-4ecc-8705-7a2ab1539ef3)

3. **Transcrever o áudio:**

Clique em "Transcrever". A barra de progresso indicará o andamento da transcrição.

![image](https://github.com/user-attachments/assets/b59fd6a7-3c83-4d77-9f55-3c7859488238)

Ao fim da transcrição, caso bem sucedida, uma mensagem será exibida na área de log da interface.

![image](https://github.com/user-attachments/assets/ad46783d-8e95-45c4-934a-7b544f2d50b0)
  
4. **Salvar a transcrição:**

Clique em "Salvar" para armazenar o texto transcrito em um arquivo .txt.

![image](https://github.com/user-attachments/assets/fab09b4b-ac38-4bf1-a0e0-3aa8b2a657ad)

5. **Buscar por palavra-chave:**

Insira uma palavra-chave no campo apropriado e clique em "Buscar" para localizar a palavra no texto transcrito, juntamente com o tempo aproximado em que ela foi mencionada no áudio.

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a MIT License.
