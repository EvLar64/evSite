# Sonnet File Revision Steps - EL

- manually took out the front and back publication portions of the file

Find: (.+)

Replace: [ <xml>\n\1\n</xml> ]
- Takes the file and wraps the whole thing in xml tags (also giving new lines) ]

- manually adjusted any inconsistent spacing between sonnets (two instances)

[ Find:
`^(\s*)([IVXLCDM]+)(\s)(.+?)(\n)` 

Replace:
`<sonnet number="\2">\4\n</sonnet>\n`
- This was the final expression I used to wrap each of the sonnets. It worked on all except for the very last sonnet for some reason that I figure has to do with spacing somehow (which was manually fixed) ]

Find: (<sonnet number="[IVXLCDM]+">)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)(\n)(.+?)


Replace: \1\n\t<line>\3</line>\n\t<line>\5</line>\n\t<line>\7</line>\n\t<line>\9</line>\n\t<line>\11</line>\n\t<line>\13</line>\n\t<line>\15</line>\n\t<line>\17</line>\n\t<line>\19</line>\n\t<line>\21</line>\n\t<line>\23</line>\n\t<line>\25</line>\n\t<line>\27</line>\n\t<line>\29</line>\n

- I like to call this the brute force method. Since each sonnet has 14 lines, I basically created a repitition for each sonnet that works 14 times to make line tags. For some reason that I again cannot discern, it worked flawlessly on every single sonnet EXCEPT for one random one (specifically #127), which was also fixed manually.

- Upon reflection, I think the reason that particular sonnet did not work is because the one previous was only 12 lines instead of 14, and therefore did not adhere to my very specific expression

Find:` <line>    (.+?) `

Replace: ` <line indent="true">    \1 `

- using the extra space alloted in them, I found the last two lines of each sonnet and added an "indent" attribute to each
