**Overview**
This file serves as documentation on the design of the database. It includes a natural description of the data, written in a certain way to facilitate the design.

Due to the project using PostgreSQL, which is a relational database, this file contains an Entity-Relationship Diagram and an abstract relational schema, which serves as a starting point in implementing the database.

**Warming up**

Here's a link to a Google Drive document: "A Convenient List for New Nerfers With Too Much Money for Their Own Good", a Hobby Blaster Catalogue.
https://docs.google.com/document/d/11Hw1tJ7mDTvTfsuYxSW-Jt3kofQ2ssyZX8zoZuN_os8/edit#heading=h.s3sb7j7jz7q6

The document is found in the r/Nerf subreddit. Link: 
https://www.reddit.com/r/Nerf/about/

The document categorizes blasters based on the author's own criteria, such as "Injection molded" or "Springer Carbines". 
And "the terminology used is an analogue in order to represent certain attributes of the blaster". For the sake of the database schema, I think we may need another way to categorize blasters, but let's move on for now.

Throughout the document, for each category of blasters, there is a table of blaster information, the columns are: a set of images of the blaster, blaster name, designer names, a minimal description of the blaster, "Price Range According to Site Listing(s)", and Site Listing(s).

That's already a great starting point for a database schema.

**Natural description of data**

So the BlasterBrowser's database should contain blaster data as the main concern. Blasters have a variety of attributes inherent to the design. 

A blaster usually has only one name. If a blaster is derived from another, I think we should treat it as a standalone blaster.
A blaster's launch mechanism includes springer, flywheeler, HPA, string, or AEB (or more?). 
A blaster build can be 3D printed or injection molded, or both, but let's say we decide the build based on which material takes up the majority of the blaster. 
A blaster's length is a worthy attribute, to determine which playstyles it may support.
A blaster can be magazine fed or not. For blasters that can operate regardless of being magazine fed, we decide that it is magazine fed.
A blaster can be fed via mag-in-grip or not.
A blaster can be a true pistol or not. 
Finally, for contigency and more information, every blaster has a minimal description.

I have been avoiding costs and site listings, so I'll address them now.

The hobby have many shops, where each shop has a name and a link to the shop in general. Shops are uniquely identified by name.
The 



