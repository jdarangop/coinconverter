# coinconverter
API for converting denominations between different cryptocurrencies

### Quickstart

First you have to clone this repository by typing this command in the console:

  `$ git clone https://github.com/jdarangop/coinconverter.git`

Then it is good to use a virtual environment to be able to configure
the requirements, for this you can use the virtualenv library

  `$ pip install virtualenv`

And then, create a virtual environment and activate it:

  `$ python3 -m venv coinconverter_env`
  `$ source coinconverter_env/bin/activate`

Now we can install the requirements within the virtual environment:

  `$ pip install -r requirements.txt`

---

To run the api:

  `$ python3 app.py`

Or simply, run the app.py file:

  `$ ./app.py`
  
Then we can open another terminal and make GET requests to our API,
the API support the following endpoint format: ´/converter?input_coin=$(Choose an input coin)&amount=$(Amount to convert)&output_coin=$(Choose the final currency)´

An example of a GET request:

  `$ curl -X GET 0.0.0.0:5000/converter?input_coin=ETC&amount=335&output_coin=BTC`

---
      
Finally, to run the unit tests, you can use the following command:

  `$ python3 -m unittest test.test_api`

  `$ python3 -m unittest test.test_converter`