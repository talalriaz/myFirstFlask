# myFirstFlask
A very simple Flask application.

## How to run
1-  In the root directory, build the docker image using command ``docker build -t my_flask .``

2-  Once the image is build, run the container using command ``docker run -p 5000:5000 my_flask``.

3-  You can verify the running container by ``docker ps``

4-  Submit the ``POST`` json request with two numbers, it will add both of them and display the results.

A sample json input:
```
{
    "num1" : 150.5,
    "num2" : 90.5
}
```
