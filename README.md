# meetup121219
Tools to write clean microservices in python without headaches. (demo project)

This project is a demo project you can use as microservice project template.
This project is using django ORM and connexion (flask) framework combined together.
You can find below all the things you can do with this project template.

## Project scructure
    .
    ├── apps
    │   ├── boilerplace
    │   │   ├── migrations
    │   ├── db
    │   │   ├── migrations
    ├── codegen_template
    ├── docs
    ├── locale
    ├── requirements
    ├── scripts
    ├── settings
    └── swagger_server
        ├── controllers
        ├── functions
        ├── models
        ├── openapi
        ├── repositories
        ├── serializers
        ├── stories
        └── tests

**apps** is a directory containing our django apps

**apps/boilerplace** a django app containing our custom user model

**apps/db** as we are using django ORM with connexion this app contains all project related db models

**codegen_template** the template we are using for code generation

**docs** the place where our api first specification is

**locale** the i18n po and mo files folder

**requirements** our project python requirements files

**scripts** this directory contains curstom scripts for convenience

**swagger_server** the root directory of connexion framework

**swagger_server/controllers** where connexion (flask) controller belongs

**swagger_server/functions** Where all utils functions belongs

**swagger_server/models** Where generated view models (api related models, not db models) belongs

**swagger_server/openapi** Where generated version of specification belong (with various things added like operationId... etc.)

**swagger_server/repositories** A layer between django models and our business code to help us switching from django ORM to anything else later.

**swagger_server/serializers** This is a convenient layer to generate a view model from a django model when fields are the same in both of them.

**swagger_server/stories** Where business transaction belongs (using dry-python/stories https://github.com/dry-python/stories)

**swagger_server/tests** Where tests and test framework fixtures configuration belongs

All of those layers are injected inside a "container" class using dependencies python library (https://github.com/dry-python/dependencies)

Those containers are defined inside the implemented.py file.
Then, those container classes can be used inside controllers.

## What is included ?
* Full features python test framework (with coverage, html report and testing on various python verions)
* Lint tools (flake8 and isort)
* Performance analysis tool (py-spy running on top of the test framework)
* i18n
* Code duplication analyser
* Dependency injection and business transaction the awesome dry-python's stories and dependencies python libraries
* Swagger ui
* Generate db er-diagram
* Other convinient scripts...

## Requirements
* yarn
* python3.6+
* sqlite
* pew
* pmd (https://pmd.github.io/)

### Before first run, execute those commands
* Create new python virtualenv for project deps
```bash
pew new --python=python3.7 meetup121219
```
* Install python dependencies in virtualenv
```
    pew in meetup121219 pip install -r requirements/requirements.txt
```
* Install node dependencies (for codegem)
```bash
yarn
```
* Migrate database
```bash
npm run db:migrate
```

## Use this project without jwt key for test purpose
If your code is running in debug we have implemented fake users in fake_user_if_fake_jwt_token function in swagger_server/functions/auth.py file.

Examples of token payload can be found inside this method.

In swagger ui or using an http client those values can be used as fake users :
- super_user
- staff_user
- standard_user
- unverified_standard_user
- blocked_standard_user

## How to... ?

As you will see this project use npm as a task runner to make various tasks available.

### Start server
```npm run dev```

### Lint code
```npm run flake8```
Find pep8 violations & other things.

### Reformat imports automatically
```npm run isort```

### Add python coding utf8 everywhere missing
```npm run fix:coding```

### Fix endl everywhere needed
```npm run fix:endl```

### Find duplicated code
```npm run cpd```
Needs $PMD_BIN to be set correctly (bin directory of pmd where run.sh script is).
Generates report called cpd_report.html

### Generate view models, dummy controllers & spec to be used to run the server (the same spec but with operationId & things like this...)
```npm run generate```
Then:
  - Copy generated/swagger_server/models/*.py to swagger_server/models/
  - Copy new controller functions to the right corresponding file
  - Forget everything else. (it is mostly useless)

Remark:
  We have customize the code-generation template to wrap controllers with a login_required wrapper.
  This wrapper extract user info from the token to create a user object
  to be used by django guardian or other django apps.

### Use swagger ui
Go to 127.0.0.1:5000/v1/ui

### Run tests
```npm run test```
Will run only last failed test by default.

```npm run test:all```
Will run all existing tests from tests directory (swagger_server/tests)

```npm run test:tox```
Will run all tests on python3.6 and python3.7

```npm run test:cdb```
'cdp' means create db.
Will re-create test db before running tests.

```npm run test:vv```
Run pytest in very verbose mode.

```npm run test:withprof```
Run pytest with py-spy to generate a flamegraph

```npm run test:nocov```
Run pytest and do not generat a coverage report.

### Find coverage info
After running `npm run test:all`, coverage report can be found in *htmlcov* directory (firefox index.html).

### Extract i18n strings from code
```npm run i18n:extract```
Extract strings to *locale* directory.

### Translate strings
Open django.po files from locale directory with poedit (https://poedit.net/)

### Make django or flask using translated strings
```npm run i18n:build```
Generates *.mo files to be used by django for translations.

### Grenerate db er-diagram
```npm run db:erdiagram```
Generates er_diagram.png file.

