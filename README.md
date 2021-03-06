# RDT-Django-round

## Introduction
    The RDT-Django project contains two Apis:
        1. Returns percentage changes of company stock on each day
        2. Top 5 volumes of Microsoft company

## Deployment spets

> 1. Crete a virtual environment
> 2. Clone the Repo
> 3. Run "pip install -r requirements.txt"
> 4. copy the database to the project folder
> 5. Install & route nginx to project static folder
> 6. Install & run gunicorn
> 7. Install supervisor & Configure

    Note: The Configuration Files are included in '.config_files' folder

## Running Steps

> ### 1. Percentage Changes of company stock
    url: /analysis/percentages/

    method: POST

    Input:
        {"name":"Microsoft"}

    Sample Response:
        [
            {
                "stock_open": "71.50",
                "stock_close": "71.77",
                "date": "July 13, 2017",
                "change": "0.38"
            },
            {
                "stock_open": "70.69",
                "stock_close": "71.15",
                "date": "July 12, 2017",
                "change": "0.65"
            },
            {
                "stock_open": "70.11",
                "stock_close": "69.99",
                "date": "July 11, 2017",
                "change": "-0.17"
            }
        ]
> ### 2. Top 5 stock volumes of Microsoft
    url: /analysis/topvolumes/

    method: POST

    Input:
        {"name":"Microsoft"}

    Sample Response:
        [
            {
                "date": "March 17, 2017",
                "Volume": "4,92,19,686"
            },
            {
                "date": "June 09, 2017",
                "Volume": "4,91,87,396"
            },
            {
                "date": "June 16, 2017",
                "Volume": "4,83,45,085"
            },
            {
                "date": "June 12, 2017",
                "Volume": "4,77,61,743"
            },
            {
                "date": "February 02, 2017",
                "Volume": "4,58,27,013"
            }
        ]
