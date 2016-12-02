# Fresh Tomatoes

This is a Python application written with server-side code to compile python to HTML and open a static web page based on
 your favorite movies.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
You will need to have Python 2.7.0 installed on your machine

Before installing Python, you’ll need to install a C compiler. The fastest way for OS X is to install the Xcode Command Line Tools by running     ```xcode-select --install```.
You can download the full version of Xcode from the Mac App Store.

OS X does not come with a decent package manager so we will be installing Homebrew. To install Homebrew, open ```terminal``` and paste in the following command.

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

The script will explain what changes it will make and prompt you before the installation begins. Once you’ve installed Homebrew, insert the Homebrew directory at the top of your PATH environment variable. You can do this by adding the following line at the bottom of your ~/.profile file

```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```
Now, we can install Python 2.7:
```
$ brew install python
```
### Installing

Download the fresh_tomatoes folder and run the following:

```
python film_list.py
```

This will generate the HTML code and open a window in your web browser displaying 6 of my favorite movies.

### Further Customizing

Simply change out the parameters of any of the film_X variables to display your favorite movies and their trailers.

```
film_1 = film.Movie("My Neighbor Totoro",
                    "https://upload.wikimedia.org/wikipedia/en/0/02/My_Nei"
                    + "ghbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.j"
                    + "pg",
                    "https://www.youtube.com/watch?v=92a7Hj0ijLs")
```


## Built With

* Plain Old Python

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Andrew Palka** - [Github](https://github.com/andrewmpalka)


## License

This project is licensed under the MIT License.