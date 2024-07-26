##
What is Markdown?
Markdown exists to shield content creators from the overhead of HTML. While HTML is great for rendering content exactly how it was intended, it takes up a lot of space and can be unwieldy to work with, even in small doses. The invention of Markdown offered a great compromise between the power of HTML for content description and the ease of plain text for editing.

This is *italic* text.
This is also _italic_ text.

Declaring headings
HTML provides content headings, such as the <h1> tag. In Markdown, this is supported via the # symbol. Just use one # for each heading level from 1-6.
  Ex
  ###### This is H6 text

  to order
  
  1. First
1. Second
1. Third
  
  
  - First
  - Nested
- Second
- Third.
  
  Building tables
You can construct tables using a combination of pipes (|) for column breaks and dashes (-) to designate the prior row as a header.
  First|Second
-|-
1|2
3|4
  
  
  > This is quoted text.
  
  Here is a<br />line break
  
  ```markdown
var first = 1;
var second = 2;
var sum = first + second;
```
  
 Tracking task lists
You can create task lists within issues or pull requests using the following syntax. These can be helpful to track progress when used in the body of an issue or pull request
  
  
  - [x] First task
- [x] Second task
- [ ] Third task
