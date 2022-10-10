saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
adelanto = pago_extra
#Para realizar un pago adecuado del saldo realizo
#la operacion de pagar mes siempre y cuando el saldo
#sea mayor o igual al pago_mensual


while saldo >= pago_mensual:
    if mes>=pago_extra_mes_comienzo and mes<=pago_extra_mes_fin:
        saldo = saldo * (1+tasa/12) - pago_mensual-adelanto
        total_pagado=total_pagado + pago_mensual + adelanto
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual

    print(mes," ",round(total_pagado,2)," ",round(saldo,2))
    mes=mes+1
    
#control de saldo, y adecuandolo a lo necesario
if saldo > 0:
    saldo = saldo * (1+tasa/12)
    total_pagado = total_pagado + saldo
    saldo = 0
    print(mes," ",round(total_pagado,2)," ",round(saldo,2))

print('Total pagado:', round(total_pagado, 2))
print('Meses:',mes)


