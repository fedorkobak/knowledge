# Terminology

This page contains general terminology of the HTML language. It makes sence to describe it separately as we discuss some special features of HTML in a separate section (e.g. forms).

**Element** is a complete part of the html language, it includes *start* and *end* tags. For example:

```HTML
<p>Content of the element</p>
```

**Open tag** marks the start of an element. It consists of the tag name and *attributes* enclosed in angle brackets (`<>`).

```HTML
<p>
```

**End tag** marks the end of the element. It is the same as *open tag* but marked there is a `/` in front of the tag name.

```HTML
</p>
```

**Attribute** is a special name that allows to configuration to be applied to the element. **Value** information assigned to an attribute.

```HTML
<p style="color:blue"></p>
```

Here `style` is attribute and `"color:blue"` is value.

Many HTML elements contain some text that needs to be displayed on them. Such information is called the **content** of the element and is usually placed between the *open tag* and *end tag*.

```HTML
<p>Content of the element</p>
```

Here *content* is the "Content of the element" line.

**Void elements** is an elements that does not need a closing tag because it is not supposed to have any content.

```HTML
<img src="image_file.jpg">
```