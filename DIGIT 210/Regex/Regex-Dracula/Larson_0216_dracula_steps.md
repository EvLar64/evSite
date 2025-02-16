# Dracula Steps - E.L.

Find: ` & `

Replace: ` &amp; `
- Fixes &'s

Find: ` \n{3,} `

Replace: ` \n\n `
- Consistent spacing

Find: ` (.+) `

Replace: ` <drac>\n\1\n</drac> `
- Wraps the whole thing in "drac" root tags

 Find: ` (D R A C U L A) `
 
 Replace: ` <title>\1</title> `
 - Title tags around the spaced-out "Dracula"
 
 Find: ` (CHAPTER )([IVXCML]+) `
 
 Replace: ` <chapterHeading>\1\2</chapterHeading> `
 - Wraps each chapter heading in its own tag
 
Find: ` <chapterHeading>(CHAPTER )([IVXCML]+)</chapterHeading> `

Replace: ` </chapter>\n<chapter num="\2"><chapterHeading>\1\2</chapterHeading> `
- Takes the new heading tags and uses them to make overall chapter indicators (which needed manual editing for the very start and end)

Find: ` \n\n</chapter> `

Replace : ` \n</chapter> `
- Fixes spacing

Find: ` (^\s*\n) `

Replace: ` </p>\1<p> `
- Creates p tags around paragraphs (which required a little fixing around beginning/end, and chapter headings)

Find: ` (<chapter (.+?))\n</p> `

Replace: ` \1\n `
- Fixes p tags around chapter headings

Find: ` (</chapter>) `

Replace: ` </p>\n\1 `
- Fixes p tags around the ends of chapters

(** Other changes made using XSLT document **)