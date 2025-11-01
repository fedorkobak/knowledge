# Intro

This section is for topics that are not closely related to any other topic and do not have enough content to justify creating a new one.

## Agile

The Agile is to approach for software development that relies on the following principles: you have to give more value to

- Individuals and interactions over processes and tools.
- Working software over comprehensive documentation
- Communicating with customers over negotiating contracts.
- Responding to change over following a plan.

There two main frameworks that follows Agile principle: Scrum and Kanban.

### Scrum

In Scrum, work involves iterative improvements to the software. Each iteration takes from one to four weeks and is called a *sprint*. There are:

- **Events**: periodical meetings or other organisational ceremonies that are usually tied to a particular phase of the software development.
- **Artifacts**: the things to be done. Separated into few groups typically: *backlog*, *to do*, *in process* and *done*.
- **Roles**: 
    - *Product owner*: person responsible for communication with the customer.
    - *Scrum master*: person that checks that scrum rules are followed.
    - *Scrum team*: people who complete the tasks.

### Kanban

Kanban just takes from scrum the groups of tasks: *to do*, *doing* and *done*.


## Markdown

Markdown is a special text formatting language. The overview:

Markdown is a lightweight markup language for formatting plain text.
Here are its basic features:

* **Headings:** `# H1`, `## H2`, `### H3`
* **Emphasis:** `*italic*`, `**bold**`, `~~strikethrough~~`
* **Lists:**

  * Unordered: `- item` or `* item`
  * Ordered: `1. item`
* **Links:** `[text](https://example.com)`
* **Images:** `![alt text](image.png)`
* **Code:**

  * Inline: `` `code` ``
  * Block:

    ````markdown
    ```python
    print("hello")
    ```
    ````
* **Blockquotes:** `> quote`
* **Tables:**

  ```markdown
  | A | B |
  |:-|:-:|
  | 1 | 2 |
  ```
* **Horizontal line:** `---` or `***`
* **Inline HTML:** `<b>bold</b>`

It’s designed to be readable as plain text and easily converted to HTML.

### Tables

Tables in markdown can be specified with the following syntax:

```markdown
| Column name 1 | Column name 2 | Column name 3 |
|:--------------|--------------:|:-------------:|
|   value 11    |  value 12     |  value 13     |                
|   value 21    |  vlaue 22     |  value 23     |
```

The colon (`:`) in the line separating the header from the content defines content's alignment.

The example table will be rendered as follows:

| Column name 1 | Column name 2 | Column name 3 |
|:--------------|--------------:|:-------------:|
|   value 11    |  value 12     |  value 13     |                
|   value 21    |  vlaue 22     |  value 23     |

### Links

- Any text that begins with `https://` will be interpreted as a link and will be clickable.
- To create a hyperlink use the syntax `[represented text](<addres>)`.
- It's not alway convenient to put the address right after text. You can define the hyperlink as `[my link][1]` and specify the address later in the text as `[1]: <address>`. This approach is called **refence-style link**.

---

Consdier the following code:

```markdown
Just address https://google.com

[Inline hyperlink](https://google.com)

[Reference-stype link][1]

[1]: https://google.com
```

This code would be rendered as:

Just address https://google.com

[Inline hyperlink](https://google.com)

[Reference-stype link][1].

[1]: https://google.com


