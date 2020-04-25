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
export AWS_ACCESS_KEY_ID=AKIAYRRLVZLV62SEX4VN &&
export AWS_SECRET_ACCESS_KEY=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
```

##### Create user with credentials and permisions

```
aws_manager -u user -r eu-west-1 -p admin -id 587428383467
```
### Delete user

```
aws_manager -u user -r eu-west-1 -p admin -id 587428383467 -d delete
```
