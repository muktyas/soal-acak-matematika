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




def tulis(teks_soal='', pg_array='', kunci=''):
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
f = sp.Function('f')
g = sp.Function('g')
bil = [ i for i in range(-9,10) if i != 0 ]

def inv(f):
	iy = sp.solve(y - f, x)
	ix = iy[0].subs(y, x)
	f_inv = sp.factor(ix)
	return sp.simplify(f_inv)
	


def s01():
	m = np.random.choice(bil)
	c = np.random.choice(bil)
	a = np.random.choice(bil)
	y = m * x + c
	soal = f'Diketahui f$(x)={sp.latex(y)}$. Nilai f$({a})$ = ... .'
	kunci = np.random.randint(0, 5)
	
	pg = [ y.subs(x, a + i) for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)
	
def s02():
	m = np.random.choice(bil)
	c = np.random.choice(bil)
	a = np.random.choice(bil)
	y = m * x + c
	soal = f'Diketahui f$(x)={sp.latex(y)}$. Nilai f$^{{-1}}({a})$ = ... .'
	kunci = np.random.randint(0, 5)
	
	pg = [ f'${sp.latex(sp.solve(y - (a + i))[0])}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s03():
	m = np.random.choice(bil)
	c = np.random.choice(bil)
	a = 0 #np.random.choice(bil)
	y = m * x + c
	f = sp.sqrt(y)
	soal = f'Diketahui f$(x)={sp.latex(f)}$. Domain fungsi f adalah ... .'
	kunci = np.random.randint(0, 5)
	
	# ~ print(y)
	pg = [ fr'$\{{ x\ge {sp.latex(sp.solve(y - (a + i))[0])},\: x\in \mathbb{{R}} \}}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s04():
	p = np.random.choice(bil)
	y = (x + p)**2
	f = sp.expand(y)
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$. Range fungsi f adalah ... .'
	kunci = np.random.randint(0, 5)
	
	# ~ print(y)
	pg = [ fr'$\{{ x\ge {sp.latex(-p + i)},\: x\in \mathbb{{R}} \}}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s05():
	a1 = np.random.randint(2,5)
	b1 = np.random.randint(-5,5)
	c1 = np.random.randint(-5,5)

	b2 = np.random.randint(-5,5)
	c2 = np.random.randint(-5,5)
	
	f = a1*x**2 + b1*x + c1
	g = b2*x + c2
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Rumus fungsi (f + g)$(x)$ adalah ... '
	h = sp.simplify(f + g)
	jawab = h
	kunci = np.random.randint(0, 5)
	pg = [ fr'${sp.latex(h + i*g)}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s06():
	a1 = np.random.randint(2,5)
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)

	b2 = np.random.choice(bil)
	c2 = np.random.choice(bil)
	
	f = 1/(b1*x + c1)
	g = 1/(b2*x)
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Rumus fungsi (f - g)$(x)$ adalah ... '
	h = sp.simplify(f - g)
	jawab = h
	kunci = np.random.randint(0, 5)
	pg = [ fr'${sp.latex(sp.simplify(sp.expand(h - i*g)))}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s07():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)

	b2 = np.random.choice(bil)
	c2 = np.random.choice(bil)
	
	f = b1*x + c1
	g = b2*x + c2
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Rumus fungsi (fg)$(x)$ adalah ... '
	h = sp.expand(f * g)
	jawab = h
	kunci = np.random.randint(0, 5)
	pg = [ fr'${sp.latex(sp.expand(h + i*g))}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s08():
	a1 = np.random.randint(2,5)
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)

	b2 = np.random.choice(bil)
	c2 = np.random.choice(bil)
	
	f = a1*x**2 + b1*x + c1
	g = x + c2
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Rumus fungsi $\\left(\\frac{{f}}{{g}}\\right)(x)$ adalah ... '
	h = sp.apart(f / g)
	jawab = h
	kunci = np.random.randint(0, 5)
	pg = [ fr'${sp.latex(h + i)}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s09():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	
	f = b1*x + c1
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$. Rumus fungsi $f^{{-1}}(x)$ adalah ... '
	h = inv(f)
	jawab = h
	kunci = np.random.randint(0, 5)
	pg = [ fr'${sp.latex(h + i)}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s10():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	b2 = np.random.choice(bil)
	
	f = b1*x + c1
	g = 1/(b2*x)
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Rumus fungsi $(\\text{{f}}\\circ \\text{{g}})(x)$ adalah ... '
	h = f.subs(x, g)
	jawab = h
	pil1 = g.subs(x, f)
	pil2 = f * g
	pil3 = inv(g)
	pil4 = f / g
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex(i)}$' for i in pg1 ]
	tulis(soal, pg, kunci)

def s11():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	b2 = np.random.choice(bil)
	
	f = b1*x + c1
	g = b2*x + 10
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Rumus fungsi $(\\text{{g}}\\circ \\text{{f}})(x)$ adalah ... '
	h = g.subs(x, f)
	jawab = h
	pil1 = f.subs(x, g)
	pil2 = f * g
	pil3 = inv(g)
	pil4 = f / g
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex(sp.expand(i))}$' for i in pg1 ]
	tulis(soal, pg, kunci)

def s12():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	bil2 = [ i for i in bil if i!= b1 and i!= c1 ]
	b2 = np.random.choice(bil2)
	
	f = b1*x + c1
	g = b2*x**2
	
	fog = f.subs(x, g)
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan $(\\text{{f}}\\circ \\text{{g}})(x)={sp.latex(fog)}$. Rumus fungsi g$(x)$ adalah ... '
	jawab = g
	pil1 = f.subs(x, fog)
	pil2 = fog.subs(x, f)
	pil3 = fog.subs(x, inv(f))
	pil4 = g.subs(x, f)
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex(sp.expand(i))}$' for i in pg1 ]
	tulis(soal, pg, kunci)

def s13():
	b1 = np.random.choice(bil)
	b2 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	c2 = np.random.choice(bil)
	
	f = b1*x + c1
	g = b2*x + c2
	
	fog = f.subs(x, g)
	
	soal = f'Diketahui g$(x)={sp.latex(g)}$ dan $(\\text{{f}}\\circ \\text{{g}})(x)={sp.latex(fog)}$. Rumus fungsi f$(x)$ adalah ... '
	jawab = f
	pil1 = g.subs(x, fog)
	pil2 = fog.subs(x, g)
	pil3 = fog.subs(x, inv(f))
	pil4 = g.subs(x, f)
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex(sp.simplify(i))}$' for i in pg1 ]
	tulis(soal, pg, kunci)

def s14():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	bil2 = [ i for i in bil if i!= b1 and i!= c1 ]
	b2 = np.random.choice(bil2)
	
	a = np.random.choice([-2, -1, 0, 1, 2])
	
	f = b1*x + c1
	g = b2*x - 10
	
	fog = f.subs(x, g)
	
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Nilai dari $(\\text{{f}}\\circ \\text{{g}})({a})$ adalah ... '
	jawab = fog.subs(x, a)
	pil1 = f.subs(x, a)
	pil2 = g.subs(x, a)
	pil3 = inv(fog).subs(x, a)
	pil4 = inv(g).subs(x, a)
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex(sp.expand(i))}$' for i in pg1 ]
	tulis(soal, pg, kunci)
	

def s15():
	c1 = np.random.randint(1, 9)
	bil2 = [ i for i in bil if i!= c1 ]
	c2 = np.random.randint(3, 9)
	
	a = np.random.choice([0, 1, 2])
	
	g = x + c1
	fog = x**2 - c2
	
	f = fog.subs(x, inv(g))
	
	soal = f'Diketahui g$(x)={sp.latex(g)}$ dan $(\\text{{f}}\\circ \\text{{g}})(x)={sp.latex(fog)}$. Nilai dari f$({a})$ adalah ... '
	jawab = f.subs(x, a)
	pil1 = fog.subs(x, a)
	pil2 = g.subs(x, a)
	pil3 = f.subs(x, a + 1)
	pil4 = f.subs(x, a - 1)
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex(sp.expand(i))}$' for i in pg1 ]
	tulis(soal, pg, kunci)

def s16():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	bil2 = [ i for i in bil if i != b1 and i != c1 ]
	b2 = np.random.choice(bil2)
	c2 = np.random.choice(bil2)
	
	f = b1*x + c1
	g = b2*x + c2
	fperg = f / g
	
	soal = f'Diketahui f$(x)={sp.latex(fperg)}$. Rumus fungsi $\\text{{f}}^{{-1}}(x)$ adalah ... '
	jawab = inv(fperg)
	pil1 = inv(f)
	pil2 = inv(g)
	pil3 = g / f
	pil4 = inv(pil3)
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex((i))}$' for i in pg1 ]
	tulis(soal, pg, kunci)

def s17():
	bil2 = [1,2,3,5,7]
	b1 = np.random.choice(bil2)
	c1 = np.random.choice(bil2)
	bil3 = [ i for i in bil2 if i != b1 and i != c1 ]
	b2 = np.random.choice(bil3)
	c2 = np.random.choice(bil3)
	
	f = b1*x + c1
	g = b2*x + c2
	fperg = f / g
	
	soal = f'Diketahui f$(x)={sp.latex(fperg)}$. Agar f adalah fungsi, maka nilai $x$ yang tidak boleh adalah ... '
	jawab = sp.Rational(-c2, b2)
	kunci = np.random.randint(0, 5)
	pg = [ fr'${sp.latex(jawab + i)}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s18():
	a = 0
	b = np.random.choice(bil)
	b = b**2
	
	g = x - b
	f = sp.sqrt(g)
	soal = f'Diketahui f$(x)={sp.latex(f)}$. Nilai dari $\\text{{f}}^{{-1}}({a})$ adalah ... '
	jawab = inv(f).subs(x, a)
	kunci = np.random.randint(0, 5)
	pg = [ fr'${sp.latex(jawab + i)}$' for i in range(-kunci, 5 - kunci) ]
	tulis(soal, pg, kunci)

def s19():
	b1 = np.random.choice(bil)
	c1 = np.random.choice(bil)
	bil2 = [ i for i in bil if i!= b1 and i!= c1 ]
	b2 = np.random.choice(bil2)
	
	a = np.random.choice([-2, -1, 0, 1, 2])
	
	f = b1*x + c1
	g = b2*x - 21
	
	fog = f.subs(x, g)
	fog_inv = inv(fog)
	soal = f'Diketahui f$(x)={sp.latex(f)}$ dan g$(x)={sp.latex(g)}$. Nilai dari $(\\text{{f}}\\circ \\text{{g}})^{{-1}}({a})$ adalah ... '
	jawab = fog_inv.subs(x, a)
	pil1 = f.subs(x, a)
	pil2 = g.subs(x, a)
	pil3 = fog.subs(x, a)
	pil4 = inv(g).subs(x, a)
	pg1 = [jawab, pil1, pil2, pil3, pil4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = [ fr'${sp.latex(sp.expand(i))}$' for i in pg1 ]
	tulis(soal, pg, kunci)

def s20():
	d = 'pqrs'
	a = np.random.choice(bil)
	e = list(range(a, a+4))
	
	bi = '\{ (p, 1), (q, 2), (r, 3), (s, 4) \}'
	p1 = '\{ (p, 1), (q, 2), (r, 1), (s, 4) \}'
	p2 = '\{ (p, 1), (q, 2), (r, 2), (s, 2) \}'
	p3 = '\{ (p, 1), (p, 2), (r, 3), (s, 4) \}'
	p4 = '\{ (p, 1), (r, 2), (r, 3), (s, 4) \}'
	
	soal = 'Di antara himpunan berikut ini yang merupakan fungsi bijektif adalah ... .'
	jawab = bi
	pg1 = [ jawab, p1, p2, p3, p4 ]
	np.random.shuffle(pg1)
	kunci = pg1.index(jawab)
	pg = pg1
	tulis(soal, pg, kunci)

def s21():
	pass
	

def s22():
	pass

def s23():
	pass

def s24():
	pass

def s25():
	pass

def s26():
	pass

def s27():
	pass
	

def s28():
	pass

def s29():
	pass

def s30():
	pass

	


















































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
	# ~ tutup_pg()
	# ~ uraian()
	# ~ u01()
	akhir()
	
	os.system(f'mv soal.pdf soal/soal_{i}.pdf')
	os.system(f'mv kunci.pdf kunci/kunci_{i}.pdf')

os.system('gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=soal/sts_mat_11.pdf soal/soal_*')
os.system('gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=kunci/sts_mat_11_kunci.pdf kunci/kunci_*')
