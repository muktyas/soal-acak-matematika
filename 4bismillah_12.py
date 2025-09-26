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



def akhir(filename_soal='soal.tex', filename_kunci='kunci.tex'):
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


def lanjut(filename):
	os.system(fr"sed -i '$ d' {filename}")




x, y = sp.symbols('x y')


#transformasi titik

def t_titik(titik, vektor):
	return np.array(titik) + np.array(vektor)

def m_titik_sbx(titik):
	return (titik[0], -titik[1])

def m_titik_sby(titik):
	return (-titik[0], titik[1])

def m_titik_y_x(titik):
	return (titik[1], titik[0])

def m_titik_y_minx(titik):
	return (-titik[1], -titik[0])

def m_titik_x_k(titik, k):
	return (2*k - titik[0], titik[1])

def m_titik_y_h(titik, h):
	return (titik[0], 2*h - titik[1])
	
def r_titik_90(titik):
	return (-titik[1], titik[0])
	
def r_titik_270(titik):
	return (titik[1], -titik[0])
	
def r_titik_180(titik):
	return (-titik[0], -titik[1])
	
def d_titik_x(titik, k):
	return (k*titik[0], titik[1])

def d_titik_y(titik, k):
	return (titik[0], k*titik[1])

def d_titik_o(titik, k):
	return (k*titik[0], k*titik[1])


# transformasi kurva

def t_kurva(f, vektor):
	g = f.subs(x, x - vektor[0]) + vektor[1]
	return sp.simplify(g)

def m_kurva_sbx(f):
	return -f

def m_kurva_sby(f):
	g = f.subs(x, -x)
	return sp.simplify(g)
	
def inv(f):
	iy = sp.solve(y - f, x)
	ix = iy[0].subs(y, x)
	f_inv = sp.factor(ix)
	return sp.simplify(f_inv)

def m_kurva_y_x(f):
	return inv(f)

def m_kurva_y_minx(f):
	g = inv(f)
	f = g.subs(x, -x)
	f = sp.factor(f)
	return sp.simplify(-f)

def m_kurva_x_k(f, k):
	g = f.subs(x, 2*k - x)
	g = sp.simplify(g)
	return g

def m_kurva_y_h(f, h):
	g = 2*h - f
	g = sp.simplify(g)
	return g
	
def r_kurva_90(f):
	g = f.subs(x, -x)
	g = inv(g)
	return g

def r_kurva_270(f):
	g = inv(f)
	return -g

def r_kurva_180(f):
	g = f.subs(x, -x)
	return -g
	
def d_kurva_x(f, k):
	g = f.subs(x, sp.Rational(1,k)*x)
	return g

def d_kurva_y(f, k):
	g = k*f
	return g

def d_kurva_o(f, k):
	g = f.subs(x, sp.Rational(1,k)*x)
	g = k * g
	return g
	

# ~ f = 3*x + 5
# ~ f = x**2 + 3*x + 2
# ~ g = t_kurva(f, [1,2])
# ~ # ~ print(g)
# ~ g = d_kurva_o(f, 4)
# ~ # ~ print(g)

bil = [ i for i in range(-9,10) if i != 0 ]
x, y = sp.symbols('x y')

def s01():
	titik =  [ np.random.choice(bil) for i in range(2) ]
	vektor = [ np.random.choice(bil) for i in range(2) ]
	titik2 = [ titik[i] + vektor[i] for i in range(2) ]
	if titik2[0] == 0:
		vektor[0] += 1
		titik2[0] += 1
	if titik2[1] == 0:
		vektor[1] += 1
		titik2[1] += 1
	soal = fr'Hasil translasi titik $({titik[0]},{titik[1]})$ searah vektor $\binom{{ {vektor[0]} }}{{ {vektor[1]} }}$ adalah ... .'
	# ~ print(soal)
	pg = [tuple(titik2)]
	pg.append(m_titik_sbx(titik2))
	pg.append(m_titik_sby(titik2))
	pg.append(m_titik_y_x(titik2))
	pg.append(m_titik_y_minx(titik2))
	# ~ print(pg)
	np.random.shuffle(pg)
	
	kunci = pg.index(tuple(titik2))
	# ~ print(pg)
	# ~ print(kunci)
	
	tulis(soal, pg, kunci)

# ~ for i in range(20):
	# ~ s01()


def s02():
	titik = [ np.random.choice(bil) for i in range(2) ]
	soal = fr'Hasil pencerminan titik $({titik[0]}, {titik[1]})$ terhadap sumbu $X$ adalah ... .'
	jawab = m_titik_sbx(titik)
	pg = [jawab]
	pg.append(m_titik_sby(titik))
	pg.append(m_titik_y_x(titik))
	pg.append(m_titik_y_minx(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)
	
# ~ s02()

def s03():
	titik = [ np.random.choice(bil) for i in range(2) ]
	soal = fr'Hasil pencerminan titik $({titik[0]}, {titik[1]})$ terhadap sumbu $Y$ adalah ... .'
	jawab = m_titik_sby(titik)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_y_x(titik))
	pg.append(m_titik_y_minx(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s03()

def s04():
	titik = [ np.random.choice(bil) for i in range(2) ]
	soal = fr'Hasil pencerminan titik $({titik[0]}, {titik[1]})$ terhadap garis $y=x$ adalah ... .'
	jawab = m_titik_y_x(titik)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_sby(titik))
	pg.append(m_titik_y_minx(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s04()

def s05():
	titik = [ np.random.choice(bil) for i in range(2) ]
	soal = fr'Hasil pencerminan titik $({titik[0]}, {titik[1]})$ terhadap garis $y=-x$ adalah ... .'
	jawab = m_titik_y_minx(titik)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_sby(titik))
	pg.append(m_titik_y_x(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s05()

def s06():
	titik = [ np.random.choice(bil) for i in range(2) ]
	if titik[0] < 0:
		k = np.random.randint(-10, titik[0])
	else:
		k = np.random.randint(titik[0] + 1, 11)
	soal = fr'Hasil pencerminan titik $({titik[0]}, {titik[1]})$ terhadap garis $x={k}$ adalah ... .'
	jawab = m_titik_x_k(titik, k)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_sby(titik))
	pg.append(m_titik_y_h(titik, k))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s06()

def s07():
	titik = [ np.random.choice(bil) for i in range(2) ]
	if titik[1] < 0:
		h = np.random.randint(-10, titik[1])
	else:
		h = np.random.randint(titik[1] + 1, 11)
	soal = fr'Hasil pencerminan titik $({titik[0]}, {titik[1]})$ terhadap garis $y={h}$ adalah ... .'
	jawab = m_titik_y_h(titik, h)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_sby(titik))
	pg.append(m_titik_x_k(titik, h))
	pg.append(r_titik_90(jawab))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s07()

def s08():
	titik = [ np.random.choice(bil) for i in range(2) ]
	soal = fr'Hasil rotasi titik $({titik[0]}, {titik[1]})$ sebesar $90^\circ$ terhadap titik $(0,0)$ adalah ... .'
	jawab = r_titik_90(titik)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_sby(titik))
	pg.append(r_titik_270(titik))
	pg.append(r_titik_180(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)
# ~ s08()

def s09():
	titik = [ np.random.choice(bil) for i in range(2) ]
	soal = fr'Hasil rotasi titik $({titik[0]}, {titik[1]})$ sebesar $180^\circ$ terhadap titik $(0,0)$ adalah ... .'
	jawab = r_titik_180(titik)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_sby(titik))
	pg.append(r_titik_270(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)
# ~ s09()

def s10():
	titik = [ np.random.choice(bil) for i in range(2) ]
	soal = fr'Hasil rotasi titik $({titik[0]}, {titik[1]})$ sebesar $270^\circ$ terhadap titik $(0,0)$ adalah ... .'
	jawab = r_titik_270(titik)
	pg = [jawab]
	pg.append(m_titik_sbx(titik))
	pg.append(m_titik_sby(titik))
	pg.append(r_titik_180(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)
# ~ s10()

def s11():
	titik = [ np.random.choice(bil) for i in range(2) ]
	k = np.random.randint(2, 10)
	soal = fr'Hasil dilatasi titik $({titik[0]}, {titik[1]})$ terhadap titik $(0,0)$ dengan faktor skala {k} adalah ... .'
	jawab = d_titik_o(titik, k)
	pg = [jawab]
	pg.append(d_titik_x(titik, k))
	pg.append(d_titik_y(titik, k))
	pg.append(m_titik_sby(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)
# ~ s11()

def s12():
	titik = [ np.random.choice(bil) for i in range(2) ]
	k = np.random.randint(2, 10)
	soal = fr'Hasil dilatasi titik $({titik[0]}, {titik[1]})$ searah sumbu $X$ dengan faktor skala {k} adalah ... .'
	jawab = d_titik_x(titik, k)
	pg = [jawab]
	pg.append(d_titik_o(titik, k))
	pg.append(d_titik_y(titik, k))
	pg.append(m_titik_sby(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s12()

def s13():
	titik = [ np.random.choice(bil) for i in range(2) ]
	k = np.random.randint(2, 10)
	soal = fr'Hasil dilatasi titik $({titik[0]}, {titik[1]})$ searah sumbu $Y$ dengan faktor skala {k} adalah ... .'
	jawab = d_titik_y(titik, k)
	pg = [jawab]
	pg.append(d_titik_o(titik, k))
	pg.append(d_titik_x(titik, k))
	pg.append(m_titik_sby(titik))
	pg.append(r_titik_90(titik))
	# ~ print(soal)
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s13()

def s14():
	m = np.random.choice(bil)
	c = np.random.choice(bil)
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	
	x = sp.symbols('x')
	y = m * x + c
	# ~ print(y)
	soal = fr'Hasil translasi garis $y={sp.latex(y)}$ searah vektor $\binom{{ {a} }}{{ {b} }}$ adalah ... .'
	# ~ print(soal)
	jawab = t_kurva(y, [a, b])
	# ~ print(jawab)
	
	pg = [ f'$y={sp.latex(jawab)}$' ]
	pg.append(f'$y={sp.latex(t_kurva(y, [b, a]))}$')
	pg.append(f'$y={sp.latex(t_kurva(y, [-a, b]))}$')
	pg.append(f'$y={sp.latex(t_kurva(y, [-a, -b]))}$')
	pg.append(f'$y={sp.latex(t_kurva(y, [-b, -a]))}$')
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(f'$y={sp.latex(jawab)}$')
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s14()

def s15():
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	c = np.random.choice(bil)
	y = a*x**2 + b*x + c
	
	soal = f'Hasil pencerminan kurva $y={sp.latex(y)}$ terhadap sumbu $X$ adalah ... .'
	# ~ print(soal)
	jawab = m_kurva_sbx(y)
	pg = [ f'$y={sp.latex(jawab)}$' ]
	pg.append(f'$y={sp.latex(m_kurva_sby(y))}$')
	pg.append(f'$y={sp.latex(m_kurva_y_x(y))}$')
	pg.append(f'$y={sp.latex(m_kurva_y_minx(y))}$')
	pg.append(f'$y={sp.latex(m_kurva_x_k(y,a))}$')
	# ~ print(pg)
	np.random.shuffle(pg)
	kunci = pg.index(f'$y={sp.latex(jawab)}$')
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)

# ~ s15()

def s16():
	bil2 = [i for i in range(-5,6) if i != 0]
	p = np.random.choice(bil2)
	q = np.random.choice(bil)
	if p < 0:
		j = np.random.randint(-9, p)
	else:
		j = np.random.randint(p+1, p+5)
	h = j**2 + q
	
	f = (x - p)**2 + q
	
	soal = f'Hasil pencerminan fungsi $f(x)={sp.latex(f)}$ terhadap garis $y={h}$ adalah $g$. Fungsi $f$ dan $g$ berpotongan ketika $x= ...$ .'
	# ~ print(soal)
	jawaban = sp.solve(h - f, x)
	# ~ print(jawaban)
	if np.random.randint(0,2) == 0:
		jawab = jawaban[0]
		pg = [jawab]
		pg.append(-jawab)
		pg.append(-jawaban[1])
		pg.append(jawaban[0] + jawaban[1]+1)
		pg.append(jawaban[0] - jawaban[1]+1)
	else:
		jawab = jawaban[1]
		pg = [jawab]
		pg.append(-jawab)
		pg.append(-jawaban[0])
		pg.append(jawaban[0] + jawaban[1]+1)
		pg.append(jawaban[0] - jawaban[1]+1)
	# ~ print(pg)
	pg.sort()
	kunci = pg.index(jawab)
	# ~ print(pg)
	# ~ print(kunci)
	tulis(soal, pg, kunci)
	# ~ print('-'*40)

def s17():
	a = np.random.randint(1,9)
	b = np.random.randint(-9,0)
	c = np.random.randint(1,5)
	d = np.random.randint(5,9)
	
	f = (a*x + b)/(c*x + d)
	soal = f'Hasil pencerminan fungsi $f(x)={sp.latex(f)}$ terhadap garis $y=x$ adalah $g$. Nilai $g(0)=$ ... .'
	# ~ print(soal)
	f1 = m_kurva_y_x(f)
	# ~ print(f1)
	g = f1.subs(x, 0)
	# ~ print(g)
	jawab = g
	kunci = np.random.randint(0,5)
	pg1 = [ i + jawab for i in range(-kunci, 5 - kunci) ]
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	tulis(soal, pg, kunci)


def s18():
	a = np.random.randint(1,3)
	b = np.random.randint(3,10)
	c = np.random.choice(bil)
	y = sp.Rational(a,b) * x + c
	soal = f'Hasil pencerminan kurva $y={sp.latex(y)}$ terhadap garis $y=-x$ adalah ... .'
	g = m_kurva_y_minx(y)
	# ~ print(soal)
	# ~ print(g)
	jawab = g
	pg1 = [jawab]
	pg1.append(m_kurva_sbx(y))
	pg1.append(m_kurva_sby(y))
	pg1.append(m_kurva_y_x(y))
	pg1.append(r_kurva_90(y))
	# ~ print(pg1)
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)

def s19():
	b = 2 * np.random.choice(bil)
	c = np.random.choice(bil)
	bil2 = [ i for i in range(-5,6) if i != b/2 ]
	k = np.random.choice(bil2)
	
	y = x**2 + b*x + c
	g = m_kurva_x_k(y, k)
	soal = f'Hasil pencerminan kurva $y={sp.latex(y)}$ terhadap garis $x=k$ adalah $y={sp.latex(g)}$. Nilai $k=$... .'
	# ~ print(soal)
	jawab = k
	kunci = np.random.randint(0,5)
	pg = [ i + jawab for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)
	
def s20():
	basis = np.random.randint(2,8)
	m = np.random.choice(bil)
	c = np.random.choice(bil)
	f = basis**(m*x + c)
	f1 = basis**(m*x - c)
	f2 = basis**(c*x + m)

	jawab = m_kurva_sby(f)
	soal = f'Hasil pencerminan kurva $y={sp.latex(f)}$ terhadap sumbu $Y$ adalah ... .'
	pg1 = [jawab]
	pg1.append(m_kurva_sbx(f))
	pg1.append(m_kurva_sby(f1))
	pg1.append(m_kurva_sbx(f1))
	pg1.append(m_kurva_sby(f2))
	# ~ print(pg1)
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)

def s21():
	m = np.random.choice(bil)
	c = np.random.choice(bil)
	y = m*x + c
	jawab = r_kurva_270(y)
	soal = fr'Hasil rotasi garis $y={sp.latex(y)}$ sebesar $270^\circ$ terhadap titik $(0,0)$ adalah ... .'
	pg1 = [jawab]
	pg1.append(r_kurva_180(y))
	pg1.append(r_kurva_90(y))
	pg1.append(m_kurva_sbx(y))
	pg1.append(m_kurva_sby(y))
	# ~ print(pg1)
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)

def s22():
	a = np.random.randint(-4,0)
	b = np.random.randint(1,4)
	p = np.random.choice(bil)
	q = np.random.choice(bil)
	r = np.random.choice(bil)
	
	y = (x + p) * (x + q) * (x + r)
	jawab = t_kurva(y, [a,b])
	soal = fr'Hasil translasi kurva $y={sp.latex(y)}$ searah vektor $\binom{{ {a} }}{{ {b} }}$ adalah ... .'
	pg1 = [jawab]
	pg1.append(t_kurva(y, [-a, b]))
	pg1.append(t_kurva(y, [-a, -b]))
	pg1.append(t_kurva(y, [a, -b]))
	pg1.append(m_kurva_sbx(y))
	
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)

def s23():
	b1 = np.random.choice(bil) * 2
	c1 = np.random.choice(bil)
	f1 = x**2 + b1*x + c1
	
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	
	f2 = t_kurva(f1, [a, b])
	soal = fr'Kurva $y={sp.latex(f1)}$ ditranslasi searah vektor $\binom{{a}}{{b}}$ menjadi $y={sp.latex(f2)}$. Nilai $a+b=...$ .'
	jawab = a + b
	kunci = np.random.randint(0, 5)
	pg = [ i + jawab for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s24():
	b1 = np.random.choice(bil) * 2
	c1 = np.random.choice(bil)
	f1 = x**2 + b1*x + c1
	
	k = np.random.randint(2,5)
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	
	f2 = d_kurva_y(f1, k)
	f3 = t_kurva(f2, [a, b])
	soal = fr'Kurva $y=f(x)$ didilatasi searah sumbu $Y$ dengan faktor skala {k} kemudian ditranslasi searah vektor $\binom{{ {a} }}{{ {b} }}$ menjadi $y={sp.latex(f3)}$. Nilai $f(1)=...$ .'
	jawab = f1.subs(x,1)
	kunci = np.random.randint(0, 5)
	pg = [ i + jawab for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s25():
	# ~ titik_awal = np.array([ [-2,3], [-1, -2], [1, -1] ])
	titik1 = [-2, 3]
	titik2 = [-1, np.random.randint(-5, 0)]
	titik3 = [1, np.random.randint(titik2[1], 3)]
	titik_awal = np.array([ titik1, titik2, titik3 ])
	# ~ titik_cermin = np.array([m_titik_sby(titik) for titik in titik_awal])
	# ~ print(titik_awal)
	# ~ # ~ print(titik_cermin)
	k = np.random.randint(2,5)
	a = 0
	b = np.random.randint(-5, 0)
	# ~ b = 0
	vektor = np.array([a, b])
	
	# ~ titik_dilatasi = np.array([d_titik_y(titik, k) for titik in titik_cermin])
	# ~ titik_translasi = np.array([t_titik(titik, vektor) for titik in titik_dilatasi])
	
		
	titik_akhir = k*(titik_awal) + vektor
	# ~ # ~ print(titik_translasi)
	# ~ print(titik_akhir)
	
	plt.rcParams["font.family"] = "Nimbus Roman"
	plt.rcParams["mathtext.fontset"] = "stix"
	
	fig, ax = plt.subplots(figsize=(7, 6))
	
	ax.plot(titik_awal[:,0], titik_awal[:,1], '-b')
	# ~ plt.plot(titik_translasi[:,0], titik_translasi[:,1], '--b')
	ax.plot(titik_akhir[:,0], titik_akhir[:,1], '--k')
	ax.set_aspect('equal')
	ax.grid(True, linestyle='-', which='both', alpha=0.5)
	xs = np.concatenate((titik_awal[:,0], titik_akhir[:,0]))
	ys = np.concatenate((titik_awal[:,1], titik_akhir[:,1]))
	xmin, xmax = min(xs), max(xs) + 1
	ymin, ymax = min(ys), max(ys) + 1
	ax.text(-2.2, 3, r"$y = f(x)$", fontsize=10, color="k", va="top", ha="right")
	# ~ print(titik_awal[:,0])
	# ~ print(titik_akhir[:,0])
	# ~ # ~ print(np.concatenate(
	ax.set_xticks(np.arange(xmin, xmax))
	ax.set_yticks(np.arange(ymin, ymax))
	ax.tick_params(labelsize=7)
	# --- buat sumbu dengan panah ---
	# ~ for spine in ax.spines.values():
		# ~ spine.set_linewidth(0.8)

	# tambahkan panah manual
	ax.arrow(xmin, 0, xmax-xmin-1, 0, head_width=0.2, head_length=0.3, fc='black', ec='black')
	ax.arrow(0, ymin, 0, ymax-ymin-1, head_width=0.2, head_length=0.3, fc='black', ec='black')


	# tambahkan label X dan Y di ujung panah
	ax.text(xmax, -0.3, "$X$", fontsize=10, ha="left", va="center")
	ax.text(-0.3, ymax, "$Y$", fontsize=10, ha="center", va="bottom")

	ax.spines["left"].set_position("zero")
	ax.spines["bottom"].set_position("zero")
	ax.spines["right"].set_color("none")
	ax.spines["top"].set_color("none")
	plt.savefig('transformasi.png', dpi=200, bbox_inches='tight')
	# ~ plt.show()
	
	soal = r'Perhatikan gambar berikut ini.\\ \includegraphics[width=.3\textwidth]{transformasi}\\Diketahui grafik fungsi $y=f(x)$ adalah yang bergaris tegas. Rumus fungsi yang bergaris putus-putus adalah ... .'
	soal = r'''
\begin{minipage}{0.35\textwidth}
\includegraphics[width=\textwidth]{transformasi}
\end{minipage}
\hfill
\begin{minipage}{0.6\textwidth}
Perhatikan gambar di samping. Diketahui grafik fungsi $y=f(x)$ adalah yang bergaris tegas. Rumus fungsi yang bergaris putus-putus adalah ... .
\end{minipage}
	
	'''
	
	f = sp.Function('f')
	# ~ jawab = f'y={k}f(x){b}'
	jawab = k*f(sp.Rational(1,k) * x)+b
	# ~ print(jawab)
	pg1 = [jawab]
	# ~ pg1.append(f'y={b}f(x)+{k}')
	# ~ pg1.append(f'y={b}f(x)-{k}')
	# ~ pg1.append(f'y={-b}f(x)-{k}')
	# ~ pg1.append(f'y={-k}f(x)+{-b}')
	pg1.append(b*f(sp.Rational(1,k) * x) + k)
	pg1.append(b*f(sp.Rational(1,-b) * x) - k)
	pg1.append(-b*f(x) + k)
	pg1.append(k*f(sp.Rational(1,k) * x) - b)
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)
	
	
def s26():
	
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	c = np.random.choice(bil)
	k = np.random.randint(2,5)
	
	f = (x + a) * (b*x + c)
	soal = f'Hasil rotasi kurva $y={sp.latex(f)}$ sebesar $180^\\circ$ terhadap titik $(0,0)$ dilanjutkan dilatasi dengan skala {k} searah sumbu $X$ adalah ... .'
	# ~ print(f)
	# ~ print(soal)
	g = r_kurva_180(f)
	h = d_kurva_x(g, k)
	# ~ print(sp.latex(h))
	# ~ print(sp.latex(sp.simplify(h)))
	jawab = sp.simplify(h)
	pg1 = [jawab]
	pg1.append(sp.simplify(g))
	pg1.append(sp.simplify(-g))
	pg1.append(sp.simplify(-f))
	pg1.append(sp.simplify(-h))
	
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)

def s27():
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	soal = f'Hasil transformasi kurva $y=f(x)$ yang dirotasikan $180^\\circ$ kemudian ditranslasi searah vektor $\\binom{{ {a} }}{{ {b} }}$ adalah ... .'
	
	# ~ print(soal)
	f = sp.Function('f')
	fx = f(x)
	rf = r_kurva_180(fx)
	g = t_kurva(rf, [a, b])
	# ~ print(g)
	jawab = g
	pg1 = [jawab]
	pg1.append(rf)
	pg1.append(t_kurva(fx, [a, b]))
	pg1.append(t_kurva(fx, [-a, -b]))
	pg1.append(t_kurva(rf, [-a, -b]))
	
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ f'$y={sp.latex(i)}$' for i in pg1 ]
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)

def s28():
	bil2 = [i for i in bil if i != -1 and i != 1]
	k = np.random.choice(bil2)
	b = np.random.choice(bil)
	if k < 0:
		t1 = 'pencerminan terhadap sumbu $X$, '
		t2 = f'dilatasi dengan faktor skala {-k} searah sumbu $Y$'
	else:
		t1 = ''
		t2 = f'dilatasi dengan faktor skala {k} searah sumbu $Y$'
	t3 = f'translasi searah vektor $\\binom{{0}}{{ {b} }}$'
	
	f = sp.Function('f')
	fx = f(x)
	y = b + k*fx
	soal = f'Proses transformasi dari kurva $y=f(x)$ menjadi $y={sp.latex(y)}$ adalah ... .'
	# ~ print(soal)
	
	jawab = t1 + t2 + ', ' + t3
	# ~ print(jawab)
	pg1 = [jawab]
	pil1 = t3 + ", " + t1 + t2
	pil2 = fr'pencerminan terhadap sumbu $Y$, dilatasi dengan faktor skala {b} searah sumbu $X$, translasi searah vektor $\binom{{0}}{{ {k} }}$'
	pil3 = fr'pencerminan terhadap sumbu $X$, dilatasi dengan faktor skala {b} searah sumbu $X$, translasi searah vektor $\binom{{ {b} }}{{0}}$'
	pil4 = fr'pencerminan terhadap sumbu $X$, dilatasi dengan faktor skala {k} searah sumbu $X$, translasi searah vektor $\binom{{ {b} }}{{0}}$'
	pg1.append(pil1)
	pg1.append(pil2)
	pg1.append(pil3)
	pg1.append(pil4)
	
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = pg1
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)

def s29():
	k = np.random.randint(2,10)
	a = np.random.choice(bil)
	b = np.random.choice(bil)
	
	y = sp.sqrt(x)
	f = d_kurva_y(y, k)
	g = t_kurva(f, [a,b])
	soal = f'Transformasi yang memetakan fungsi $f(x)={sp.latex(y)}$ ke $g(x)={sp.latex(g)}$ adalah ... .'
	jawab = fr'Dilatasi searah sumbu $Y$ dengan faktor skala {k}, dilanjutkan translasi searah vektor $\binom{{ {a} }}{{ {b} }}$'
	pg1 = [jawab]
	pil1 = fr'Dilatasi searah sumbu $X$ dengan faktor skala {k}, dilanjutkan translasi searah vektor $\binom{{ {a} }}{{ {b} }}$'
	pil2 = fr'Dilatasi searah sumbu $X$ dengan faktor skala {a}, dilanjutkan translasi searah vektor $\binom{{ {k} }}{{ {b} }}$'
	pil3 = fr'Dilatasi searah sumbu $Y$ dengan faktor skala {a}, dilanjutkan translasi searah vektor $\binom{{ {k} }}{{ {b} }}$'
	pil4 = fr'Dilatasi searah sumbu $Y$ dengan faktor skala {k}, dilanjutkan translasi searah vektor $\binom{{ {b} }}{{ {a} }}$'
	
	pg1.append(pil1)
	pg1.append(pil2)
	pg1.append(pil3)
	pg1.append(pil4)
	
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = pg1
	# ~ print(kunci)
	# ~ print(pg)
	tulis(soal, pg, kunci)
	
def s30():
	k = np.random.choice(bil)
	a = np.random.randint(1, 10)
	b = np.random.randint(1, 10)
	
	soal = f'Garis $y=mx+c$ ditranslasi {a} satuan ke kiri dan {b} satuan ke bawah, kemudian dicerminkan terhadap sumbu $X$ menghasilkan garis $y={k}x$. Nilai $m-c$ adalah ... .'
	
	y = k * x
	f = m_kurva_sbx(y)
	g = t_kurva(f, [a, b])
	
	m, c = sp.symbols('m c')
	mc = sp.solve(m * x + c - g, [m, c])
	# ~ print(mc)
	jawab = mc[m] - mc[c]
	# ~ print(jawab)
	kunci = np.random.randint(0, 5)
	pg = [ i + jawab for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)
	
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
	
def u01():
	genap_min = [ 2 * i for i in range(-2, 0) if i != 0 ]
	genap_plus = [ 2 * i for i in range(1, 3) if i != 0 ]
	ganjil = [ 2 * i + 1 for i in range(-5, 5) ]
	a = np.random.choice(genap_min)
	p = np.random.choice(genap_plus)
	q = np.random.choice(ganjil)
	
	y = a * (x + p)**2 + q
	f = sp.expand(y)
	soal = f'Nyatakan $y={sp.latex(f)}$ ke dalam bentuk $y={a}(x+p)^2+q$.'
	# ~ print(sp.latex(y))
	# ~ print(sp.latex(f))
	# ~ print(soal)
	
	kunci = f'$y={sp.latex(f)}\Longrightarrow y={sp.latex(y)}$'
	tulis_uraian(soal, kunci)
	
	soal2 = fr'''Fungsi $f$ dan $g$ didefinisikan oleh
	\begin{{align*}}
		f(x)&=x^2,\quad\quad x\in \mathbb{{R}}\\
		g(x)&={sp.latex(f)},\quad x\in \mathbb{{R}}
	\end{{align*}}
	Tuliskan urutan transformasi dari kurva $y=f(x)$ menjadi $y=g(x)$ secara terperinci.'''
	
	kunci2 = fr'Pencerminan terhadap sumbu $X$, dilatasi faktor skala {-a} searah sumbu $Y$, translasi searah vektor $\binom{{ {-p} }}{{ {q} }}$'
	tulis_uraian(soal2, kunci2)













os.system('mkdir -p soal kunci')
for i in range(30):
	awal(ke=i)
	s01()
	s02()
	s03()
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

os.system('gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=soal/sts_mat_12.pdf soal/soal_*')
os.system('gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=kunci/sts_mat_12_kunci.pdf kunci/kunci_*')
