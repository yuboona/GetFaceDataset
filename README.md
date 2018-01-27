# Get the Pubfig dataset

---

## What this is

This is a project for fetching the [Pubfig face dataset][1].

[Pubfig face dataset][1] is a useful dataset for developing the face recognition models. And it's dataset is a txt file contains the source urls of the face pics. It's a really boring work to make a program to fetch them. So you can just use my code to save time.

## Attention

The raw `dev_people.txt` and `dev_urls.txt` from Pubfig contains a list of persons' face pics urls. I cut the **Miley_Cyrus**'s contents and make them a new file called `Miley_Cyrus.txt`.

You can do the same to cut a person's list you need.

## How to use

This project uses python3.5 and the module urllib, requests.

Make sure that you have the py3.5 installed. Or you need install them by `$ sudo apt install python3` on Ubuntu.

You can use following lines to run the program(I have 4 .py files, but only the `get_url.py` and `get_face_with_headers.py` will be used):

```python
    # download the code
    $ git clone git@github.com:yuboona/GetFaceDataset.git

    # run the get_url.py, get the pure urls
    $ cd ./GetFaceDataset
    $ python3 get_url.py

    # run the get_face_with_headers.py
    $ python get_face_with_headers.py

```

## Some interesting things
I tried three ways to fetch the pics. 

1. urllib without headers
1. urllib with headers
1. requests with headers

Finally I choose the 2rd way as the default solution. Requests is more convenient, but don't get the exact results I need. There are too much verbose things in the result.


[1]: http://www.cs.columbia.edu/CAVE/databases/pubfig/