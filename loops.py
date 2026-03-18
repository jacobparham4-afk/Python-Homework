def main():
    muffins = 10
    cupcakes = 10

    while True:
        item = input("Enter item (muffin, cupcake) or 0 to stop: ")

        if item == "0":
            break

        elif item == "muffin":
            if muffins > 0:
                muffins -= 1
            else:
                print("Out of stock")

        elif item == "cupcake":
            if cupcakes > 0:
                cupcakes -= 1
            else:
                print("Out of stock")

        else:
            print("Invalid item")

    print(f"muffins: {muffins} cupcakes: {cupcakes}")


if __name__ == "__main__":
    main()