calificacion = 10
color = None

#modo normal
"""
if calificacion >= 7:
    color = 'Verde'
else:
    color = 'Rojo'
"""

#modo terniario
color = 'Verde' if calificacion >= 7 else 'Rojo'
print(calificacion, color)