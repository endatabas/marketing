# Endb Video Script

NOTE: After each Problem, the images corresponding to the Problems could collapse into
      bubbles with text under each one (Destructive Updates, Fragile SQL, Proprietary
      Documents, Separate OLAP Tools, Coupled Storage, Expensive Operations) ... I'm not
      sure if this is necessary yet, though. -sd

## 1970s Computer Room

1960s / 1970s jazz playing (Thelonius Monk's "I Surrender, Dear"? or John Coltrane's "Psalm" or "Pursuance - Original"?)
Zoom into terminal screen with blinking cursor.

## Terminal Screen

On screen, show typing: "THERE IS A PROBLEM WITH DATA TOOLS TODAY".
Volume of jazz is reduced to background audio.

Zoom further into terminal so it is the entire screen.

## Office Interior

* PROGRAMMER, MECHANIC, DOCTOR, & SCIENTIST:

> We're tired of babysitting dozens of data tools.

* CEO:

> And I'm tired of paying people to babysit databases instead of doing their actual job.

Narrator appears, a 1970s female programmer, neatly dressed.
She speaks with a Swedish accent.

* NARRATOR:

> The landscape of data tools in 2024 is fractured and scattered.
> Let's take a look at why. And how we might solve this problem.

## Modern (2024) Server Rack

Narrator stands beside server rack.

* NARRATOR:

> Most OLTP databases still have destructive updates.
> If users update or delete a record, the past is gone forever.
> This means that compliance, audits, and historical queries are all manual.
> These basic processes are accomplished with additional tools, data duplication, and awkward queries.
> These "solutions" are complicated and expensive.

As the Narrator says "destructive updates", tiny explosions animate on the servers in the rack.
The explosions continue as she speaks.
A confused/frustrated doctor appears beside the exploding rack.
As the Narrator describes the 3 processes, they are listed on the left.
As the Narrator describes the 3 solutions, they are listed on the right (in red text?).

* NARRATOR:

> The real solution is, of course, to stop destroying things:
> Keep the full history in an immutable object store.
> Give users audits and time travel for free.
> And only ERASE data to comply with laws like GDPR.
> This is the foundation.

The "exploded" server rack moves aside with little burned spots where explosions happened.
A clean server rack with attached disk appear beside the Narrator (with no explosions).

As the Narrator says "foundation", the clean server rack + disk become the Zeroth Bubble (in the centre).
The Zeroth Bubble says "Full History" under it.

## Two Terminals, Side By Side

Narrator may or may not be visible.

* NARRATOR:

> The relational model has a lot of baggage.
> SQL databases have no flexible schema, so they calcify with age.
> Flexibility is shoehorned in with JSONB columns and making everything nullable.
> As an organization matures, and becomes inreasingly reliant on the database,
> it become fragile and expensive to change.

The first screen has 3 or 4 2D database tables on it.
"Calcify": The tables become 'hard' (stone?).
"JSONB": A few ill-fitting documents are placed in some table cells for some columns.
"Nullable": A few scattered NULLs are spread across the tables.
"Fragile": One or two table crack?

* NARRATOR:

> Of course, the NoSQL fad was no solution.
> These databases had non-standard query languages.
> They were all different.
> They stored stringly-typed JSON or weakly-typed objects.
> Developers and DBAs had no way to reuse their knowledge of other databases.
> This world was proprietary, expensive, and full of vendor lock-in.

The second screen has 3 or 4 document icons on it.
"Query languages": Scribble queries in a few different colours/languages.
"Stringly-typed" / "Weakly-typed": Colour each document differently.
"Developers and DBAs": Mechanic and doctor appear, confused. (Optional)

* NARRATOR:

> We should grow the relational model
> ...rather than going multi-model or throwing it out completely.
> The relational model can support strongly-typed documents
> ...and arbitrary joins
> ...in a standard storage format like Apache Arrow
> ...with standard, native SQL
> ...over standard protocols.
> This is the user interface.

As the Narrator says this, the two terminals join.
The documents all become one colour.
Each document slides into one row of the tables.
(I'll explain this. Alternatively, we can merge the tables so we only have to animate one.)

As the Narrator says "user interface", the merged terminal becomes the First Bubble (on the left).
The First Bubble says "SQL Documents" under it.

NOTE: To keep the numbering the same as my notebook, this is both First and Second Bubble.

## A Complicated Rube Goldberg Machine

The Machine consists of multiple terminals, server racks, storage boxes, big cylinders,
and clocks. It is all connected with conveyor belts. (Doesn't need to be animated.)
Narrator stands in front, motioning to the machine with her hand.

* NARRATOR:

> Most OLAP databases still require separate tools.
> Often, _many_ tools.
> Since OLTP databases destroy data, we lean on event streams.
> Data is shuffled around to column stores and time series databases.
> Data Scientists can't use the same interfaces as Developers.
> This leads to complexity, maintenance, and expense.
> (You're probably noticing a theme, here.)
> Even Hybrid Transactional/Analytical (or "HTAP") stores tend to duplicate data into column stores
> ...or force the user to choose between columns and rows.

As the Narrator talks, tired-looking mechanics and scientists appear near the machine.
No animations are required for this picture while the Narrator talks.
If the conveyor belts moved boxes around, that would be a nice touch.

* NARRATOR:

> We should support True HTAP.
> We need to unify OLTP, timeline, and columnar data into one relational model.
> Immutability gives us a timeline.
> Apache Arrow gives us columnar storage.

As the Narrator speaks, the Rube Goldberg Machine collapses into one database cylinder.
This becomes the Third Bubble.
The Third Bubble says "True HTAP" under it.

## Database Cylinder

The Narrator stands close to the cylinder.

* NARRATOR:

> Okay, so, why can't other databases support True HTAP?

A computer chip appears beside the cylinder.

* NARRATOR:

> Most databases have storage coupled to compute.
> Local disk is limited and expensive.
> Sharding is complicated and error-prone.
> Failover, HA, and scale are complicated and expensive.

As each description is given, another chip/cylinder pair appears
with question marks or dollar signs on top.

* NARRATOR:

> The solution? Separate storage from compute.
> The immutable object store becomes the source of truth.
> Compute nodes are cheap and scale freely.
> Without the immutable object store, this is very difficult to do.

When "object store" is mentioned, the cylinder slides up and multiplies into dozens of cylinders.
When "compute nodes" are mentioned, the computer chip slides down and divides into five chips.

The many cylinders and chips become a smaller Fourth Bubble, next to the Third Bubble.
The Fourth Bubble says "Separated Storage & Compute" under it.

## Dozens of Database Cylinders

The Narrator stands close to the dozens of database cylinders.

* NARRATOR:

> This sure looks like a lot of data to manage.
> Won't this make an existing problem worse?
> At the beginning, we heard that everyone is tired of "babysitting databases".
> Optimizing queries.
> Fiddling with indexes.
> All of this wastes time and money.

When "babysitting databases" is mentioned, mechanics with wrenches and goggles
appear on the other side of the cylinders.

* NARRATOR:

> We must automate all of this with Machine Learning.
> Queries should optimize themselves.
> Indexes need to be adaptive.
> Light and Adaptive Indexes keep queries fast without overburdening nodes.

When "automate" is mentioned, the mechanics are replaced with 1970s-style robots.

The robots become a small Fifth Bubble, next to the Third Bubble.
The Fifth Bubble says "Light and Adaptive Indexes" under it.

## Complete Bubble Diagram

Narrator is off-screen.
We hear the Narrator coming from the speaker of the terminal.
(She is no longer as clear as during the rest of the video.)

* NARRATOR:

> A database like this was not possible ten years ago.
> Such a database can't be built from Postgres plugins.
> It requires a total reimagining of what a database can be.
> Perhaps it can replace dozens of data tools and save millions of wasted hours.

As this is spoken, zoom out to terminal screen.
Replace Bubble Diagram with a pixelated Endatabas logo.

* NARRATOR:

> En databas.
> A Database.
> One Database.

As each word pair is spoken, it is displayed on-screen.

## 1970s Computer Room

We zoom out from the terminal to see the entire server room again.
The jazz music from the beginning becomes louder as the image fades out.
