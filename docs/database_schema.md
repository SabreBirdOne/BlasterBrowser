**Overview**

This file serves as documentation on the design of the database. It includes a natural description of the data, written in a certain way to facilitate the database design.

Due to the project using PostgreSQL, which is a relational database, this file contains an Entity-Relationship Diagram and an abstract relational schema, which serves as a starting point in implementing the database.

**Background**

_First example_

Here's a link to a Google Drive document: "A Convenient List for New Nerfers With Too Much Money for Their Own Good", a Hobby Blaster Catalogue.
https://docs.google.com/document/d/11Hw1tJ7mDTvTfsuYxSW-Jt3kofQ2ssyZX8zoZuN_os8/edit#heading=h.s3sb7j7jz7q6

The document is found in the r/Nerf subreddit. Link: 
https://www.reddit.com/r/Nerf/about/

The document categorizes blasters based on the author's own criteria, such as "Injection molded" or "Springer Carbines". 
And "the terminology used is an analogue in order to represent certain attributes of the blaster". For the sake of the database schema, I think we may need another way to categorize blasters, but let's move on for now.

Throughout the document, for each category of blasters, there is a table of blaster information, the columns are: a set of images of the blaster, blaster name, designer names, a minimal description of the blaster, "Price Range According to Site Listing(s)", and Site Listing(s).

That's already a great starting point for a database schema.

_Second example_

Here's a link to a Google Drive spreadsheet: "Meaker Blaster Master List"
https://docs.google.com/spreadsheets/d/1YHi-dMucY6FEKNMeTnOKDIbyf-veNf7oJuvx2uj0X1g/edit#gid=23575684

This spreadsheet, at a glance, resembles a relational database, which is excellent. I'm primarily interested in the Printable Blaster List table. The columns are:
- creator: designer of blasters
- blaster: blaster name
- power source: describes dart launching mech
- feed: how the blaster feeds darts
- dart type: half, full, Mega, etc.
- action: the blaster action to launch darts (semi or full auto, slide prime etc.)
- flywheels: more specifically type of flywheels
- pusher: describes how darts are pushed into launching mech
- format: describes whether blaster is standard format, pistol, front, bullpup etc.
- license: 3D printing licensing?
- File/Insturctions cost: I think we should have 2 columns for each cost, even though very regularly the cost is for both files and instructions.
- Other notes: some more text describing the blaster

This spreadsheet really helps me with organizing database columns for blasters.

**Natural description of data**

A lot of the description below may sound very obvious to us as hobbyists. I'm writing it this way to explicitly make the data modeling clear for development.

The Hobby has a lot of designers involved, which is great. 
- Each designer is uniquely identified by a name. A designer can be an individual or a group.
- Each designer can be contacted via many links

The BlasterBrowser's database should contain blaster data as the main concern. Blasters have a variety of attributes inherent to the design. 

First, I'd like to state how we can uniquely identify blasters in the database
- Every blaster should be identified by a unique ID in the database.
- A blaster usually has only one name. But many blasters can also share a name (The Longshot confusion)...
  + If a blaster is derived from another, I think we should treat it as a standalone blaster. 
- A blaster can be designed by zero, one, or many designers

I made the choice of using an artificial ID in the database because names and designers of blasters may sometimes conflict... The way to ID blasters is extremely important because it is used to connect blaster attributes across the entire database.

Next, here are some attributes related to the blaster's mechanism
- A blaster's launch mech includes springer, flywheeler, HPA, string, or AEB (or more?).
- A blaster can have one, or many action types to prime itself and launch darts.
- If a blaster's launch mech is flywheel, then it has a type of flywheel used.
- A blaster has a dart pushing mechanism.
- A blaster have different ways to feed darts.
- A blaster can have a minimum and maximum cyclic rates of fire (-1 being manual)
- A blaster can have a minimum and maximum effective rates of fire (if manual, we can vote on it)

Some attributes about the darts 
- A blaster can use one, or many dart types.

Here are some attributes to describe the blaster's overall build
- A blaster's shell material can usually be 3D printed or injection molded, or fully metal etc.
  + If the shell material is mixed, the material that takes up the majority of the shell is listed.

- A blaster's internals, specifically the material, are important considerations
  + (for example: metal internals to withstand higher spring loads)

Some attributes about form factor.
- A blaster's length (in milimeters) is a worthy attribute, to determine which playstyles it may support.
- A blaster's ergonomic shape is interesting: pistol, bullpup, regular

Each Blaster can have documenation, which contains:
- information about licenses
- link to the license (optional?)
- an extra description.

The hobby have many shops:
- Each shop has a name that uniquely identifies it.
- A link to the shop's main page also uniquely identifies it.
- For the sake of simplicity, if we can buy blasters from an individual hobbyist or designer, we can also consider the person as a shop in the database

The hobby has blaster listings. 
- Each listing can contain many blasters
- Each listing has a price. If the price is variable from a listing, we can find a special number to indicate that.
- Each listing has a link, which is unique in the database.

A shop can have have many listings. 
A listing can only be from one shop (especially when the listing's link links back to a webpage of the shop)

A blaster listing can have many different blasters (I don't know, maybe a deal?). Also, it is possible that the same blaster can be in many listings (very commonly so!)

A blaster can be designed by many designers, while a designer can design many blasters.




