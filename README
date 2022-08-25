# Screenpy Demo Stack

## Installation

You'll want chrome, chromedriver, and xvfb.
To install required dependencies, run
`pip install -r requirements.txt`

## Running tests

From the root of the repo, run:
`./test {desired directory or test file}`

Examples:

```shell
# all tests
./test

# all swaglabs test suites
./test features/swaglabs

# only the_innerent test file
./test features/the_innernet/test_theinnernet.py
```

## What is this? What is it for?

This is a general-purpose implementation of the [Screenpy](https://github.com/ScreenPyHQ) Automated testing framework.

For now, primarily this is just a ready-made platform to pull up during interviews to demonstrate my general approach and philosophy of automated testing.

Secondly, it's a handy pitch for the excellent Screenpy framework specifically.

And finally, it's a platform for me to experiment with broader targets and skills that I haven't had the opportunity to work with in my career thus far.

## What is this not?

This is not a formal showcase of the Screenpy framework, though I'm pretty proud of the approach I take with this tool. 

For a more comprehensive and deeper set of examples of the framework, see the [Screenpy Examples](https://github.com/ScreenPyHQ/screenpy_examples) module at Screenpy HQ.

## I'm not currently interviewing you, but I'm interested in this. What should I be looking at?

Great question, cherished admirer!

I may not have added everything in the following list yet, but I'm particularly fond of these techniques / patterns:

* *Tasks* are not specific to Screenplay pattern, but I find them extremely useful as a pattern for keeping automated test suites readable and maintainable. Common workflows that fit nicely into the *Task* paradigm are things like login sequences and the like, but there are much more interesting applications as well.

    Examples:

        tasks/swaglabs/login_to_swaglabs.py 

* *Dataclasses* for handling complex concepts such as Users. Whether you're working with static data or generating data in real time for your test cases, maintainability can become catastrophically strained as your suite expands. Bundling related data fields into a single package and designing relevant methods to handle that package in a standardized way pays huge dividends! 

    Examples:
    
        constants.py
        user_classes.py
        