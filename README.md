# Music Library Management System

A music library management system built in Python using OOP concepts.

## Classes

- **MediaItem** - Base class for all media items
- **Album** - Inherits from MediaItem, represents a music album
- **Podcast** - Inherits from MediaItem, represents a podcast
- **Member** - Represents a library member
- **MusicLibrary** - Main class that manages albums and members

## OOP Concepts

- **Inheritance** - Album and Podcast inherit from MediaItem
- **Polymorphism** - display_info() behaves differently for Album and Podcast
- **Encapsulation** - Each class manages its own data

## How to run

python main.py

## How to run tests

python -m pytest test_library.py -v