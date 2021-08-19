# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added

### Changed

### Removed

## [v0.3.0](https://github.com/drewtchrist/pylabeler/releases/tag/v0.3.0) - 2021-08-18
### Added
* Set up pre commit hooks
* Created an HtmlModel class to hold the html and connect signals to
* Created a custom web engine that accepts drops
* Created an assets directory that persists after install
* Bundled interact.js with the projects in the assets directory
* Connected interact.js with the web engine and html successfully
* Added desktop shortcuts on installation with pyshortcuts

### Changed
* Tree view and tool buttons stay disabled when an item dialog is open to prevent opening more
* Majorly refactored main_window.py by moving all file i/o logic into application.py

### Removed

## [v0.2.0](https://github.com/drewtchrist/pylabeler/releases/tag/v0.2.0) - 2021-08-10
### Added
* Added qt-material stylesheet
* Added files for github pages
* Added a link to the github pages under the help menu
* Added an about dialog

### Changed
* Increased the size of all the left side widgets
* Replaced QTextEdit for html with QsciScintilla with an html lexer
* Tool button icons are white now

### Removed
* Removed QTextEdit for css

## [v0.1.0](https://github.com/drewtchrist/pylabeler/releases/tag/v0.1.0) - 2021-08-08
### Added
* Basic UI design is implemented
* Methods for getting from user input -> html label -> pdf with labels have been realized
* Rough class diagram has been added

### Changed

### Removed
