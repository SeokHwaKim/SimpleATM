from modules.Mod_Card.Mod_Card import Mod_Card
from modules.Mod_Bank.Mod_Bank import Mod_Bank
from modules.Mod_Account.Mod_Account import Mod_Account
from modules.Mod_Balance.Mod_Balance import Mod_Balance

import json
import logging
import re

def main():
    print("=====================================")
    print("= \t\tStart ATM Service\t\t =")
    print("=====================================")
    while True:
        print("=====================================")
        print("= \t\tSimple ATM System\t\t =")
        print("=====================================")
        print("=\t\t\tInput command\t\t  =")
        print("=\t\t\t1.Insert Card\t\t  =")
        print("=\t\t\t2.Tset ATM\t\t\t  =")
        print("=\t\t\t3.Exit ATM\t\t\t  =")
        cmd = input()
        mod_card = Mod_Card()
        if cmd == "1":
            print("=\t\t\tWaiting Insert Card\t\t=")
            print("=====================================")
            print("=\t\t\tNot Support Now\t\t  =")
            print("=====================================")

        elif cmd == "2":
            with open("test_data/cardData.json") as f:
                card_data = json.load(f)
            f.close()
            if mod_card.read_card(card_data) is False:
                logging.error("ATM - Card data load failed")
                continue

            card = mod_card.get_card()
            if card is None:
                logging.error("ATM - Card get failed")
                continue
            mod_bank = Mod_Bank(card)
            print("=\t\t\tShow Card\t\t\t=")
            print("=====================================")
            mod_card.dump_card()

            card_bank = card.get_bank_info()
            if mod_bank.check_card_in_banks(card_bank.get_bank_serial()) is False:
                logging.error("ATM - Card not in bank")
                continue
            print("=\t\tInsert Your PIN Number\t\t=")
            print("=====================================")
            pin = input()
            if mod_bank.check_pin(pin) is False:
                logging.error("ATM - PIN number was wrong")
                continue
            else:
                print("= Hi {}, Show Your Account =".format(card.get_person().get_name()))
                print("=====================================")

            card_serial = card.get_card_serial()

            mod_account = Mod_Account(card)
            if mod_account is None:
                logging.error("ATM - Account load failed")
                continue
            mod_account.load_account(card_serial)
            mod_account.dump_accounts()
            print("=\t\t\tChoice Account\t\t\t=")
            print("=====================================")

            account_idx = str(input())
            for i in range(0, 3):
                if re.match("[0-9]+", account_idx):
                    account = mod_account.choice_account(int(account_idx))
                    if account is not False:
                        break
                print("=   \t\tAccount Idx Wrong\t\t=")
                print("=\t\t\tChoice Account\t\t\t=")
                print("=====================================")
                account_idx = str(input())

            while True:
                print("=\t\t\tChoice Action\t\t\t=")
                print("=\t\t\t1. Shows Balance\t\t=")
                print("=\t\t\t2. Deposit Balance\t\t=")
                print("=\t\t\t3. Withdraw Balance\t\t=")
                print("=\t\t\t4. Exit\t\t\t\t\t=")
                action_idx = str(input())
                for i in range(0, 3):
                    if re.match("[0-9]+", action_idx) and ( 1 <= int(action_idx) <= 4 ):
                        if account is not False:
                            break
                    print("=   \t\tAction Wrong\t\t=")
                    print("=\t\t\tChoice Action\t\t\t=")
                    print("=====================================")
                    action_idx = str(input())
                mod_balance = Mod_Balance(card, account)

                if int(action_idx) == 1:
                    mod_balance.dump_account()
                elif int(action_idx) == 4:
                    card.clear()
                    mod_balance.clear()
                    mod_account.clear()
                    mod_bank.clear()
                    mod_card.clear()
                    print("=\t\t\tExit \t\t\t\t\t=")
                    print("=====================================")
                    break
                else:
                    print("=\t\t\tInsert Money\t\t\t=")
                    print("=====================================")
                    money = input()
                    if not re.match("[0-9]+", money):
                        print("=\t\t\tMoney Wrong\t\t\t\t=")
                        print("=====================================")
                        continue

                    if int(action_idx) == 2:
                        if mod_balance.deposit_balance(money) is True:
                            print("=   \t\tDeposit Success\t\t=")
                            print("=====================================")
                    elif int(action_idx) == 3:
                        if mod_balance.withdraw_balance(money) is True:
                            print("=   \t\tWithdraw Success\t\t=")
                            print("=====================================")
                    mod_balance.dump_account()

if __name__ == '__main__':
    main()
