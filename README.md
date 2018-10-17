# [venue-spex](https://venue-spex.herokuapp.com/)

## Summary
Why jump through hoops to find technical specifications for the venue you'll be performing in? Venue-spex centralizes all relevant information for venues in your city. All the gear - all up to date.

Check it out on [Heroku](https://venue-spex.herokuapp.com/).

## Inspiration
As a musician and technician in the world of live performance, it's sometimes been hard to track down the technical specifications for venues, rehearsal spaces, and even recording studios. 

The traditional way is to contact the venue at an hour in which they will attend the phone, or hope someone answers your email from the generic "info@venue.com". Higher-end venues often provide their specs on their websites, but then neglect key information or don't update their site regularly.

Venue-spex aims to become the largest, most complete database of relevant venue tech specs for venues all over the world. It currently provides a centralized place for performance professionals to add, update, and modify their venues while allowing others to comment tips for each.

It is far from finished, and there's a lot to fix! Please see the future developments section at the bottom of this file!


## Technologies
- FULL Django
- Heroku (not a huge headache this time around!) 
- Pillow

## MVP
Reached full CRUD on all models.

## To-do of Fixes
- Handle errors on front end more in a prettier way.
- Handle delete yourself with a warning.
- More, better redirects
- Find a way to attach comments to the current Venue.pk (not just to a user)
- Add better styling + layout w/ modals and carousels

## Future Features
We don't stop here! If you spot bugs or have an idea for a feature, reach out at <em>venue.spex at gmail dot com</em>

- Create API with real venue data (with venue permission)
- Incorporate Google Places api for more venue info
- Add Google Maps (or Open Map) for a map view of venues with pins
- Make different types of users with different auth capabilities (Venue Managers - done; Musicians, Tour Managers, Technicians (not done))
- Gig list - enable musicians and performance professionals to "follow" venues and add them to a list of upcoming gigs
- Automatic email for user signup and for venue updates to venue followers
- Search functions
- Expand models for rehearsal spaces and recording studios