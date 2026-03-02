import sympy as sp

# 1. Definimos el símbolo y la fórmula
Vb = sp.symbols('Vb')
neto_expr = Vb + (0.19 * Vb) - (0.10 * Vb)

# 2. Pedimos el valor al usuario
entrada = input("¿Cuánto vas a cobrar? (valor bruto): ")
valor_real = float(entrada)

# 3. SymPy hace la magia: simplifica y calcula
formula_final = sp.simplify(neto_expr)
resultado = neto_expr.subs(Vb, valor_real)

print(f"La fórmula que SymPy simplificó es: {formula_final}")
print(f"Tu pago neto real es: ${resultado:,.0f} COP")