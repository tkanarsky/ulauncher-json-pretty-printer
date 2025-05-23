## Ulauncher JSON pretty printer extension

Install by entering https://github.com/tkanarsky/ulauncher-json-pretty-printer in the Add Extension dialog.

Initially hydrated by Claude Code from the following priors:
- Ulauncher v5 extension documentation loaded into context
- `jpp` keyword
- Adjustable spacing
- Action to copy pretty-printed json

followed by manual cleanup of Claude-isms.

Logo adapted from https://github.com/jesseweed/seti-ui/blob/master/icons/json.svg under MIT license.
Recolored and png-ified with 
```
sed -i 's/#DBCD68/#000000/g' ~/Downloads/json.svg && convert -density 288 -background none ~/Downloads/json.svg images/icon.png
```

MIT licensed.