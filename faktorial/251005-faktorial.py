import numpy as np
import sympy as sp
import os

def tulis(soal, pg, kunci):
  with open('soal.tex', 'a') as f:
    f.write(fr'\item {soal}' + '\n')
    f.write(r'  \begin{enumerate}' + '\n')
    for abc in pg:
      f.write(fr'   \item {abc}' + '\n')
    f.write(r'  \end{enumerate}' + '\n')

  with open('kunci.tex', 'a') as f:
    f.write(r'\item ' + 'ABCDE'[kunci] + '\n')
  
  with open('kunci_kode.txt', 'a') as f:
    f.write(f'{kunci},')

def awal(bab, ke=1):
  kode = np.random.randint(21,30) * 30 + ke
  
  with open('kunci_kode.txt', 'a') as f:
    f.write(f'{kode}:[')

  with open('soal.tex', 'w') as f:
    f.write(r'''\documentclass[a4paper,12pt]{article}
\usepackage{hyperref}
\usepackage{mathptmx}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage[margin=1in, includehead]{geometry}
\usepackage{fancyhdr}
\usepackage{multicol}
\begin{document}
\pagestyle{fancy}
\begin{multicols}{2}
''')
    
    f.write(fr'\section*{{ {bab} }}' + '\n')
    f.write(fr'\section{{ kode: {kode} }}' + '\n')
    f.write(r'\begin{enumerate}' + '\n')
  
  with open('kunci.tex', 'w') as f:
    f.write(r'''\documentclass[a4paper,12pt]{article}
\usepackage{hyperref}
\usepackage{mathptmx}
\usepackage{amsmath}
\usepackage{amsfonts}
\begin{document}
''')

    f.write(fr'\section*{{ {bab} }}' + '\n')
    f.write(fr'\section{{ kode soal: {kode} }}' + '\n')
    f.write(r'\begin{enumerate}' + '\n')

def akhir():
  with open('kunci_kode.txt', 'a') as f:
    f.write(']\n')

  with open('soal.tex', 'a') as f:
    f.write(r'\end{enumerate}' + '\n')
    f.write(r'\end{multicols}' + '\n')
    f.write(r'\end{document}')
  
  with open('kunci.tex', 'a') as f:
    f.write(r'\end{enumerate}' + '\n')
    f.write(r'\end{document}')
  
  os.system('pdflatex soal.tex')
  os.system('pdflatex kunci.tex')
  # ~ os.system('xdg-open soal.pdf')
  # ~ os.system('xdg-open kunci.pdf')

def pg_sekitar(jawaban):
  kunci = np.random.randint(0,5)
  return [ f'${jawaban + i}$' for i in range(-kunci, 5 - kunci) ], kunci



os.system('rm -f kunci_kode.txt')
bab = '251005-faktorial-permutasi'
def s1():
  a = np.random.randint(4, 8)
  soal = fr'${a}! = ...$'
  jawab = sp.factorial(a)
  # ~ pg, kunci = pg_sekitar(jawab)
  kunci = np.random.randint(0,5)
  pg = [ f'${sp.factorial(a + i)}$' for i in range(-kunci, 5 - kunci) ]
  tulis(soal, pg, kunci)

def s2():
  a = np.random.randint(5, 8)
  b = np.random.randint(2, a)
  soal = fr'$\dfrac{{ {a}! }}{{ {b}! }} = ...$'
  jawab = sp.factorial(a)/sp.factorial(b)
  pg, kunci = pg_sekitar(jawab)
  tulis(soal, pg, kunci)

def s3():
  a = np.random.randint(5, 8)
  b = np.random.randint(2, a - 1)
  c = np.random.randint(b + 1, a)
  
  if np.random.randint(0,2) == 0:
    fc = -sp.factorial(c)
    tanda = '-'
  else:
    fc = sp.factorial(c)
    tanda = '+'
  
  soal = fr'$\dfrac{{ {a}! }}{{ {b}! }} {tanda} {c}!= ...$'
  jawab = sp.factorial(a)/sp.factorial(b) + fc
  pg, kunci = pg_sekitar(jawab)
  tulis(soal, pg, kunci)
  
def s4():
  a = np.random.randint(3, 6)
  b = a - 1
  p = np.random.randint(5, 10)
  q = np.random.randint(2, 4) * p
  
  
  soal = fr'${p}\times {a}! + {q}\times {b}!= ...$'
  jawab = p * sp.factorial(a) + q * sp.factorial(b)
  pg, kunci = pg_sekitar(jawab)
  tulis(soal, pg, kunci)
  
def s5():
  a = np.random.randint(6, 11)
  b = a - 1
  c = b - 1
  d = c - 1
  
  soal = fr'$\dfrac{{ {a}! }}{{ {c}! }} + \dfrac{{ {b}! }}{{ {d}! }}= ...$'
  jawab = sp.factorial(a)/sp.factorial(c) + sp.factorial(b)/sp.factorial(d)
  pg, kunci = pg_sekitar(jawab)
  tulis(soal, pg, kunci)
  
  
def s6():
  a = np.random.randint(15, 19)
  b = a - 2
  c = np.random.randint(11, a - 2)
  d = c - 2
  
  soal = fr'$\dfrac{{ {a}! }}{{ {b}! }} - \dfrac{{ {c}! }}{{ {d}! }}= ...$'
  jawab = sp.factorial(a)/sp.factorial(b) - sp.factorial(c)/sp.factorial(d)
  pg, kunci = pg_sekitar(jawab)
  tulis(soal, pg, kunci)
  
def s7():
  pil = ['90', '144', '252', sp.latex(1+sp.Rational(1,2)), sp.latex(sp.Rational(1,2))]
  a = np.random.choice(pil)
  soal = fr'Dari pilihan berikut ini yang bernilai ${a}$ adalah ... .'
  pg = [r'$\dfrac{6!\times 7!}{8!}$', r'$\dfrac{9!\times 2!}{7!}$', r'$\dfrac{7!\times 3!}{5!}$', r'$\dfrac{15!\times 4!}{16!}$', r'$\dfrac{11!\times 3!}{12!}$' ]
  kunci = pil.index(a)
  tulis(soal, pg, kunci)
  
def s8():
  a = np.random.randint(51, 70)
  soal = f'Luas persegi panjang yang berukuran panjang {a} cm dan lebar {a - 1} cm dalam notasi faktorial adalah ... cm${{}}^2$.'
  kunci = np.random.randint(0, 5)
  pg = [ fr'$\dfrac{{ {a + i}! }}{{ {a + i - 2}! }}$' for i in range(-kunci, 5 - kunci) ]
  tulis(soal, pg, kunci)
  
def s9():
  a = np.random.randint(51, 70)
  b = np.random.randint(11, 20)
  soal = f'Diketahui kubus 1 berukuran panjang {a} cm, lebar {a - 2} cm, tinggi {a - 1} cm. Kubus 2 berukuran panjang {b - 1} cm, lebar {b - 2} cm, dan tinggi {b} cm. Selisih volume kedua kubus tersebut dalam notasi faktorial adalah ... cm${{}}^3$.'
  kunci = np.random.randint(0, 5)
  pg = [ fr'$\dfrac{{ {a + i}! }}{{ {a + i - 3}! }} - \dfrac{{ {b + i}! }}{{ {b + i - 3}! }}$' for i in range(-kunci, 5 - kunci) ]
  tulis(soal, pg, kunci)
  
  
def s10():
  a = np.random.randint(4, 8)
  
  soal = f'Dalam berapa cara {a} anak dapat disusun sebaris?'
  jawab = sp.factorial(a)
  pg, kunci = pg_sekitar(jawab)
  tulis(soal, pg, kunci)

def s11():
  a = np.random.randint(4, 8)
  b = np.random.randint(4, 8)
  
  soal = f'Dalam berapa cara {a} gajah dan {b} tikus dapat disusun sebaris?'
  jawab = a + b
  kunci = np.random.randint(0, 5)
  pg = [ f'${jawab + i}!$' for i in range(-kunci, 5 - kunci) ]
  tulis(soal, pg, kunci)

def s12():
  a = np.random.randint(10, 15)
  b = np.random.randint(4, 8)
  parkir = sp.factorial(a)
  soal = f'Sembilan motor dan $x$ sepeda dapat diparkir sebaris sebanyak {parkir} cara. Dalam berapa cara {b} motor dan $x + {9-b}$ sepeda dapat diparkir sebaris?'
  jawab = a
  # ~ pg, kunci = pg_sekitar(jawab)
  kunci = np.random.randint(0, 5)
  pg = [ f'${sp.factorial(jawab + i)}$' for i in range(-kunci, 5 - kunci) ]
  tulis(soal, pg, kunci)

def s13():
  a = np.random.randint(17, 25)
  naik = (a + 1) * (a + 2)
  soal = f'Sebanyak $n$ siswa dapat disusun sebaris dalam $x$ cara. Dengan menambahkan dua siswa lagi, banyaknya cara menyusun menjadi {naik} kali lipat. Nilai $n$ adalah ... .'
  jawab = a
  pg, kunci = pg_sekitar(jawab)
  tulis(soal, pg, kunci)

def s14():
  a = np.random.randint(4, 12)
  soal = f'Seorang ibu memiliki {a} anak. Beliau menyusun {a+1} kursi sebaris dan duduk di tengah. Jika anak termuda duduk persis di samping kanan Beliau maka banyaknya cara menyusun anak yang tersisa adalah ... .'
  jawab = a - 1
  kunci = np.random.randint(0, 5)
  pg = [f'${sp.factorial(jawab + i)}$' for i in range(-kunci, 5 - kunci)]
  tulis(soal, pg, kunci)

def s15():
  a = np.random.randint(3, 6)
  x = np.random.randint(1, 5)
  y = np.random.randint(5,10)
  angka = [ x for i in range(a) ]
  for i in range(6 - a):
    angka.append(y)
  soal = f'Ada berapa banyak cara bilangan yang terdiri dari enam digit dapat dibuat dari angka-angka {angka}?'
  jawab = sp.factorial(6)/(sp.factorial(a)*sp.factorial(6 - a))
  kunci = np.random.randint(0, 5)
  pg = [f'${jawab + i}$' for i in range(-kunci, 5 - kunci)]
  tulis(soal, pg, kunci)

os.system('mkdir -p tex_soal')
os.system('mkdir -p tex_kunci')
os.system('mkdir -p pdf_soal')
os.system('mkdir -p pdf_kunci')
for i in range(30):
  awal(bab, ke=i)
  s1()
  s2()
  s3()
  s4()
  s5()
  s6()
  s7()
  s8()
  s9()
  s10()
  s11()
  s12()
  s13()
  s14()
  s15()
  akhir()
  os.system(f'cp soal.tex tex_soal/soal_{i}.tex')
  os.system(f'cp kunci.tex tex_kunci/kunci_{i}.tex')
  os.system(f'cp soal.pdf pdf_soal/soal_{i}.pdf')
  os.system(f'cp kunci.pdf pdf_kunci/kunci_{i}.pdf')

os.system(f'gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=pdf_soal/{bab}_soal_jadi_satu.pdf -dBATCH pdf_soal/soal*')
os.system(f'gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=pdf_kunci/{bab}_kunci_jadi_satu.pdf -dBATCH pdf_kunci/kunci*')
