import speech_recognition

rec = speech_recognition.Recognizer()

file = 'audio/test4.wav'

audio_file = speech_recognition.AudioFile(file)


with audio_file as source:
    rec.adjust_for_ambient_noise(source, duration=0.2)
    audio = rec.record(source)

result = rec.recognize_google(audio, language='ru')

with open(f'audio/test{file[-5]}.txt', mode='w', encoding='utf-8') as file:
   file.write("Расшифрованный текст:")
   file.write("\n")
   file.write(result)
   print("Готово!")
