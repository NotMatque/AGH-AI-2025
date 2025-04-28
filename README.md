# Rozpoznawanie i zliczanie pojazdów w celu analizy zatłoczenia na drodze
## Kluczowe informacje
### Zamysł na projekt
Końcowym celem tego projektu jest stworzenie modelu AI, który na podstawie filmu - nagrania z ulicy, określić ilość pojazów która się po niej poruszała.

Projekt stworzony w ramach kursu na uczelni **nie musi** być jedynie na zaliczenie ;P
### Wykorzystane narzędzia
#### 1. OpenCV
- [Dokumentacja](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
- [Kurs na opencv.org](https://opencv.org/university/free-opencv-course/?utm_source=opcv&utm_medium=menu&utm_campaign=obc) <- to jest ciekawe
- [GeeksForGeeks](https://www.geeksforgeeks.org/opencv-python-tutorial/)
#### 2. YOLO (You only look once)
- [Opis v3](https://pjreddie.com/darknet/yolo/)
- [Link do GitHuba Ultralytics](https://github.com/ultralytics/ultralytics)
#### 3. ChatGPT
- [Najlepszy i najgorszy współpracownik w historii](https://chatgpt.com/)
### Dane
- **Zestaw 1**: [car-detection-and-tracking-dataset](https://www.kaggle.com/datasets/amitkumargurjar/car-detection-and-tracking-dataset)\
**Cechy**:\
**+** Prosty, szybki\
**-** Mały 399 zdjęć

- **Zestaw 2**: [car-detection-dataset](https://www.kaggle.com/datasets/seyeon040768/car-detection-dataset/data)\
**Cechy**:\
**+** Duży (16k zdjęć), na każdym zdjęciu dokładnie widać pojazd\
**-** Brak pustej przestrzeni, na każdym zdjęciu znajduje się pojaz, zdjęcia pozowane -> nie z drogi

- Zestaw 3: [car-detection](https://www.kaggle.com/datasets/abdallahwagih/cars-detection)\
**Cechy**:\
**+** Zróżnicowane zdjęcia, pojazdy w prawdziwym życiu\
**-** Mały (126 zdjęć), różne klasy (nie tylko samochody)

### Szkolenie modelu AI
Wybrany model był szkolony na podstawie konfiguracji `yolov8n.yaml` stworzonej przez _Ultralytics_. Dokładne dodefiniowanie naszego modelu znajduje się w pliku [dataset.yaml](dataset.yaml).

### Pozostałe linki
- [Jak nazywać commity](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)
- [Jak byś ocenił(a) stan projektu?](https://www.youtube.com/watch?v=iMmItLCZXv8)
## Kamienie milowe
### 1. **Określenie tematu i celu projektu, analiza wymagań**
- **Opis:** Zdefiniowanie celu projektu, zakresu, oraz wymaganych zasobów do
wdrożenia AI. Określenie problemu, który ma zostać rozwiązany przy użyciu
sztucznej inteligencji oraz zebranie wymagań (np. wydajność, skalowalność,
bezpieczeństwo).
- **Oczekiwany wynik:** Jasno określony cel projektu, dokumentacja wymagań.
### 2. **Zbiór danych i ich przygotowanie**
- **Opis:** Zbieranie, czyszczenie i wstępna analiza danych, które będą wykorzystane
do treningu modeli AI. Może to obejmować pozyskanie danych z różnych źródeł,
normalizację, usuwanie brakujących lub błędnych danych oraz ich
transformację.
- **Oczekiwany wynik:** Przygotowany zestaw danych, gotowy do wykorzystania w
procesie uczenia maszynowego.
### 3. **Wybór i implementacja modelu AI**
- **Opis:** Wybór odpowiedniego algorytmu AI oraz implementacja modelu. Może to
obejmować prototypowanie różnych podejść i testowanie ich wydajności na
przygotowanych danych.
- **Oczekiwany wynik:** Zbudowany i przetestowany model AI, gotowy do oceny
### 4. **Ocena wyników modelu i optymalizacja**
- **Opis:** Dobór metryk. Testowanie modelu na zestawie danych testowych w celu
oceny jego dokładności, wydajności, oraz ogólnych wyników. Optymalizacja
modelu np. przez dostosowanie hiperparametrów, selekcję cech lub poprawę
jakości danych.
- **Oczekiwany wynik:** Zoptymalizowany model AI osiągający wymagane parametry
wydajności.
### 5. **Wdrożenie modelu i monitorowanie**
- **Opis:** Przeniesienie modelu do środowiska produkcyjnego i integracja z
otoczeniem. Ustalenie mechanizmów monitorowania.
- **Oczekiwany wynik:** Zaimplementowany i uruchomiony system z AI w
konkretnym środowisku.
### Dodatkowe informacje dotyczące kamieni milowych
- Kamienie milowe są oceniane 0-1, na zajęciach należy zaprezentować raport z
realizacji kamienia milowego, te raporty złączone ze sobą na koniec będą stanowiły
raport z projektu.
- Ocena z projektu wynika z sumy punktów z kamieni milowych. Konieczne jest również
uzyskanie pozytywnej oceny z prezentacji projektu (kolokwium ustnego). Ocena
końcowa z ćwiczeń jest średnią z ocen za realizację projektu (jedna ocena wynikająca z
ocen za kamienie milowe) oraz jego prezentacji.
- Prezentacja ma być zwięzłym podsumowaniem projektu
- Minimum **50%** obecności na zajęciach jest warunkiem koniecznym do zaliczenia
ćwiczeń.
- Możliwe jest **wcześniejsze** oddanie projektu.
- Opóźnienie oddania kamienia milowego powoduje obniżenie oceny stosownie do
opóźnienia. 