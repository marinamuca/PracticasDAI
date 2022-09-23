# Expresiones regulares

# Identificar cualquier palabra seguida de un espacio y una única letra mayúscula
"[a-zA-Z]*\s[A-Z][a-zA-Z]*"

# Identificar correos electrónicos válidos
"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

# Identificar números de tarjeta de crédito cuyos dígitos estén separados por - o espacios en blanco cada paquete de cuatro dígitos: 1234-5678-9012-3456 ó 1234 5678 9012 3456.
"([0-9]{4}(\s|-)){3}[0-9]{4}"