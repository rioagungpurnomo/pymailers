# PyMailer
The classic email sending library for Python.

## Example
A simple example is just sending an email message with PyMailer, in **display** you can replace it with **false** then it will not get any logs but if it is made **true** then you will get a log after sending the email message.

```python
from PyMailer import PyMailer

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
Help me to buy a laptop because my laptop is broken and I don't have a laptop, I only use an Android phone to make works like this even though it's difficult, your help and donations are a great encouragement for me to continue working.

Link : **[Donate](https://trakteer.id/rioagungpurnomo)**

## Contact me
Contact me via email: rioagungpurnomo.ak@gmail.com, I'm waiting for your input or suggestions.
