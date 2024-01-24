from im_packages.decor import my_decor


@my_decor
def kvadrat():
    for i in range(50):
        print(i ** 2)


kvadrat()
