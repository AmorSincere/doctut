# Django MTV Tutorial Project

This repository contains the code for a Django project designed to help users create their own tutorials. The project is inspired by GitBook, and allows users to create multiple tutorials, subjects, and content within those subjects.

## Features

- Authentication: Users can create accounts and login to the site. Authentication is required for creating tutorials, subjects, and content.
- Create Tutorials: Users can create multiple tutorials, each with its own subjects and content.
- Subject Management: Users can add subjects within their tutorials.
- Content Management: Users can add but cannot delete content within the subjects of their tutorials after creating it.

## Usage

To use the project, simply clone the repository and run the Django development server using the `python manage.py runserver` command. You may also need to create and apply migrations using the `python manage.py makemigrations` and `python manage.py migrate` commands.

## To Do

- Improve Design: The current design could use some work, and we plan to improve the visual appearance of the site.
- Add Rich Text Editor: Currently, users can only create plain text content. We plan to add a rich text editor to allow for easier formatting.
- Free Tutorial Link: We plan to add a feature that allows users to generate a link to their completed tutorial and share it with others (done without design).

## Credits

This project was created by Abduqosim.

Feel free to use, modify, and distribute this project.
