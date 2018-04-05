# Pepper navigation service


## Exploration/Creating a map
The code is copied from [the Pepper API documentation](http://doc.aldebaran.com/2-5/naoqi/motion/exploration-api.html#exploration-api).

First, run the service locally on your computer. **Make sure that you have uninstalled the service from pepper**

```
$ python service/decos_navigation.py --qi-url pepper.local
```

Then you can run the test app.

```
$ python test_app.py --ip pepper.local
```

The result should be a saved map "your_map.jpeg" and the map should also be prompted on your screen.

## Testing the application

To run all test cases:
```
$ python -m unittest discover
```

To run a specific unittest
```
$ python -m unittest -v service.test.test_exploration.TestExploration
```

Or if you are using [green](https://github.com/CleanCut/green)
```
$ green -vvv
```

To get the coverage
```
$ green -vvv -r
```