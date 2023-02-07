from lib import emit_portfolio_update, emit_price_update
from termcolor import colored
from tqdm import tqdm
import time, os
from multiprocessing import Process
def main_process():
    last_net = 0
    while True:
        try:
            _net = float(emit_portfolio_update())
            if _net > last_net:
                print(colored("Portfolio Value: "+ str(_net)+ " CHF", "green"))
            elif _net < last_net:
                print(colored("Portfolio Value: ", str(_net)+ " CHF", "red"))
            else:
                print(colored("Portfolio Value: "+ str(_net)+ " CHF", "yellow"))
            last_net = _net

        except Exception as Req_Limit:
            print('[E]: Request limit exceeded')

        interval = 60*60
        timer = tqdm(total=interval)
        for i in range(0, interval):
            time.sleep(1)
            timer.update(1)
        time.sleep(0.1)
        timer.close()
        os.system('clear')
def casper_process():
    while True:
        emit_price_update('casper-network')
        time.sleep(10*60)
if __name__ == '__main__':
    mp = Process(target=main_process)
    mp.start()
    casper_process()
    mp.join()
