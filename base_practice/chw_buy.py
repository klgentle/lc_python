all_goods_and_deliver = 4866.02
au_goods_and_deliver = 998.45
au_deliver = 66.81
print(f"CHW营养品总价及运费(第一次):￥ {all_goods_and_deliver}, 澳元原价: {au_goods_and_deliver}")
rmb_deliver2 = 74.33 * 4 + 87.45
print(f"澳州转运费:￥ {rmb_deliver2}")
all_fee = all_goods_and_deliver + rmb_deliver2

rate = all_goods_and_deliver / au_goods_and_deliver

print(f"利率：{rate}")
dha_price = 28.99
black_price = 29.99
vd_price = 13.99
print(f"DHA单价(AU):{dha_price}, black单价(AU): {black_price}, VD单价(AU): {vd_price}")

ryq_good = [10, 2, 2]
xz_good = [10, 6, 6]
print(f"饶奕钦营养品数量：DHA * {ryq_good[0]}, black * {ryq_good[1]}, VD * {ryq_good[2]}")
print(f"肖珍营养品数量：DHA * {xz_good[0]}, black * {xz_good[1]}, VD * {xz_good[2]}")

ryq_good_au_value = ryq_good[0] * dha_price + ryq_good[1] * black_price + ryq_good[2] * vd_price
xz_good_au_value = xz_good[0] * dha_price + xz_good[1] * black_price + xz_good[2] * vd_price
ryq_good_rmb_value = ryq_good_au_value * rate
xz_good_rmb_value = xz_good_au_value * rate
print(f"饶奕钦营养品价值：￥{ryq_good_rmb_value:.2f}, 澳元价值：{ryq_good_au_value}")
print(f"肖珍营养品价值：￥{xz_good_rmb_value:.2f}, 澳元价值：{xz_good_au_value}")


ryq_deliver = au_deliver * rate / 2  + 74.33 + 87.45
xz_deliver = au_deliver * rate / 2  + 74.33 * 3
print(f"饶奕钦运费：￥{ryq_deliver:.2f}")
print(f"肖珍运费：￥{xz_deliver:.2f}")

ryq_good_add_fee = ryq_good_rmb_value + ryq_deliver
xz_good_add_fee = xz_good_rmb_value + xz_deliver

print(f"饶奕钦营养品加运费：￥{ryq_good_add_fee:.2f}")
print(f"肖珍营养品加运费：￥{xz_good_add_fee:.2f}")

assert( all_fee == ryq_good_add_fee + xz_good_add_fee)
