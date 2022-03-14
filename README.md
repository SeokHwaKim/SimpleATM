##Simple ATM
####Created By "Seokhwa Kim"

###Desription
This project shows the simple ATM program by python3

---
###Environment
- Python 3.10
- PyCharm 2021.3.2
---
###Usage
1. Open project on pycharm
2. Set to the right python interpreter
3. Open main.py file
4. run
---
###Test Run
1. Open test_main.py file
2. run
---
###Project Structure
```bash
├── modules
│   ├── Mod_Account
│   ├── Mod_Balance 
│   └── Mod_Bank
│   └── Mod_Card
├── obj #── object 
│   ├── Account
│   ├── Bank
│   ├── Card
│   └── CardCompany
│   └── PersonalIfno
├── test_src
│   ├── test_data
│   ├── test_mod #── modules test codes  
│   ├── test_obj #── object test codes 
│   └── test_main.py
└── main.py
``` 
---
###ATM Definition
1. A process of converting json from real card was processed by ATM Hardward.
2. A real bank system is unknown, so Account/Banking data were replaced to Json Data
3. Currently, I cannot have a data corresponding to real card data. It was replaced to Json Data
---
###Example Data Format
Card Data Format

    {
    "card_name":"NarasarangCard",
    "card_serial":"1222023",
    "card_company":{
                        "company_name":"ShinHanCard",
                        "company_serial":3
                    },
    "card_bank":{
                    "bank_name":"ShinhanBank",
                    "bank_serial":3
                },
    "card_person":{
                    "person_name":"SeokhwaKim",
                    "person_serial":"01091732725"
                    }
    }
---
Bank Data Format

    {
    "bank_list": {
            "3": [
                "1222023",
                "2233034"
            ],
            "4": [],
            "5": [
                "9923435"
            ]
        }
    }
---
Account List Data Format

    {
    "card_list": {
        "1222023": [
        {
            "account_serial":"99173272543",
            "account_balance":30000
        },
        {
            "account_serial":"01091732725",
            "account_balance":50000
        },
        {
            "account_serial":"91732725",
            "account_balance":10000
        }
        ]
    }
    }