# Overview

This file serves as documentation on the design of the database. It includes a natural description of the data, written in a certain way to facilitate the database design.

Due to the project using PostgreSQL, which is a relational database, this file contains an Entity-Relationship Diagram and an abstract relational schema, which serves as a starting point in implementing the database.

Note that ERD diagrams and natural description can be constantly under work.

# Background 

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

# Natural description of data

A lot of the description below may sound very obvious to us as hobbyists. I'm writing it this way to explicitly make the data modeling clear for development.

When discussing entities below:
- Entities are basically the tables in the database
- Each entity has at least one attribute: columns of the table.
- Each entity needs to have a key: a set of attributes that uniquely identify a row in the table.
- Attributes / Columns must be able to characterize a row in the table on their own. To show you what I mean, here's an example:
  + Should length be an attribute of a spring? Yes. Length is the usual description of a spring.
  + Should dart velocity effect be an attribute of a spring? Likely yes. What fps a spring can achieve describes that spring.
  + Should price be an atribute of a spring? Not really. You buy a spring from a shop's listing, and the listing has a price. So the price describes the listing for the spring, not the spring itself.

- If a table can satisfy the above, then it is a good table.

**Entities**

The database records data about people involved in the Hobby.
- Each person is uniquely identified by a name. A "person" here can be an individual, a group or a company. Names are unique in the database.
- Each person has a description

The database collects blaster data, the main concern. 
- Every blaster is identified by a unique ID in the database.
- A blaster has a name. Not always unique (Longshot confusion)

The database records all launch mechanisms commonly seen in the Hobby.
- Each row has just one unique type in the database: springer, stringer, flywheel, hpa, aeb, etc.

The database collects data about listings. 
- Each listing is uniquely identified by an ID in the database
- Each listing has a price. Listings with variable prices have a price of -1.
- Each listing may have a name, link to the a webpage, and a description. 

The next set of entities describe blaster parts in the hobby.

The database stores parts information:
- Each part has a unique id in the database
- Each part has a name, and a stock indicator
- Each part has a material: aluminum, brass, anonized, 3d_printed, abs, etc.
- Each part has a part type, and description

The database stores muzzles information:
- Each muzzle has a unique part id in the database (same id as the one in parts table)
- Each muzzle has a length (mm), and attaching diameter (mm) (what is the outer diameter of any barrel that the muzzle can attach to)

The database stores scar_muzzles information:
- Each scar has a unique part id in the database (same id as the one in parts table)
- Each scar has a number of strings, and rotation (degrees)

The database stores bcar_muzzles information:
- Each bcar has a unique part id in the database (same id as the one in parts table)
- Each bcar has a number of bearings, and rotation (degrees)

The database stores tracer_muzzles information:
- Each tracer muzzle has a unique part id in the database (same id as the one in parts table)
- Each tracer muzzle has brightness (lumens)

The database stores decorative_muzzles information:
- Each decorative_muzzles has a unique part id in the database (same id as the one in parts table)

The database stores launch_springs information:
- Each launch spring has a unique id in the database (same id as the one in parts table)
- Each launch spring has a length (mm), outer diameter (mm), inner diamter (mm), and spring constant (newtons per meter)

The database stores barrels information:
- Each barrel has a unique id in the database (same id as the one in parts table)
- Each barrel has a length (mm), outer diameter (mm), inner diameter (mm)

The database stores spring_modifiers information:
- Each spring modifier has a unique id in the database (same id as the one in parts table)
- Each spring modifier has a type: spacers, caps, etc.


**Relationships**

A blaster can be designed by 0 to many people. A person can design 0 to many blasters

A blaster can have 1 to many launch mechanisms. A launch mechanism is used in 0 to many blasters.

A blaster is compatible with 0 to many parts. A part is compatible with 0 to many blasters.

A person can have 0 to many listings. A unique listing can only be from one person.

A listing can have 0 to many different blasters. A blaster can be in 0 to many listings.

A listing can have 0 to many different parts. A part can be in 0 to many listings.

Parts is a family of blaster parts. All parts have a universal part id across the database, and have a part type inside the family tree below:

All Parts:
- Muzzles
  + SCAR Muzzles
  + BCAR Muzzles
  + Tracer Muzzles
  + Decorative Muzzles
- Launch springs
- Barrels
- Spring modifiers

**Other considerations**

These considerations are nice to be documented, but I haven't found a good way to incorporate them into the schema.

Here are some things related to the blasters

Blaster's launch mechanism:
- A specific launch mechanism, in a specific blaster or as a standalone part, is uniquely identified by name
- Each specific launch mechanism belongs to a type: springer, flywheeler, HPA, string, AEB, etc.

A blaster can have at least one, and many specific launch mechanisms. A specific launch mechanism may be placed in many blasters
- For example: a stock Nexus pro can have a stock spring or upgraded spring. The Worker Swift spring can be placed in the Swift, or the Worker Harrier blasters

Blaster's action mechanism:
- A specific action mechanism, in a specific blaster or as a standalone part, is uniquely identified by name
- Each specific action mechanism belongs to a type: pump, slide prime, regular bolt, straight pull bolt, semi automatic, fully automatic etc.
- A specific action mechanism can achieve a cyclic rate of fire and effective rate of fire.

A blaster can have at least one, and many action mechanisms. A specific action mechanism may be placed in many blasters
- For example: the XYL Unicorn can be pump action or slide prime action. A HPA core can be placed in HPA-minded blasters, or someone in the Hobby can mod a Nexus pro to use HPA cores (?)

Blaster's flywheels:
- A specific flywheel model, in a specific blaster or as a standalone part, is uniquely identified by name
- Each specific flywheel belongs to a type: brushed, brushless, etc.

A blaster can have zero, one, or many specific flywheel models. A specific flywheel model can be placed in many blasters.
- For example: nexus pro has no flywheels (in case the hobby can do it, the database can cope with that), Kraken motors can be placed in Stryfe or OFD Quik (?) blasters.

Blaster dart feed mech:
- A specific dart feed mechanism, in a specific blaster or as a standalone part, is uniquely identified by name
- Each specific dart feed mechanism belongs to a type: single shot, cyclinder fed, front-of-grip magazine fed, mag-in-grip, bullpup magazine fed, hopper-fed, etc.

A Blaster can have at least one, to many dart feed mechanism. A specific dart feed mechanism may be placed in many blasters.
- For example: the Matrixfire can be hopper-fed (stock form) or front-of-grip magazine fed (via a mod). Or a specific talon magazine adapter can be placed in many blasters.

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

Each Blaster can have additional documentation, which contains:
- information about licenses
- link to the license (optional?)
- an extra description.

# Entity-Relationship Diagram

Diagrams are drawn and viewed on this website: https://app.diagrams.net/

 ![ERD](https://github.com/SabreBirdOne/BlasterBrowser/blob/main/docs/ERD.png)




# Schema


