import ItemPricePulls
import time

if __name__ == '__main__':
    while True:
        try:
            ItemPricePulls.doTheThings()
            print("Data pulled.")
        except Exception as e:
            print("Trying again in 60sec: Somethin' fucked up.\n" + e)

        time.sleep(60)
    pass