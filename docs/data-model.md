# Data Model

## Jewelry Item

Represents a physical vintage jewelry object.

Core attributes:

- item_id
- brand
- designer
- category
- signature
- estimated decade
- materials
- condition
- dimensions
- weight
- authenticity status
- data quality score

## Market Observation

Represents a market event related to a jewelry item.

Examples:

- confirmed sale
- auction result
- active listing
- unsold listing

Core attributes:

- observation_id
- item_id
- platform
- asking price
- sold price
- currency
- sold date
- source
- reliability score

## Important Design Principle

Jewelry items and market observations are stored separately.

An asking price is not equivalent to market value.

Confirmed sales therefore receive a higher reliability score than
active listings.
