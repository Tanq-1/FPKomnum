# **Final Project Komputasi Numerik**

## **Soal yang kami dapatkan:**
![Soal](https://github.com/user-attachments/assets/d8ea5df3-c990-445f-bf13-113d4acacbee)

---

## **Penjelasan Singkat:**
Pada soal ini, kami diminta untuk membuat sebuah program dengan bahasa python untuk mencari akar dari persamaan di soal dengan
metode **Newton-Raphson**. Iterasi dimulai dari X<sub>0</sub> hingga X<sub>t</sub>. 

---

## **Penyelesaian:**
### 1. Definisikan **`F(x)`** di dalam program:
```python
import math

def F(x):
    return x**3 + 6 * x**2 - 19*x -84
```
Di sini kami mendefinisikan fungsi F(x) dari soal ke dalam program.


### 2. Definisikan **`Df(x)`** sebagai turunan dari F(x):
```python
# kode sebelumnya
def Df(x):
    return 3 * x**2 + 12*x - 19
```
Pada bagian ini, kami medefinisikan Df(x) yang merupakan turunan dari F(x) agar dapat digunakan untuk mencari akar persamaan.


### 3. Definisikan **`x`** dan **`xt`** sebagai nilai X<sub>0</sub> dan X<sub>t</sub>
```python
# kode sebelumnya
x = -4 #Ini nilai X0
xt = -3 #Ini nilai x sebenarnya
```
Kami mendefinisikan x dan xt sesuai dengan nilai-nilai mereka pada soal yaitu -4 dan 3.


### 4. Melakukan pencarian dari akar x mulai dari X<sub>0</sub> hingga mencapai X<sub>t</sub>
```python
# kode sebelumnya 
i = 1
while x != xt:
    x = x - F(x) / Df(x)
    print("Iterasi ke -",i,":","\Nilai x: ",x,"\n")
    i += 1
```
- Kami membuat variabel i untuk menandai urutan dari iterasi nanti
- Kami membuat sebuah `while` loop dengan kondisi di mana jika x masih belum sama dengan xt, maka loop tersebut akan berjalan terus hingga mendapatkan xt.
- Di dalam loop (pada baris pertama loop), kami menggunakan rumus **Newton-Rhapson** untuk mwncari akar dari persamaan pada soal yaitu $x_i = x_{i-1} - \frac{f(x)}{f'(x)}$.
- Baris kedua dari loop berfungsi untuk mencetak semua nilai iterasinya.
- Baris ketiga dari loop melakukan inkremen terhadap nilai i setiap iterasi
Jika kodenya dijalankan, maka outputnya akan seperti ini:
```
Iterasi ke - 1 : 
Nilai x:  -2.736842105263158 

Iterasi ke - 2 : 
Nilai x:  -2.9941674898365407 

Iterasi ke - 3 : 
Nilai x:  -2.9999963738865816 

Iterasi ke - 4 : 
Nilai x:  -2.9999999999985913 

Iterasi ke - 5 : 
Nilai x:  -3.0000000000000004 

Iterasi ke - 6 : 
Nilai x:  -3.0 

```
### 5. Membuat fungsi **`Flounder(x)`** (Float Rounder) untuk melakukan pembulatan
```python
# kode sebelumnya
def Df(x):
    return 3 * x**2 + 12*x - 19
def Flounder(x):
    if ((x*1000) % 10 >=5):
        return (((x*100)-((x*100)%1))/100 + 0.01)
    else :
        return (((x*100)-((x*100)%1))/100)
x = -4 #Ini nilai X0
# kode sebelumnya
```
- Kami membuat fungsi Flounder untuk melakukan pembulatan terhadap nilai x
- Angka akan dibulatkan hingga dua angka di belakang koma.
- Jika angka yang berada di tiga angka di belakang koma lebih besar atau sama dengan 5, maka dibulatkan ke atas.
- Jika tidak, maka akan dibulatkan ke bawah.
- Cara kerja dari fungsi ini adalah dia akan mengalikan x dengan 1000 sehingga angka yang berada pada tiga angka di belakang koma menjadi satuan dari x
- Nilai x akan dimodulus dengan 10 sehingga kita mendapatkan nilai satuannya.
- Jika satuan tersebut lebih besar atau sama dengan 5, maka x akan dibulatkan ke atas (nilai yang berada dua angka di belakang koma ditambahkan satu) dan nilai-nilai yang berada di tiga atau lebih angka di belakang koma dihilangkan.
- Jika tidak, maka x akan dibulatkan ke bawah (sama seperti pembulatan ke atas, namun tidak ditambahkan satu)
- Pendekatan ini kami gunakan karena operasi modulus dengan nilai kecil seperti 0.001 terkadang tidak akurat

### 6. Memperbarui **`while`** loop untuk menggunakan **`Flounder(x)`**
```python
# kode sebelumnya
while x != xt:
    x = x - F(x) / Df(x)
    print("Iterasi ke -",i,":","\nTanpa pembulatan: ",x,"\nDengan pembulatan: ",Flounder(x),"\n")
    i += 1
```
- Pada bagian ini, kami memperbarui **`whilw`** loop untuk menggunakan **`Flounder(x)`**
- Karena kami tidak mengetahui apakah nilai x harus dibulatkan atau tidak, kami memasukkan kedua nilai x yaitu sebelum dan setelah pembulatan
Berikut ini adalah output dari kodenya setelah diperbarui dan dijalankan:
```
Iterasi ke - 1 : 
Tanpa pembulatan:  -2.736842105263158 
Dengan pembulatan:  -2.74 

Iterasi ke - 2 : 
Tanpa pembulatan:  -2.9941674898365407 
Dengan pembulatan:  -2.99 

Iterasi ke - 3 : 
Tanpa pembulatan:  -2.9999963738865816 
Dengan pembulatan:  -3.0 

Iterasi ke - 4 : 
Tanpa pembulatan:  -2.9999999999985913 
Dengan pembulatan:  -3.0 

Iterasi ke - 5 : 
Tanpa pembulatan:  -3.0000000000000004 
Dengan pembulatan:  -3.0 

Iterasi ke - 6 : 
Tanpa pembulatan:  -3.0 
Dengan pembulatan:  -3.0 

```

---

## Kode Lengkap 
```python
import math

def F(x):
    return x**3 + 6 * x**2 - 19*x -84
def Df(x):
    return 3 * x**2 + 12*x - 19
def Flounder(x):
    if ((x*1000) % 10 >=5):
        return (((x*100)-((x*100)%1))/100 + 0.01)
    else :
        return (((x*100)-((x*100)%1))/100)
x = -4 #Ini nilai X0
xt = -3 #Ini nilai x sebenarnya
i = 1
while x != xt:
    x = x - F(x) / Df(x)
    print("Iterasi ke -",i,":","\nTanpa pembulatan: ",x,"\nDengan pembulatan: ",Flounder(x),"\n")
    i += 1
```

---
