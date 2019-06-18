# tulang

A very opinionated :stuck_out_tongue: simple backend generator 

# Problem

It takes a lot of effort and steps to setup a backend service that include:

* Monitoring
* CI/CD
* Documentation
* Compute Engine

# Who is it for ? 

Developers that want to quickly spin up a backend with minimal development work to easily test out some ideas

# Existing Solutions

There are solutions to generate template based on API specifications i.e. Swagger Generator and OpenAPI 3.0. However, there is no single solution that integrates the features we want together

# Proposed Solution

## CI/CD

[CircleCI](https://circleci.com)

## Compute Engine

AWS Lambda

## Protocol

REST

## Documentation

Swagger

## Version Control

Github

## Monitoring

CloudWatch via Lambda 

## Languages

Python, Javascript

# Code Generation

## Existing Solution

- General
    - [Conjure](https://medium.com/palantir/introducing-conjure-palantirs-toolchain-for-http-json-apis-2175ec172d32)
    - [Telosys](http://www.telosys.org/models.html)
    - [Swagger Codegen](https://github.com/swagger-api/swagger-codegen)
    - Protobuf and Thrift
- Python
    - [Jinja2](http://jinja.pocoo.org/) 
- Javascript
    - [Yeoman](https://yeoman.io/)
- Videos
    - [Source Code Generation](https://www.youtube.com/watch?v=jKWJKCuggmI)
    - [Human-readable scheduling tool](https://www.youtube.com/watch?v=TCPhJpKv9SE)
