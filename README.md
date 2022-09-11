# Student Grade Checker

# studentgradechecker-transcript-40040160

Student Grade Checker is a microservice application designed as part of the Queen's University Belfast MSc Software Development Cloud Computing module (CSC7071).

The transcript function utilises Python Flask to receive HTTP request with form data, processes the values and uses FPDF import to format in a PDF file. This is
then send back to client and downloaded through the browser.

## Functions

1. Highest and lowest scoring modules calculator
2. Sort modules from highest to lowest score
3. Calculate total marks
4. Calculate final classification (measured against QUB official guidelines)

### Additional Functions

5. Get averages (all modules, dissertation modules, non-dissertation modules)
6. Print unofficial transcript to PDF

## Further Information

#### The project required the demonstration of:

A) New functionalities using containers, including unit testing and CI pipeline

B) Improvements to functionalities, including error handling, stateful saving and frontend failure handler

C) Proxy implementation, including configurability

D) Monitoring

## Contributing

Original code created by Niall Hodgen.

## License

[MIT](https://choosealicense.com/licenses/mit/)
