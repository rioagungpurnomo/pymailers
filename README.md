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
<a href="https://trakteer.id/rioagungpurnomo" target="_blank"><img id="wse-buttons-preview" src="https://cdn.trakteer.id/images/embed/trbtn-red-6.png" height="40" style="border:0px;height:40px;" alt="Trakteer Saya"></a>

Paypal : **[Support me](https://www.paypal.me/RioDev)**

## Contact me
Contact me via email: rioagungpurnomo.ak@gmail.com, I'm waiting for your input or suggestions.
