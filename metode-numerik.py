import math

# Parameter
x0, y0 = 1.5, 3.5
epsilon = 0.000001
max_iter = 1000

print("="*80)
print("PENYELESAIAN SISTEM PERSAMAAN NON LINEAR")
print("f1(x,y) = x^2 + xy - 10 = 0")
print("f2(x,y) = y + 3xy^2 - 57 = 0")
print(f"Tebakan awal: x0 = {x0}, y0 = {y0}")
print(f"Epsilon: {epsilon}")
print(f"NIMx = 72 mod 4 = 0")
print("="*80)

# METODE 1: ITERASI TITIK TETAP - JACOBI dengan g1A dan g2A
print("\n" + "="*80)
print("METODE 1: ITERASI TITIK TETAP - JACOBI (g1A dan g2A)")
print("="*80)
print("Fungsi iterasi:")
print("g1A: x = sqrt(10 - xy)")
print("g2A: y = sqrt((57 - y) / (3x))")
print("-"*80)

def g1A_jacobi(x, y):
    val = 10 - x*y
    if val <= 0:
        print(f"Warning: 10 - xy = {val} <= 0 pada x={x:.6f}, y={y:.6f}")
        return None
    return math.sqrt(val)

def g2A_jacobi(x, y):
    if abs(x) < 1e-10:
        return None
    val = (57 - y) / (3*x)
    if val <= 0:
        print(f"Warning: (57-y)/(3x) = {val} <= 0 pada x={x:.6f}, y={y:.6f}")
        return None
    return math.sqrt(val)

x, y = x0, y0
print(f"{'Iter':<6} {'x':<15} {'y':<15} {'deltaX':<15} {'deltaY':<15}")
print("-"*80)
print(f"{0:<6} {x:<15.6f} {y:<15.6f} {0.0:<15.6f} {0.0:<15.6f}")

converged = False
for i in range(1, max_iter + 1):
    x_old, y_old = x, y
    x_new = g1A_jacobi(x_old, y_old)
    y_new = g2A_jacobi(x_old, y_old)
    
    if x_new is None or y_new is None:
        print(f"\nDivergen pada iterasi ke-{i} (nilai di dalam akar negatif)")
        break
    
    deltaX = abs(x_new - x_old)
    deltaY = abs(y_new - y_old)
    
    x, y = x_new, y_new
    
    if i <= 15 or (deltaX < epsilon and deltaY < epsilon):
        print(f"{i:<6} {x:<15.6f} {y:<15.6f} {deltaX:<15.6f} {deltaY:<15.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x:.6f}, y = {y:.6f}")
        print(f"Verifikasi: f1({x:.6f}, {y:.6f}) = {x**2 + x*y - 10:.9f}")
        print(f"           f2({x:.6f}, {y:.6f}) = {y + 3*x*y**2 - 57:.9f}")
        converged = True
        break

if not converged and x_new is not None:
    print("\nTidak konvergen dalam batas iterasi maksimum")

# METODE 2: ITERASI TITIK TETAP - SEIDEL dengan g1A dan g2A
print("\n" + "="*80)
print("METODE 2: ITERASI TITIK TETAP - SEIDEL (g1A dan g2A)")
print("="*80)
print("Fungsi iterasi:")
print("g1A: x = sqrt(10 - xy)")
print("g2A: y = sqrt((57 - y) / (3x)) [menggunakan x_baru]")
print("-"*80)

x, y = x0, y0
print(f"{'Iter':<6} {'x':<15} {'y':<15} {'deltaX':<15} {'deltaY':<15}")
print("-"*80)
print(f"{0:<6} {x:<15.6f} {y:<15.6f} {0.0:<15.6f} {0.0:<15.6f}")

converged = False
for i in range(1, max_iter + 1):
    x_old, y_old = x, y
    
    # Hitung x baru
    val_x = 10 - x_old*y_old
    if val_x <= 0:
        print(f"\nDivergen pada iterasi ke-{i} (10 - xy = {val_x} <= 0)")
        break
    x = math.sqrt(val_x)
    
    # Gunakan x baru untuk hitung y
    if abs(x) < 1e-10:
        print(f"\nDivergen pada iterasi ke-{i} (x terlalu kecil)")
        break
    val_y = (57 - y_old) / (3*x)
    if val_y <= 0:
        print(f"\nDivergen pada iterasi ke-{i} ((57-y)/(3x) = {val_y} <= 0)")
        break
    y = math.sqrt(val_y)
    
    deltaX = abs(x - x_old)
    deltaY = abs(y - y_old)
    
    if i <= 15 or (deltaX < epsilon and deltaY < epsilon):
        print(f"{i:<6} {x:<15.6f} {y:<15.6f} {deltaX:<15.6f} {deltaY:<15.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x:.6f}, y = {y:.6f}")
        print(f"Verifikasi: f1({x:.6f}, {y:.6f}) = {x**2 + x*y - 10:.9f}")
        print(f"           f2({x:.6f}, {y:.6f}) = {y + 3*x*y**2 - 57:.9f}")
        converged = True
        break

if not converged:
    print("\nTidak konvergen dalam batas iterasi maksimum")

# METODE 3: NEWTON-RAPHSON
print("\n" + "="*80)
print("METODE 3: NEWTON-RAPHSON")
print("="*80)

def f1(x, y):
    return x**2 + x*y - 10

def f2(x, y):
    return y + 3*x*y**2 - 57

def df1_dx(x, y):
    return 2*x + y

def df1_dy(x, y):
    return x

def df2_dx(x, y):
    return 3*y**2

def df2_dy(x, y):
    return 1 + 6*x*y

x, y = x0, y0
print(f"{'Iter':<6} {'x':<15} {'y':<15} {'deltaX':<15} {'deltaY':<15}")
print("-"*80)
print(f"{0:<6} {x:<15.6f} {y:<15.6f} {0.0:<15.6f} {0.0:<15.6f}")

converged = False
for i in range(1, max_iter + 1):
    u = f1(x, y)
    v = f2(x, y)
    
    du_dx = df1_dx(x, y)
    du_dy = df1_dy(x, y)
    dv_dx = df2_dx(x, y)
    dv_dy = df2_dy(x, y)
    
    det = du_dx * dv_dy - du_dy * dv_dx
    
    if abs(det) < 1e-10:
        print(f"Determinan Jacobi terlalu kecil pada iterasi ke-{i}, iterasi dihentikan")
        break
    
    x_new = x - (u * dv_dy - v * du_dy) / det
    y_new = y + (u * dv_dx - v * du_dx) / det
    
    deltaX = abs(x_new - x)
    deltaY = abs(y_new - y)
    
    x, y = x_new, y_new
    
    if i <= 20 or (deltaX < epsilon and deltaY < epsilon):
        print(f"{i:<6} {x:<15.6f} {y:<15.6f} {deltaX:<15.6f} {deltaY:<15.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x:.6f}, y = {y:.6f}")
        print(f"Verifikasi: f1({x:.6f}, {y:.6f}) = {x**2 + x*y - 10:.9f}")
        print(f"           f2({x:.6f}, {y:.6f}) = {y + 3*x*y**2 - 57:.9f}")
        converged = True
        break

if not converged:
    print("\nTidak konvergen dalam batas iterasi maksimum")

# METODE 4: SECANT
print("\n" + "="*80)
print("METODE 4: METODE SECANT")
print("="*80)
print("Catatan: Metode Secant untuk sistem persamaan menggunakan")
print("aproksimasi turunan numerik pada setiap variabel")
print("-"*80)

# Untuk metode Secant, perlu 2 tebakan awal untuk setiap variabel
x0_sec, y0_sec = 1.5, 3.5
x1_sec, y1_sec = 1.6, 3.6

print(f"{'Iter':<6} {'x':<15} {'y':<15} {'deltaX':<15} {'deltaY':<15}")
print("-"*80)
print(f"{0:<6} {x0_sec:<15.6f} {y0_sec:<15.6f} {0.0:<15.6f} {0.0:<15.6f}")
print(f"{1:<6} {x1_sec:<15.6f} {y1_sec:<15.6f} {abs(x1_sec-x0_sec):<15.6f} {abs(y1_sec-y0_sec):<15.6f}")

x_prev, y_prev = x0_sec, y0_sec
x_curr, y_curr = x1_sec, y1_sec

converged = False
for i in range(2, max_iter + 1):
    f1_prev = f1(x_prev, y_prev)
    f1_curr = f1(x_curr, y_curr)
    f2_prev = f2(x_prev, y_prev)
    f2_curr = f2(x_curr, y_curr)
    
    # Hitung x baru menggunakan aproksimasi secant untuk f1
    if abs(f1_curr - f1_prev) < 1e-10:
        df1_approx = 1.0
    else:
        df1_approx = (x_curr - x_prev) / (f1_curr - f1_prev)
    
    # Hitung y baru menggunakan aproksimasi secant untuk f2
    if abs(f2_curr - f2_prev) < 1e-10:
        df2_approx = 1.0
    else:
        df2_approx = (y_curr - y_prev) / (f2_curr - f2_prev)
    
    x_new = x_curr - f1_curr * df1_approx
    y_new = y_curr - f2_curr * df2_approx
    
    deltaX = abs(x_new - x_curr)
    deltaY = abs(y_new - y_curr)
    
    if i <= 20 or (deltaX < epsilon and deltaY < epsilon):
        print(f"{i:<6} {x_new:<15.6f} {y_new:<15.6f} {deltaX:<15.6f} {deltaY:<15.6f}")
    
    if deltaX < epsilon and deltaY < epsilon:
        print(f"\nKonvergen pada iterasi ke-{i}")
        print(f"Solusi: x = {x_new:.6f}, y = {y_new:.6f}")
        print(f"Verifikasi: f1({x_new:.6f}, {y_new:.6f}) = {f1(x_new, y_new):.9f}")
        print(f"           f2({x_new:.6f}, {y_new:.6f}) = {f2(x_new, y_new):.9f}")
        converged = True
        break
    
    x_prev, y_prev = x_curr, y_curr
    x_curr, y_curr = x_new, y_new

if not converged:
    print("\nTidak konvergen dalam batas iterasi maksimum")

print("\n" + "="*80)
print("ANALISIS KONVERGENSI")
print("="*80)
print("\n1. METODE JACOBI vs SEIDEL:")
print("   - Seidel lebih cepat konvergen karena menggunakan nilai x_baru")
print("     langsung untuk menghitung y")
print("   - Keduanya bergantung pada pemilihan fungsi iterasi yang tepat")
print("\n2. METODE NEWTON-RAPHSON:")
print("   - Konvergensi kuadratik (paling cepat)")
print("   - Memerlukan perhitungan determinan Jacobi dan turunan parsial")
print("   - Lebih stabil untuk berbagai tebakan awal")
print("\n3. METODE SECANT:")
print("   - Aproksimasi Newton-Raphson tanpa turunan eksplisit")
print("   - Konvergensi superlinear (antara linear dan kuadratik)")
print("   - Memerlukan 2 tebakan awal untuk setiap variabel")
print("\n4. PEMILIHAN FUNGSI ITERASI:")
print("   - Fungsi g1A dan g2A: x = sqrt(10-xy), y = sqrt((57-y)/(3x))")
print("   - Konvergen untuk tebakan awal yang dekat dengan solusi")
print("   - Syarat konvergen: |∂g1/∂x| + |∂g1/∂y| < 1 dan")
print("                       |∂g2/∂x| + |∂g2/∂y| < 1")
print("="*80)