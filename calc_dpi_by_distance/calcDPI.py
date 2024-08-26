def get_distance_from_user():
    while True:
        try:
            distance = float(
                input("> Input the distance (in centimeters) which the image will be seen: \n "))
            if distance <= 0:
                print("The distance should be a positive number")
            else:
                return distance
        except ValueError:
            print("Please, insert a valid number")


def calc_dpi(distance_cm):
    distance_inch = distance_cm / 2.54
    dpi = 1 / ((distance_inch * 0.000291) / 2)
    return int(dpi)


def main():
    distance = get_distance_from_user()
    min_dpi = calc_dpi(distance)
    print(f"The minimum DPI for an image is: {min_dpi}")


if __name__ == "__main__":
    main()
