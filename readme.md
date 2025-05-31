## Ulauncher JSON formatter extension

Install by entering https://github.com/tkanarsky/ulauncher-json-pretty-printer in the Add Extension dialog.

### Features

- **Pretty-print JSON** with `jpp` keyword - formats JSON with configurable indentation (2-8 spaces)
- **Minify JSON** with `jmm` keyword - removes unnecessary whitespace for compact output
- Both commands copy the formatted result to clipboard
- Error handling for invalid JSON with helpful error messages

### Usage

1. Type `jpp` followed by your JSON string to pretty-print it
2. Type `jmm` followed by your JSON string to minify it
3. Press Enter to copy the formatted result to your clipboard

Initially hydrated by Claude Code from the following priors:
- Ulauncher v5 extension documentation loaded into context
- `jpp` keyword for pretty-printing
- `jmm` keyword for minification  
- Adjustable spacing
- Action to copy formatted json

followed by manual cleanup of Claude-isms.

Logo adapted from https://github.com/jesseweed/seti-ui/blob/master/icons/json.svg under MIT license.
Recolored and png-ified with 
```
sed -i 's/#DBCD68/#000000/g' ~/Downloads/json.svg && convert -density 288 -background none ~/Downloads/json.svg images/icon.png
```

MIT licensed.