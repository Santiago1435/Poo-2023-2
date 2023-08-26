horas = 48
valor_horas = 5000
retencion = 0.125

salario_bruto = round(horas * valor_horas)
retencion_valor = round(salario_bruto * retencion)
salario_neto = round(salario_bruto - retencion_valor)

print(f"Salario bruto es:{salario_bruto}")
print(f"Salario neto es:{salario_neto}" )
print(f"Retencion es:{retencion_valor}")