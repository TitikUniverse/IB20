import csv


def main():
    csv_file = input('Введите название csv файла в вашей папке: ')
    st_pers_data = input('Введите название столбца в csv файле, который отвечает за перс данные: ')
    slov_data = input('Введите название словаря данных: ')

    try:
        t = int(input('Что вы хотите сделать: '))
    except:
        print('0_0 что-то пошло не так')
    opportunities(t, csv_file, st_pers_data, slov_data)


def opportunities(t, csv_file, st_pers_data, slov_data):
    if t == 1:
        print('Введите данные, на которые хотите заменить')
        fio = input('Введите ФИО через пробел: ')
        phone = input('Введите телефон в формате 8...: ')
        address = input('Введите адрес в формате улица дом: ')
        w = fio + ", " + phone + ", " + address

        string = int(input('Введите номер строчки, не считая оглавление и начиная с 1: '))

        try:
            with open(csv_file, "r", newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                e, q, kl = 0, [], []
                for row in reader:
                    q.append([])
                    if e == string - 1:
                        for i in row.keys():
                            kl.append(i)
                            if i != st_pers_data:
                                q[e].append(row[i])
                            else:
                                q[e].append(w)
                    else:
                        r = []
                        for i in row.keys():
                            r.append(row[i])
                        q[e] = r
                    e += 1
            q.insert(0, kl)
            if q:
                with open(csv_file, 'w', newline="") as csvfile:
                    writer = csv.writer(csvfile, delimiter=';')
                    for i in range(len(q)):
                        h = q[i]
                        writer.writerow(h)
        except:
            print('0_0 что-то пошло не так')
    elif t == 2:
        e = []
        try:
            string = int(input('Введите номер строчки, не считая оглавление и начиная с 1: '))

            with open(csv_file, "r", newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                e, q = 0, []
                for row in reader:
                    kl = []
                    for i in row.keys():
                        kl.append(i)
                    q.append([])
                    r = []
                    for i in row.keys():
                        r.append(row[i])
                    q[e] = r
                    e += 1
            q.insert(0, kl)
            f = q[0].index(st_pers_data)
            u = []
            u.append([])
            for i in q[0]:
                if i == st_pers_data:
                    u[0].append("fio")
                    u[0].append("name")
                    u[0].append("patronymic")
                else:
                    u[0].append(i)
            for i in range(1, len(q)):
                d = q[i]
                g = d[f]
                o = []
                fio = g.split(',')[0].strip()
                phone = g.split(',')[1].strip()
                address = g.split(',')[2].strip()
                print(fio)
                print(phone)
                print(address)
                for p in q[i]:
                    if q[i].index(p) == f:
                        o.append(fio)
                        o.append(phone)
                        o.append(address)
                    else:
                        o.append(p)
                u.append(o)

            if q:
                with open(csv_file, 'w', newline="") as csvfile:
                    writer = csv.writer(csvfile, delimiter=';')
                    for i in range(len(u)):
                        s = u[i]
                        writer.writerow(s)
        except:
            print('0_0 что-то пошло не так')
    else:
        print('Такого действия не существует, наверное вы что-то перепутали!')
        print('Попробуйте снова!')


if __name__ == "__main__":
    main()