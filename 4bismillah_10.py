import numpy as np
import sympy as sp
import os
from collections import Counter, defaultdict
import matplotlib.pyplot as plt

os.system('rm -f kunci_kode.txt')

def awal(ke=1):
	filename_soal='soal.tex'
	filename_kunci='kunci.tex'
	
	rhs = np.random.randint(11, 19)
	kodesoal = 30 * rhs + ke
	
	with open('template.tex', 'r') as f:
		with open(filename_soal, 'w') as g:
			g.write(f.read())
			g.write(fr'''
\section{{Kode soal: {kodesoal}}}''')
			g.write(r'''
\subsection{Pilihlah jawaban yang paling benar (A, B, C, D, atau E) pada lembar jawab yang tersedia.}
\begin{enumerate}
''')

		with open(filename_kunci, 'w') as h:
			h.write(r'''\documentclass{article}
\usepackage{mathptmx}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage[hidelinks]{hyperref}
\usepackage{bookmark}
\usepackage[a4paper,margin=1cm,footskip=.5cm]{geometry}
\renewcommand\thesubsection{\Alph{subsection}}

\begin{document}''')
			h.write(fr'''
\section{{Kode soal: {kodesoal}}}''')
			h.write(r'''
\subsection{PG}
\begin{enumerate}
''')
	with open('kunci_kode.txt', 'a') as j:
		j.write(f'{kodesoal}:[')

# ~ awal()




def tulis(teks_soal, pg_array, kunci):
	filename_soal = 'soal.tex'
	filename_kunci = 'kunci.tex'
	# tulis soal
	with open(filename_soal, 'a') as f:
		f.write(fr'''\item {teks_soal}''')
		
		# tulis pg
		f.write(r'''
	\begin{enumerate}''')
		for pg in pg_array:
			f.write(fr'''
	\item {pg}''')
		f.write(r'''
	\end{enumerate}
''')

	# tulis kunci
	with open(filename_kunci, 'a') as g:
		g.write(fr'''\item {'ABCDE'[kunci]}	
''')
	with open('kunci_kode.txt', 'a') as h:
		h.write(f'{kunci}, ')



def akhir():
	filename_soal='soal.tex'
	filename_kunci='kunci.tex'
	with open(filename_soal, 'a') as f:
		f.write(r'\end{enumerate}\end{document}')
	with open(filename_kunci, 'a') as f:
		f.write(r'\end{enumerate}\end{document}')
	with open('kunci_kode.txt', 'a') as f:
		f.write(']\n')
	os.system(f'pdflatex {filename_soal}')
	os.system(f'pdflatex {filename_kunci}')
	# ~ os.system(f'mv soal.pdf pdf_soal/soal_{i}.pdf')
	# ~ os.system(f'mv kunci.pdf pdf_kunci/kunci_{i}.pdf')

def tutup_pg():
	with open('soal.tex', 'a') as f:
		f.write(r'''\end{enumerate}
''')

	with open('kunci.tex', 'a') as f:
		f.write(r'''\end{enumerate}
''')


def uraian():
	with open('soal.tex', 'a') as s:
		s.write(r'''
\subsection{Uraian}
\begin{enumerate}
''')

	with open('kunci.tex', 'a') as k:
		k.write(r'''
\subsection{Uraian}
\begin{enumerate}
''')

def tulis_uraian(teks_soal, kunci):
	with open('soal.tex', 'a') as f:
		f.write(fr'''\item {teks_soal}
''')
	with open('kunci.tex', 'a') as f:
		f.write(fr'''\item {kunci}
''')



x, y, z, a, b, c = sp.symbols('x y z a b c')
bil = [ i for i in range(-9,10) if i != 0 ]




def s01():
	# ~ with sp.evaluate(False):
	a = np.random.randint(2,6)
	h = sp.Pow(a,-2) + sp.Pow(a,-1) + sp.Pow(a,0) + sp.Pow(a,1) + sp.Pow(a,2)
	j = sp.Pow(a,-2) - sp.Pow(a,-1) - sp.Pow(a,0) - sp.Pow(a,1) - sp.Pow(a,2)
	print(h)
	print(1/h)
	soal = fr'${a}^{{-2}} + {a}^{{-1}} + {a}^0 + {a}^1 + {a}^2 = ... .$'
	print(soal)
	jawab = h
	pg = [jawab]
	pg.append(1+h)
	pg.append(-j)
	pg.append(1-j)
	pg.append(1)
	pg.sort()
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	
	tulis(soal, pg1, kunci)
	
# ~ s01()
def s02():
	a = np.random.randint(2,6)
	b = np.random.randint(2,6)
	p = np.random.choice(bil)
	q = np.random.choice(bil)
	r = np.random.choice(bil)
	s = np.random.choice(bil)
	
	g = a * x**p * y**q * b * x**r * y **s
	h = a * x**p * y**q / (b * x**r * y **s)
	j = 1/h
	k = g/b
	l = g/(x**r)
	soal = fr'${sp.latex(a * x**p * y**q)}\times {sp.latex(b * x**r * y**s)}=... .$'
	print(soal)
	print(g)
	jawab = g
	pg = [jawab, h, j, k, l]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	
	tulis(soal, pg1, kunci)

def s03():
	p = np.random.randint(1,10)
	q = np.random.randint(1,10)
	r = np.random.randint(1,10)
	s = np.random.randint(1,10)
	
	z = np.random.randint(2,6)
	x = np.random.randint(1,4)*z
	y = np.random.randint(4,7)*z
	atas = x * a**p * b**q
	bawah = y * a**r * b**s
	soal = fr'$\dfrac{{ {sp.latex(atas)} }}{{ {sp.latex(bawah)} }}=... .$'
	
	jawab = atas/bawah
	pg = [jawab]
	pg.append(1/jawab)
	pg.append(jawab/z)
	pg.append(1/jawab/z)
	pg.append(jawab/(b**s))
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s04():
	atas = np.random.randint(101,999)
	g = atas/99
	soal = fr'Bilangan {np.floor(g*10**6)/10**6}... jika ditulis dalam bentuk $\dfrac{{a}}{{b}}$ dengan $a$ dan $b$ bilangan bulat adalah ... .'
	kunci = np.random.randint(0,5)
	pg = [ f'$\dfrac{{ {atas + i} }}{{99}}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s05():
	a = np.random.randint(2, 9)
	ganjil = [2*i+1 for i in range(4)]
	genap = [2*i for i in range(1,4)]
	p = np.random.choice(ganjil)
	q = np.random.choice(genap)
	r = np.random.choice(ganjil)
	
	f = 2 * a**2 * x**p * y**q * z**r
	g = a * x**int(p/2) * y**int(q/2) * z**int(r/2)
	h = 2 * x * z
	
	soal = fr'$\sqrt{{ {sp.latex(f)} }}=... .$'
	jawab = fr'${sp.latex(g)}\sqrt{{ {sp.latex(h)} }}$'
	pil1 = fr'${sp.latex(g)}$'
	pil2 = fr'${sp.latex(h)}\sqrt{{ {sp.latex(g)} }}$'
	pil3 = fr'${sp.latex(g)}\sqrt{{ {sp.latex(h/2)} }}$'
	pil4 = fr'${sp.latex(g)}\sqrt{{ {sp.latex(3*h)} }}$'
	pg = [jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	tulis(soal, pg, kunci)

def s06():
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	c = np.random.randint(2,10)
	d = np.random.randint(-9,0)
	
	p = np.random.randint(2,7)**2 * 3
	q = np.random.randint(2,7)**2 * 2
	
	g = a * sp.sqrt(2) + b * sp.sqrt(3)
	h = c * sp.sqrt(p) + d * sp.sqrt(q)
	jawab = g + h
	soal = fr'${sp.latex(g)}+ {c}\sqrt{{ {p} }} {d}\sqrt{{ {q} }}=... .$'
	pil1 = g - h
	pil2 = -jawab
	pil3 = -pil1 + g
	pil4 = pil1 + g
	pg = [jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s07():
	a = np.random.randint(2,10)
	bil2 = [2,3,5,6,7,10]
	b = np.random.choice(bil2)
	
	soal = fr'$({a}+\sqrt{{ {b} }})({a}-\sqrt{{ {b} }})=... .$'
	jawab = sp.expand((a + sp.sqrt(b))*(a - sp.sqrt(b)))
	pil1 = -jawab
	pil2 = sp.expand((b + sp.sqrt(a))*(b - sp.sqrt(a)))
	pil3 = -pil2
	pil4 = a**2 + b**2
	pg = [jawab, pil1, pil2, pil3, pil4]
	pg.sort()
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s08():
	bil2 = [3,5,6,7,10]
	b1 = np.random.choice(bil2)
	b2 = 2
	a = np.random.randint(2,10) * (b1 - b2)
	
	f = a/(sp.sqrt(b1) + sp.sqrt(b2))
	soal = fr'$\dfrac{{ {a} }}{{ \sqrt{{ {b1} }} + \sqrt{{ {b2} }} }}=... .$'
	jawab = a*(sp.sqrt(b1) - sp.sqrt(b2))/(b1 - b2)
	pil1 = -jawab
	pil2 = sp.sqrt(b1) - sp.sqrt(b2)
	pil3 = -pil2
	pil4 = int(a/(b1 - b2))
	pg = [jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s09():
	bil2 = [5,20,25,40,50]
	b = np.random.choice(bil2)
	
	pil1 = 1 - x
	pil2 = 1 + x
	pil3 = 2*(1-x)
	pil4 = 2*x + 1
	pil5 = 2 - x
	
	pil = [pil1, pil2, pil3, pil4, pil5]
	jawab = pil[bil2.index(b)]
	soal = fr'Jika $\log 2 = x$ maka $\log {b} = ... .$'
	
	pg = pil
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s10():
	soal = 'Diketahui $\log x - \log 25 = \log 0,4$. Nilai $x=... .$'
	jawab = 10
	kunci = np.random.randint(0,5)
	pg = [ jawab + i for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s11():
	bil2 = [-2, -1, 1, 2, 3]

	m1 = np.random.choice(bil2)
	m2 = np.random.choice(bil2)
	c1 = np.random.choice(bil2)
	c2 = np.random.choice(bil2)
	
	kiri = (m1*x + c1)*a
	kanan = (m2*x + c2)*(1 - a)
	solusi = sp.solve(kiri - kanan, x)
	jawab = solusi[0]
	
	soal = fr'Diketahui $\log 2 = a$. Solusi dari $2^{{ {sp.latex(m1*x + c1)} }} = 5^{{ {sp.latex(m2*x + c2)} }}$ dalam $a$ adalah ... .'
	kunci = np.random.randint(0, 5)
	pg = [ sp.simplify(jawab + i) for i in range(-kunci, 5 - kunci) ]
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s12():
	kiri = 4**(x + 1) * 3**(2-3*x)
	kanan = 2**(5+x) * 3**(5-4*x)
	solusi = sp.solve(kiri - kanan, x)
	soal = fr'Diketahui $4^{{x+1}}\times 3^{{2-3x}}=2^{{5+x}}\times 3^{{5-4x}}$. Nilai dari $x= ... .$'
	jawab = solusi[0]
	# ~ print(kiri)
	# ~ print(kanan)
	# ~ print(soal)
	# ~ print(jawab)
	kunci = np.random.randint(0, 5)
	pg = [ sp.simplify(jawab + i) for i in range(-kunci, 5 - kunci) ]
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s13():
	bil2 = [3,5,6,7,10]
	b1 = np.random.choice(bil2)

	a = np.random.randint(2,10) * (b1)
	
	f = a/(sp.sqrt(b1))
	soal = fr'$\dfrac{{ {a} }}{{ \sqrt{{ {b1} }} }}=... .$'
	jawab = a*(sp.sqrt(b1))/(b1)
	pil1 = -jawab
	pil2 = sp.sqrt(b1)
	pil3 = -pil2
	pil4 = int(a/(b1))
	pg = [jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s14():
	b = np.random.randint(2, 6)
	c = b **np.random.randint(2, 6)
	y = b**x - c
	soal = fr'Grafik fungsi $y={sp.latex(y)}$ berpotongan terhadap sumbu $X$ ketika $y=... .$'
	solusi = sp.solve(y, x)
	jawab = solusi[0]
	kunci = np.random.randint(0, 5)
	pg = [ sp.simplify(jawab + i) for i in range(-kunci, 5 - kunci) ]
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)
	

def s15():
	b = np.random.randint(2, 6)
	c = b ** np.random.randint(2, 6)
	y = b**x - c
	soal = fr'Grafik fungsi $y={sp.latex(y)}$ berpotongan terhadap sumbu $Y$ ketika $x=... .$'
	solusi = y.subs(x, 0)
	jawab = solusi
	kunci = np.random.randint(0, 5)
	pg = [ sp.simplify(jawab + i) for i in range(-kunci, 5 - kunci) ]
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s16():
	bil2 = [2,3,4,5,6,7,8,9]
	atas = np.random.choice(bil2)
	bil3 = [ i for i in bil2 if i!= atas ]
	bawah = np.random.choice(bil3)
	p = -np.random.choice([2,3,4])
	
	f = (atas/(bawah*a))**p
	soal = fr'$\left(\dfrac{{ {atas} }}{{ {bawah} a }}\right)^{{ {p} }}=... .$'
	jawab = f
	pil1 = 1/f
	pil2 = -f
	pil3 = -1/f
	pil4 = f * atas
	
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s17():
	p = np.random.randint(2,5)
	q = np.random.randint(2,5)
	
	soal = fr'Jika $\left( \dfrac{{1}}{{ x^{p} }} \right)^{q}=x^a$ maka nilai $a$ adalah ... .'
	
	jawab = -p * q
	pil1 = p*q
	pil2 = p - q
	pil3 = q - p
	pil4 = sp.Rational(q,p)
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s18():
	bil2 = [2, 3, 5, 6, 7, 10]
	a = np.random.choice(bil2)
	bil3 = [ i for i in bil2 if i != a ]
	b = np.random.choice(bil3)
	
	tambah = a + b
	kali = a * b
	
	soal = fr'$\sqrt{{ {tambah} + 2\sqrt{{ {kali} }} }}=... .$'
	jawab = sp.sqrt(a) + sp.sqrt(b)
	pil1 = sp.sqrt(a) - sp.sqrt(b)
	pil2 = -jawab
	pil3 = -pil1
	pil4 = sp.sqrt(tambah) + sp.sqrt(kali)
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s19():
	bil2 = [2, 3, 5, 6, 7, 10]
	a = np.random.choice(bil2)
	bil3 = [ i for i in bil2 if i != a ]
	b = np.random.choice(bil3)
	
	tambah = a**2 + b
	kali = b
	
	soal = fr'$\sqrt{{ {tambah} + {2*a}\sqrt{{ {kali} }} }}=... .$'
	jawab = a + sp.sqrt(b)
	pil1 = sp.sqrt(a) - sp.sqrt(b)
	pil2 = -jawab
	pil3 = -pil1
	pil4 = sp.sqrt(tambah) + sp.sqrt(kali)
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s20():
	
	m1 = np.random.randint(1,5)
	m2 = np.random.randint(1,5)
	c1 = np.random.choice(bil)
	c2 = np.random.choice(bil)
	
	kiri = 8**(m1*x+c1)
	kanan = 4**(m1*x+c2)
	solusi = sp.solve(kiri - kanan, x)
	soal = fr'Jika ${sp.latex(kiri)}={sp.latex(kanan)}$ maka $x=... .$'
	jawab = solusi[0]
	pil1 = -jawab
	pil2 = sp.simplify(jawab + 1)
	pil3 = -pil2
	pil4 = jawab * 2
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s21():
	a = np.random.randint(2,8)
	b = np.random.randint(2,8)
	
	basis = a * b
	p = np.random.randint(2,5)
	soal = fr'${{}}^{{ {basis} }}\log {a} + {{}}^{{ {basis} }}\log {p*b} - {{}}^{{ {basis} }}\log {p*a} + {{}}^{{ {basis} }}\log {b} - {{}}^{{ {basis} }}\log {sp.latex(sp.Rational(b,a))}=... .$'
	
	jawab = 1
	kunci = np.random.randint(0, 5)
	pg = [ sp.simplify(jawab + i) for i in range(-kunci, 5 - kunci) ]
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)
	

def s22():
	x = np.random.randint(2,5)
	bil2 = [2,3,4,5]
	q = np.random.randint(2,4)
	p = np.random.randint(q+1,5)
	bil3 = [ i for i in bil2 if i != p ]
	a = x**p
	b = x**q
	
	soal = fr'Nilai dari ${{}}^{{ {a} }}\log {b}$ adalah ... .'
	jawab = sp.Rational(p,q)
	pil1 = sp.Rational(a,b)
	pil2 = sp.Rational(b,a)
	pil3 = sp.Rational(q,p)
	pil4 = b - a
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s23():
	m1 = np.random.randint(1,3)
	m2 = np.random.randint(m1+1,6)
	c1 = np.random.randint(1,5)
	c2 = np.random.randint(-5, -1)
	
	kiri1 = m1*x + c1
	kiri2 = m2*x + c2
	
	b = np.random.randint(2,8)
	soal = fr'Himpunan penyelesaian dari ${{}}^{{ {b} }}\log({sp.latex(kiri1)}) - {{}}^{{ {b} }}\log({sp.latex(kiri2)})=1$ adalah ... .' 
	solusi = sp.solve(kiri1 - b*kiri2, x)
	jawab = solusi[0]
	pil1 = jawab * b
	pil2 = 1/jawab
	pil3 = 1/pil1
	pil4 = jawab / b
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s24():
	a = np.random.randint(2,5)
	b = np.random.randint(-5, -1)
	
	x = sp.Pow(a, b)
	soal = f'Nilai dari ${a}^{{ {b} }}$ = ... .'
	jawab = x
	pil1 = sp.Pow(a,-b)
	pil2 = sp.Pow(b, a)
	pil3 = sp.Pow(b,-a)
	pil4 = a * b
	pg = [jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def s25():
	p = np.random.randint(2, 6)
	x = sp.Pow(10, p)
	
	soal = fr'Nilai dari $\log {x} = ... .$'
	kunci = np.random.randint(0,5)
	pg = [ p + i for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s26():
	x = np.random.randint(2,5)
	y = np.random.randint(2,5)
	p = x**y
	
	soal = fr'Nilai dari ${{}}^{{ {x} }}\log {p}$ adalah ... .'
	jawab = y
	kunci = np.random.randint(0, 5)
	pg = [ y + i for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s27():
	bil2 = [ 2,3,5,6,7 ]
	a = np.random.choice(bil2)
	bil3 = [ i for i in bil2 if i != a ]
	b = np.random.choice(bil3)
	
	x = 4 * a
	y = 9 * b
	
	tambah = x + y
	kali = a * b
	soal = fr'$\sqrt{{ {tambah} + {2*a}\sqrt{{ {kali} }} }}=... .$'
	jawab = sp.simplify(sp.sqrt(x) + sp.sqrt(y))
	pil1 = a * sp.sqrt(2) + b * sp.sqrt(3)
	pil2 = b * sp.sqrt(2) + a * sp.sqrt(3)
	pil3 = 3 * sp.sqrt(a) + 2 * sp.sqrt(b)
	pil4 = sp.sqrt(a) + sp.sqrt(b)
	pg = [ jawab, pil1, pil2, pil3, pil4]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)
	

def s28():
	pass

def s29():
	pass

def s30():
	pass



def u01():
	a = np.random.randint(2,4)
	c = sp.Pow(a, np.random.randint(-4, 4))
	y = a**x - c
	soal = f'Lukislah grafik $y={sp.latex(y)}$ dengan menggunakan tabel bantuan untuk nilai $x$ pada rentang \{{-2, -1, 0, 1, 2\}}. Gambarkan pula garis asimtot datarnya dengan garis putus-putus.'
	kunci = f'Gambar lukisan grafik $y={sp.latex(y)}$ dengan asimtot datarnya.'
	tulis_uraian(soal, kunci)
	
	sol = sp.solve(y, x)
	sbx = sol[0]
	sby = 1 + c
	soal2 = 'Tentukan titik potong grafik fungsi tersebut terhadap sumbu $X$ dan sumbu $Y$. Tuliskan langkah-langkahnya secara terperinci.'
	kunci2 = f'Titik potong $y={sp.latex(y)}$ terhadap sumbu $X$ pada $({sp.latex(sbx)}, 0)$ dan sumbu $Y$ pada $(0, {sp.latex(sby)})$.'
	tulis_uraian(soal2, kunci2)


def bonus1():
	n = np.random.randint(3,7)
	f = r'a\times '*n + 'a'
	
	g = a**(n+1)
	soal = f'Bentuk lain dari ${f}$ adalah ... .'
	jawab = g
	kunci = np.random.randint(0, 5)
	pg = [ a**i * g for i in range(-kunci, 5 - kunci) ]
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)

def bonus2():
	p = np.random.randint(2,5)
	q = np.random.randint(2,9)
	r = np.random.randint(2,9)
	
	y = x**p * x**q / x**r
	soal = fr'Bentuk sederhana dari $\dfrac{{x^{p}\times x^{q} }}{{ x^{r} }}$ adalah ... .'
	jawab = y
	kunci = np.random.randint(0, 5)
	pg = [ x**i * y for i in range(-kunci, 5 - kunci) ]
	pg1 = [ f'${sp.latex(i)}$' for i in pg ]
	tulis(soal, pg1, kunci)
	
def bonus3():
	bil2 = list(range(2,10))
	a = np.random.choice(bil2)
	bil3 = [ i for i in bil2 if i != a ]
	b = np.random.choice(bil2)
	bil4 = [ i for i in bil2 if i != b ]
	c = np.random.choice(bil3)
	
	f = sp.Rational(a*b, c)
	soal = fr'$\log {a} + \log {b} - \log {c} = ... .$'
	jawab = f
	pil1 = sp.Rational(a*c, b)
	pil2 = sp.Rational(b*c, a)
	pil3 = sp.Rational(c, b*a)
	pil4 = sp.Rational(a, b*c)
	pg = [ jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	pg1 = [ fr'$\log \left({sp.latex(i)}\right)$' for i in pg ]
	tulis(soal, pg1, kunci)
	


















































os.system('mkdir -p soal kunci')
for i in range(30):
	awal(ke=i)
	s01()
	bonus1()
	s02()
	s03()
	bonus2()
	s04()
	s05()
	s06()
	s07()
	s08()
	s09()
	s10()
	s11()
	s12()
	s13()
	s14()
	s15()
	s16()
	s17()
	s18()
	s19()
	s20()
	s21()
	s22()
	s23()
	s24()
	s25()
	bonus3()
	s26()
	s27()
	s28()
	s29()
	s30()
	tutup_pg()
	uraian()
	u01()
	akhir()
	os.system(f'mv soal.pdf soal/soal_{i}.pdf')
	os.system(f'mv kunci.pdf kunci/kunci_{i}.pdf')

os.system('gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=soal/sts_mat_10.pdf soal/soal_*')
os.system('gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=kunci/sts_mat_10_kunci.pdf kunci/kunci_*')
