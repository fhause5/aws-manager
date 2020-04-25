<span style="color: blue">&#x1F535; AWS manager </span>

##### The python scripts for AWS

Installing

```
cd aws-manager

Create the virtualenv

pipenv install --python python3.7

Activate the virtualenv.


pipenv shell

Install the tool and make it editable.

pip install -e .

```
> Please DO NOT FORGET export ENV VARIABLES !!!

```
export AWS_ACCESS_KEY_ID= &&
export AWS_SECRET_ACCESS_KEY=
```

##### Create user with credentials and permisions

```
aws_manager -u user -r eu-west-1 -p admin -id 58742666467
```
### Delete user

```
aws_manager -u user -r eu-west-1 -p admin -id 587428666467 -d delete
```
