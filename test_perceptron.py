# Perceptron
[-15000.0, -30000.0, -45000.0, 60000.0, 465000.0, 150000.0, 0.0, 0.0, 15000.0, 0.0, -135000.0, -270000.0, 0.0, -15000.0, 240000.0, -30000.0, 0.0, 15000.0, -15000.0, -135000.0, -135000.0, 375000.0, -15000.0, 225000.0, 165000.0, 0.0, 0.0, 0.0, -135000.0, 315000.0, 45000.0, 90000.0, -180000.0, 450000.0, 15000.0, 15000.0, -15000.0, -150000.0, 270000.0, -180000.0, -210000.0, -60000.0, 480000.0, 30000.0, 15000.0, -15000.0, 285000.0, 150000.0, 150000.0, 240000.0, 105000.0, 330000.0, 450000.0, 0.0, 0.0, 405000.0, -75000.0, 15000.0, 45000.0, -180000.0, 60000.0, 540000.0, 30000.0, 405000.0, 45000.0, -150000.0, -270000.0, -300000.0, -150000.0, 15000.0, 390000.0, 195000.0, 495000.0, -60000.0, -120000.0, -240000.0, -150000.0, -60000.0, 60000.0, 75000.0, 495000.0],
[15000.0, 30000.0, 30003.5, 68842.0, -18854.5, 12651.5, 0.0, 0.0, 0.0, 15000.0, 30088.0, 15107.0, 71279.5, -4436.5, 45018.5, 45000.0, 0.0, 0.0, 15000.0, 38918.0, 15019.0, 66688.0, -51722.0, -3754.0, 42651.5, 0.0, 0.0, 15000.0, 30088.5, -18838.0, 51157.5, -27655.5, 2451.5, 14956.0, -4456.5, 0.0, 15000.0, 45088.5, -8264.5, 70661.0, 77397.5, -12567.5, -33856.0, -11187.5, 0.0, 15000.0, -23199.5, -27825.5, 77161.5, -12840.0, -27820.5, 17075.0, -60019.0, 0.0, 0.5, -44955.0, -4444.5, 55538.5, -49455.0, 10644.5, 10538.0, -75043.5, -4456.5, -48828.5, 3870.0, 20.0, 150011.5, 60102.5, 75037.5, -14998.0, -51191.5, -23855.5, -60023.5, 70.5, 93.5, 105095.0, 90036.0, 45004.5, -59998.0, -30017.5, -60024.0]

w = {
    'A': [-15000.0, -30000.0, -45000.0, 60000.0, 465000.0, 150000.0, 0.0, 0.0, 15000.0, 0.0, -135000.0, -270000.0, 0.0, -15000.0, 240000.0, -30000.0, 0.0, 15000.0, -15000.0, -135000.0, -135000.0, 375000.0, -15000.0, 225000.0, 165000.0, 0.0, 0.0, 0.0, -135000.0, 315000.0, 45000.0, 90000.0, -180000.0, 450000.0, 15000.0, 15000.0, -15000.0, -150000.0, 270000.0, -180000.0, -210000.0, -60000.0, 480000.0, 30000.0, 15000.0, -15000.0, 285000.0, 150000.0, 150000.0, 240000.0, 105000.0, 330000.0, 450000.0, 0.0, 0.0, 405000.0, -75000.0, 15000.0, 45000.0, -180000.0, 60000.0, 540000.0, 30000.0, 405000.0, 45000.0, -150000.0, -270000.0, -300000.0, -150000.0, 15000.0, 390000.0, 195000.0, 495000.0, -60000.0, -120000.0, -240000.0, -150000.0, -60000.0, 60000.0, 75000.0, 495000.0],
    'B': [15000.0, 30000.0, 30003.5, 68842.0, -18854.5, 12651.5, 0.0, 0.0, 0.0, 15000.0, 30088.0, 15107.0, 71279.5, -4436.5, 45018.5, 45000.0, 0.0, 0.0, 15000.0, 38918.0, 15019.0, 66688.0, -51722.0, -3754.0, 42651.5, 0.0, 0.0, 15000.0, 30088.5, -18838.0, 51157.5, -27655.5, 2451.5, 14956.0, -4456.5, 0.0, 15000.0, 45088.5, -8264.5, 70661.0, 77397.5, -12567.5, -33856.0, -11187.5, 0.0, 15000.0, -23199.5, -27825.5, 77161.5, -12840.0, -27820.5, 17075.0, -60019.0, 0.0, 0.5, -44955.0, -4444.5, 55538.5, -49455.0, 10644.5, 10538.0, -75043.5, -4456.5, -48828.5, 3870.0, 20.0, 150011.5, 60102.5, 75037.5, -14998.0, -51191.5, -23855.5, -60023.5, 70.5, 93.5, 105095.0, 90036.0, 45004.5, -59998.0, -30017.5, -60024.0]
}

b_w = [300000, 120130]


datas = open('test_data', 'r').read().split('\n')
test_data = []
true_test = []
for i in datas:
    test_data.append((i[0], i[1:]))

for i in test_data:
    print '*'*50
    conv = map(lambda x: float(x) if float(x) > 0 else -1, [char for char in i[1]])
    a = b_w[0]+sum([x*y for x,y in zip(w['A'],[float(num) for num in i[1]])])
    b = b_w[1]+sum([x*y for x,y in zip(w['B'],[float(num) for num in i[1]])])

    print "Test with A: {}".format(a)
    print "Test with B: {}".format(b)
    print "Target: {} >< Result {}".format(i[0], 'A' if a>b else 'B')

    if (a>=b and i[0] == 'A') or (a<b and i[0]=='B'):
        true_test.append(1)
    else:
        true_test.append(0)

print '*'*50
print "Validity: {}%".format((sum(true_test)*1.0/len(true_test)*1.0)*100)
