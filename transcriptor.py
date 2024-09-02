import tkinter as tk
from tkinter import filedialog, ttk
import threading
import wave
import vosk
import json
import os
import tempfile
from pydub import AudioSegment

class TranscriptorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Transcriptor de Áudio")
        master.geometry("400x350")

        self.audio_file_label = tk.Label(master, text="Selecione o arquivo de áudio:")
        self.audio_file_label.pack()

        self.audio_file_entry = tk.Entry(master, width=40)
        self.audio_file_entry.pack()

        button_frame = tk.Frame(master)
        button_frame.pack(pady=5)

        self.browse_button = tk.Button(button_frame, text="Procurar", command=self.browse_file)
        self.browse_button.pack(side=tk.LEFT, padx=5)

        self.transcribe_button = tk.Button(button_frame, text="Transcrever", command=self.transcribe_audio)
        self.transcribe_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(button_frame, text="Salvar", command=self.save_file, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.log_text = tk.Text(master, height=5, width=40, state=tk.DISABLED)
        self.log_text.pack()

        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=(30, 0))

        self.footer_label = tk.Label(master, text="Desenvolvimento por Evandro Santos (VanSor) @ 2024", font=("Arial", 10))
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

        self.temp_file = None  # Armazena o caminho do arquivo temporário

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", ".mp3 .ogg .flac .wav")])
        self.audio_file_entry.delete(0, tk.END)
        self.audio_file_entry.insert(0, file_path)

    def transcribe_audio(self):
        audio_file = self.audio_file_entry.get()

        if audio_file:
            self.log_message("Iniciando a transcrição...")
            self.progress["value"] = 0
            thread = threading.Thread(target=self.transcribe_audio_thread, args=(audio_file,))
            thread.start()
        else:
            self.log_message("Por favor, selecione um arquivo de áudio primeiro.")

    def transcribe_audio_thread(self, audio_file):
        try:
            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete('1.0', tk.END)
            self.log_text.config(state=tk.DISABLED)

            self.log_message(f"Carregando o arquivo de áudio: {audio_file}")
            audio_segment = AudioSegment.from_file(audio_file)
            self.log_message(f"Formato do áudio: {audio_segment.sample_width * 8}-bit, {audio_segment.frame_rate}Hz, {audio_segment.channels} canal(is)")

            if audio_segment.channels > 1:
                self.log_message("Convertendo o áudio para mono...")
                audio_segment = audio_segment.set_channels(1)

            wav_file = "temp.wav"
            self.log_message(f"Exportando áudio para {wav_file}...")
            audio_segment.export(wav_file, format="wav")

            self.log_message("Carregando o modelo Vosk...")
            model_path = "/caminho/para/diretório/models/"
            model = vosk.Model(model_path)
            self.log_message(f"Modelo carregado de: {model_path}")

            with wave.open(wav_file, "rb") as wf:
                recognizer = vosk.KaldiRecognizer(model, wf.getframerate())
                total_frames = wf.getnframes()
                frames_processed = 0

                self.log_message("Iniciando a leitura dos frames...")

                # Cria um arquivo temporário
                temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8')
                self.temp_file = temp_file.name

                # Acumula o texto da transcrição em uma variável
                transcription_text = ""

                while True:
                    data = wf.readframes(4000)
                    if len(data) == 0:
                        break

                    if recognizer.AcceptWaveform(data):
                        result = json.loads(recognizer.Result())

                        if "text" in result:
                            transcription_text += result["text"] + " "
                        recognizer.Reset()  # Limpa o buffer do recognizer

                    frames_processed += 4000
                    self.update_progress(frames_processed, total_frames)

                final_result = json.loads(recognizer.FinalResult())
                if "text" in final_result:
                    transcription_text += final_result["text"] + " "

                # Escreve a transcrição completa no arquivo temporário
                temp_file.write(transcription_text)
                temp_file.flush()
                temp_file.close()

            # Limpa o log e exibe apenas a mensagem de conclusão
            self.log_text.config(state=tk.NORMAL)
            self.log_text.delete('1.0', tk.END)
            self.log_message("Transcrição concluída!")
            self.log_text.config(state=tk.DISABLED)

            if os.path.exists(self.temp_file):
                self.save_button.config(state=tk.NORMAL)
            else:
                self.log_message("A transcrição não gerou nenhum texto.")

        except Exception as e:
            self.log_message(f"Erro na transcrição: {e}")

        finally:
            if os.path.exists(wav_file):
                os.remove(wav_file)

    def update_progress(self, frames_processed, total_frames):
        progress_value = (frames_processed / total_frames) * 100
        self.master.after(0, lambda: self.progress.config(value=progress_value))

    def log_message(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def save_file(self):
        if self.temp_file and os.path.exists(self.temp_file):
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if save_path:
                try:
                    with open(save_path, "w") as file:
                        with open(self.temp_file, "r") as temp_file:
                            file.write(temp_file.read())

                    # Limpa o log e exibe apenas a mensagem de salvamento
                    self.log_text.config(state=tk.NORMAL)
                    self.log_text.delete('1.0', tk.END)
                    self.log_message(f"Arquivo salvo em: {save_path}")
                    self.log_text.config(state=tk.DISABLED)
                except Exception as e:
                    self.log_message(f"Erro ao salvar o arquivo: {e}")
                finally:
                    os.remove(self.temp_file)
        else:
            self.log_message("Nenhum texto para salvar. Por favor, transcreva o áudio primeiro.")

if __name__ == "__main__":
    root = tk.Tk()
    transcriptor_gui = TranscriptorGUI(root)
    root.mainloop()
