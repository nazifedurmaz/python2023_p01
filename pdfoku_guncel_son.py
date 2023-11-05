import os #işletim sistemi etkileşimi için dizin yolları vs.
import pdfplumber # PDF okumak için
from fpdf import FPDF  # PDF oluşturmak için.

def menu():
    print("Menü:")
    print("1- PDF Dosya İçerik (Başlıklar) Oku")
    print("2- PDF (Başlıkları) Kaydet")
    print("3- Çıkış Yap")

def extract_titles_from_pdf(pdf_path):
    titles = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            titles.extend(text.split('\n'))

    return titles

def save_titles_to_pdf(titles):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for title in titles:
        pdf.cell(200, 10, txt=title, ln=True)

    pdf.output("newfile.pdf")

while True:
    menu()
    choice = input("Seçiminizi girin (1/2/3): ")

    if choice == "1":
        print("PDF Dosyalarını Oku seçildi:")
        pdf_folder = "pdfler"
        pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
        titles = []
        for pdf_file in pdf_files:
            titles.extend(extract_titles_from_pdf(pdf_file))
        for title in titles:
            print(title)
    elif choice == "2":
        print("PDF Dosyalarını Kaydet seçildi:")
        pdf_folder = "pdfler"
        pdf_files = [os.path.join(pdf_folder, f) for f in os.listdir(pdf_folder) if f.endswith(".pdf")]
        titles = []
        for pdf_file in pdf_files:
            titles.extend(extract_titles_from_pdf(pdf_file))
        save_titles_to_pdf(titles)
        print("Başlıklar yeni PDF dosyasına kaydedildi: newfile.pdf")
    elif choice == "3":
        print("Çıkış Yapılıyor.")
        break
    else:
        print("Geçersiz seçenek! Lütfen 1, 2 veya 3 girin.")
