if __name__ == '__main__':
    n = int(input().strip())

    if 1 <= n <= 100:
        if n % 2 != 0:
            print('Weird')

        else:
            if n in range(2, 5):
                print("Not Weird")

            elif n in range(6, 21):
                print("Weird")

            else:
                print("Not Weird")
    else:
        print("Number Not Allowed!")
