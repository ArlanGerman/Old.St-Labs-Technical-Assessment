# Employee System

Written by Arlan Vincent John German as for the Old St Technical Assessment. This system allows the user to perform the following tasks:

 - Create new Employees
 - Edit existing Employees
 - Delete an existing Employees
 - List all Existing Employees order by the monthly salary descending order
 - List all Existing Employees order by the date of birth descending order
 - List all Existing Employees order by First name and Last name ascending
order

## Prerequisites
Your system must have **Python** (version >= 3.10.4) and **pip** (version >= 22.1.1) installed prior to the installation.

## Installation

A requirements.txt is provided for the needed libraries, simply run

    pip install -r requirements.txt



## Running locally

First, we have to make sure the local database is ready. Hence, we need to run the following first:

    python manage.py makemigrations
    python manage.py migrate

Afterwards, we can locally run the Django application by running the following:

    python manage.py runserver

You can confirm that the application is running when it gives the message: *'Starting development server at http://127.0.0.1:8000/'*. The default address and port that Django uses are localhost (e.g., 127.0.01) and 8000, respectively.

# API Documentation

This is the official API documentation for the Employee system written by Arlan Vincent John German.

## Adding a new employee

You can add a new employee by either visiting the default endpoint stated (i.e., http://127.0.0.1:8000/), or by sending a POST request to the default endpoint with a JSON or form-data body of format:

    {
	    "first_name": "<First Name>",
	    "last_name": "<Last Name>",
	    "birth_date": "<Date format: YYYY-MM-DD>",
	    "monthly_salary": <Salary>,
	    "status": "<ACTIVE or INACTIVE>"
    }

If your request was successful, you should receive a 201 Created Response with the following body:

    {
	    "employee_id": "<Employee ID>",
	    "first_name": "<First Name>",
	    "last_name": "<Last Name>",
	    "birth_date": "<Date format: YYYY-MM-DD>",
	    "monthly_salary": <Salary>,
	    "status": "<ACTIVE or INACTIVE>"
    }

## Edit an existing employee's info

You can edit an existing employee's info by either visiting the endpoint stated with the employee's id number (i.e., http://127.0.0.1:8000/<employee_id>/), or by sending a PATCH request to the same endpoint with a JSON or form-data body of format:

    {
	    "first_name": "<First Name>",
	    "last_name": "<Last Name>",
	    "birth_date": "<Date format: YYYY-MM-DD>",
	    "monthly_salary": <Salary>,
	    "status": "<ACTIVE or INACTIVE>"
    }

The mentioned format may include just one or more fields. If your request was successful, you should receive a 200 OK Response with the following body:

    {
	    "employee_id": "<Employee ID>",
	    "first_name": "<First Name>",
	    "last_name": "<Last Name>",
	    "birth_date": "<Date format: YYYY-MM-DD>",
	    "monthly_salary": <Salary>,
	    "status": "<ACTIVE or INACTIVE>"
    }

## Delete an existing employee

You can edit an existing employee's info by either visiting the endpoint stated with the employee's id number (i.e., http://127.0.0.1:8000/<employee_id>/), or by sending a DELETE request to the same endpoint. If your request was successful, you should receive a 204 No Content Response.

##  List all existing employees

You can retrieve a list of all employees by either visiting the default endpoint stated (i.e., http://127.0.0.1:8000/), or by sending a GET request to the default endpoint. If your request was successful, you should receive a 200 OK Response with the following body:

    [
	    {
		    "employee_id": "<Employee ID>",
		    "first_name": "<First Name>",
		    "last_name": "<Last Name>",
		    "birth_date": "<Date format: YYYY-MM-DD>",
		    "monthly_salary": <Salary>,
		    "status": "<ACTIVE or INACTIVE>"
	    },
	    ...
    ]
    
You can order the contents of the list as well by adding the query parameter *'ordering'* to the default endpoint.

    http://127.0.0.1:8000?ordering=<field_name_1>,<field_name_2>

**Monthly salary in descending order**

    http://127.0.0.1:8000?ordering=-monthly_salary

**Date of birth in descending order**
	 
    http://127.0.0.1:8000?ordering=-birth_date

**First and Last Names in ascending order**
	 
    http://127.0.0.1:8000?ordering=first_name,last_name
