import csv
from os import path

#csv_filename = r"c:\Users\Денис\AppData\Local\Temp\cars.csv"

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        self.photo_file_name = path.splitext(self.photo_file_name)[1]
        return self.photo_file_name


class Car(CarBase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_file_name, carrying):
        super(Car, self).__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, body_whl, carrying):
        super(Truck, self).__init__(car_type, brand, photo_file_name, carrying)
        self.body_width = self.body_height = self.body_length = 0.0


        if body_whl == '':
            self.body_width = self.body_height = self.body_length = 0.0
        else:
            body_parametr = body_whl.split('x')
            self.body_length = float(body_parametr[0])
            self.body_width = float(body_parametr[1])
            self.body_height = float(body_parametr[2])

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length

class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super(SpecMachine, self).__init__(car_type, brand,photo_file_name,carrying)
        self.extra = extra

def get_car_list(csv_filename):
    #csv_filename
        car_list = []
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)
            for row in reader:
                if len(row) == 7:
                    car_type = row[0]
                    brand = row[1]
                    passenger_seats_count = row[2]
                    photo_file_name = row[3]
                    body_whl = row[4]
                    carrying = row[5]
                    extra = row[6]
                    try:
                        if car_type == 'car':
                            if brand != '' and passenger_seats_count != '' and photo_file_name != '' and carrying != '':
                                car = Car(car_type, brand, passenger_seats_count,photo_file_name,carrying)
                                car_list.append(car)
                                #print (car.car_type, car.brand,car.photo_file_name,car.passenger_seats_count,car.carrying)
                        elif car_type == 'truck':
                            if brand != '' and photo_file_name != '' and carrying != '':
                                truck = Truck(car_type, brand, photo_file_name, body_whl,carrying)
                                car_list.append(truck)
                                print (type(truck.body_width))
                                #print (truck.car_type,truck.brand,truck.photo_file_name,truck.body_width,truck.body_height,truck.body_length,truck.carrying)
                        elif car_type == 'spec_machine':
                            if brand != '' and photo_file_name != '' and carrying != '' and extra != '':
                                spmachine = SpecMachine(car_type, brand, photo_file_name, carrying, extra)
                                car_list.append(spmachine)
                                #print (spmachine.brand,spmachine.photo_file_name,spmachine.carrying,spmachine.extra)
                    except IndexError as err:
                        return('Конец файла!',err)
            return car_list


if __name__ == "__main__":
   get_car_list(csv_filename)