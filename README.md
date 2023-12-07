# Static site
Generates static web pages from HTML templates and source files. Uses the source directory structure to structure the web page navigation

# The structure is directory index pages, leaf pages and child folders
* Index pages contain links to their own leaf pages & thumb nails with links to their child directories
* Leaf pages contain actual content (HTML, images, videos)

# Navigation
* Breadcrumbs are generated automatically to navigate the directory structure
* Previous & next links generated automatically using alphabetic sorting by source file name
* Provide download links for content


# Source folder structure

## Root folder

* used to generate the site index page
* data.yml
    *  contains site name and site owner data
* data from sub folders is used to generate the index page contents of sub-directories


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
        * thumb.png <- for the parent index page

        * image_page_1.html
        * image_1.png
        * video_page.html
        * video.mp4
    * sub_folder
        * index.html
        * thumb.png <- for the parent index page

            * sub_folder
                * index.html
                * thumb.png <- for the parent index page

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


# Classes
    * Director - interface for classes to direct building a tree of page nodes
        * Director has logic to read from a source (fs, s3 bucket, json file, yaml file etc)
        * FileSystemSourceDirector - reads from a source directory
        * S3SourceDirector - reads from an S3 bucket

    * Builder - interface for classes to build page nodes
        * keeps state with current node, allows current node to be set

    * Generator - interface for classes to generate a set of html pages & assets from a tree of page nodes
        * FileSystemTargetGenerator - writes to a target directory


# Required page properties

* title
* path

## Arbitrary properties, used to populate templates

* owner
* sub_title
* inline css
* inline js

* child pages

## Files
* thumbnail image
    * page path
    * source path
* content file (img, vid, text/md)
    * page path
    * source path
* css files
    * page path
    * source path
* js files
    * page path
    * source path
###
    * file interface
    * provide the source location
        * diff impls for local, S3, http etc
    * calculates page path
    * provides file name etc

