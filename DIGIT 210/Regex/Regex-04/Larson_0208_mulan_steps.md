# Mulan Revision Steps - EL


Find: ` \n\n `

Replace: ` </sp>\n\n<sp> `
- Wraps "sp" tags around each chunk of text separated by a blank line, which required manually adding an opening tag at the beginning and a closing tag at the end.

Find: ` (.+) `

Replace: ` <root>\n\0\n</root> `
- Gives the file a root element