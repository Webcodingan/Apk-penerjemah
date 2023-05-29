from googletrans import Translator

translator = Translator()

text = input("Masukkan teksnya: ")
bahasa = input("translate ke bahasa? (ja, ko, en, id, su, zh-cn): ")
hasil = translator.translate(text, dest=bahasa)

print("Dari ", hasil.src, " : ", text)
print("Ke ", hasil.dest, " : ", hasil.text)
print("Pronunisasi : ", hasil.pronunciation)
