medida = float(input('Digite uma distância em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000

print('A medida de {} m corresponde a: \n{} cm \n{} mm \n{} dm'.format(medida, cm, mm, dm))
print('{} dam \n{} hm \n{} km'.format(dam, hm, km))
