# static-site
Generate static web pages from templates

# Organise source files into the target directory structure

# The structure is simply indexes & leaf pages

* Index pages contain links & thumb nails to child directories
* Leaf pages contain actual content (HTML, images, videos)

# Navigation
* Bread crumbs are generated automatically to navigate the structure
* Previous & next links generated automatically using alphabetic sorting by source file name

* Provide download links for content?


# Source folder structure

## Root folder

* used to generate the site index page
* data.yml
    *  contains site name and site owner data
* data from sub folders is used to generate the index page contents



# Generation logic

* read all data into a tree structure of generators
* validate source files exist
* iterate over the tree creating index pages, leaf pages and source files
    * read from source folder & child folders
    * write to target folder - this is the static site contents


# Target structure

root
* index.html
    * sub_folder
        * index.html
        * image.png
        * thumbx.png
        * video.mp4
    * sub_folder
        * index.html
            * sub_folder
                * index.html
                * image_1.png
                * thumb_1.png
                * page_1.html
                * image_2.png
                * thumb_2.png
                * page_2.html
css
    * stylesheet_1.css
js
    * javascript_1.js

