# PyMailers
The classic email sending library for Python.

## Installation
Start to do the installation.
```bash
pip install pymailers
```

## Example
A simple example is just sending an email message with PyMailer, in **display** you can replace it with **false** then it will not get any logs but if it is made **true** then you will get a log after sending the email message.

```python
from pymailers.PyMailer import PyMailer

pymailer = PyMailer({
  'smtp_host': 'smtp.gmail.com',
  'smtp_port': 587,
  'email': 'xxxxx@gmail.com',
  'password': 'xxxxxxxxxx',
  'to': 'xxxxx@gmail.com',
  'subject': 'Hello World',
  'body': '<p>Hi im Rio</p>',
  'display': True
})

pymailer.send()
```

## Donate
- [Saweria](https://saweria.co/rioagungpurnomo)
- [Trakteer](https://trakteer.id/rioagungpurnomo)
- [PayPal](https://www.paypal.me/rioagungpurnomoo)

## Contact me
Contact me via email: rioagungpurnomo@programmer.net, I'm waiting for your input or suggestions.
