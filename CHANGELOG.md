## [Unreleased]

### Added

- Added the new location url for redirects [#29](https://github.com/Patr1ick/green-web-analyzer/issues/29)

### Updated

- Updated UI
- Updated TailwindCSS Preflight for basic UI elements [#27](https://github.com/Patr1ick/green-web-analyzer/issues/27)

## [1.0.0]

### Added

-   Added further security for the webhook endpoint
-   Added healthcheck endpoint and integrated it into docker [#17](https://github.com/Patr1ick/green-web-analyzer/issues/17)

### Updated

-   Updated the way chromium and the Chromedriver is downloaded [#20](https://github.com/Patr1ick/green-web-analyzer/issues/20)
-   Updated AboutPage [#24](https://github.com/Patr1ick/green-web-analyzer/issues/24)

### Fixed

-   Fixed units [#19](https://github.com/Patr1ick/green-web-analyzer/issues/19)
-   Fixed bug where chromium and chromedriver has different versions [#20](https://github.com/Patr1ick/green-web-analyzer/issues/20)

## [0.2.6](https://github.com/Patr1ick/green-web-analyzer/releases/tag/0.2.5)

### Added

-   Added new metric "website is using green energy" [#14](https://github.com/Patr1ick/green-web-analyzer/issues/14)
-   Added new metric "estimated website co2 emissions" [#15](https://github.com/Patr1ick/green-web-analyzer/issues/15)

## [0.2.5](https://github.com/Patr1ick/green-web-analyzer/releases/tag/0.2.5)

### Added

-   Added new criteria "minify files" [#1](https://github.com/Patr1ick/green-web-analyzer/issues/1)
-   Added new criteria "images lazy loaded" [#4](https://github.com/Patr1ick/green-web-analyzer/issues/4)
-   Added new criteria "avoid massive payload" [#3](https://github.com/Patr1ick/green-web-analyzer/issues/3)

### Updated

-   Updated the criteria in the backend so that they are more consistent

### Fixed

-   Fixed bug in views.py
-   Fixed that really all requests are registered
-   Fixed bug when assigning all files by type

## [0.2.4](https://github.com/Patr1ick/green-web-analyzer/releases/tag/0.2.4-fix)

### Added

-   Added BasicHint and better error messages
-   Added new metric potential savings (not finished)
-   Added icon
-   Added new criteria "redirects"

### Updated

-   Updated styling for Components

## [0.2.3](https://github.com/Patr1ick/green-web-analyzer/releases/tag/0.2.3-fix)

### Added

-   Added more logging and validation to the backend
-   Added privacy policy

## [0.2.2](https://github.com/Patr1ick/green-web-analyzer/releases/tag/0.2.2)

### Added

-   Added RequestForm to MainPage
-   Added basic AboutPage

### Updated

-   Updated dark theme
-   Updated CriteriaRequest to handle redirects and requests with no responses

### Removed

-   Remove extra Page for Requests
