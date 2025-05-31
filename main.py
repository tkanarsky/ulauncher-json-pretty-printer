import json
import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)


class JsonPrettyPrinterExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        """Handle user input and format JSON"""
        
        # Get user input (query argument)
        input_text = event.get_argument() or ""
        
        # Determine if this is minify mode based on keyword
        keyword = event.get_keyword()
        is_minify = keyword == extension.preferences.get('jmm_kw', 'jmm')
        
        # Get user preferences
        try:
            indent_size = int(extension.preferences.get('indent', '2'))
            if indent_size < 0 or indent_size > 8:
                indent_size = 2
        except (ValueError, TypeError):
            indent_size = 2
        
        items = []
        
        # If no input provided, show usage instructions
        if not input_text.strip():
            if is_minify:
                items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name='JSON Minifier',
                    description='Enter JSON string to minify, e.g {"foo": "bar", "baz": 42}',
                    on_enter=HideWindowAction()
                ))
            else:
                items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name='JSON Pretty-printer',
                    description='Enter JSON string to format, e.g {"foo":"bar","baz":42}',
                    on_enter=HideWindowAction()
                ))
            return RenderResultListAction(items)
        
        try:
            # Try to parse the JSON
            parsed_json = json.loads(input_text.strip())
            
            if is_minify:
                # Format as minified JSON
                formatted_json = json.dumps(parsed_json, separators=(',', ':'), ensure_ascii=False, sort_keys=True)
                action_name = 'Copy minified JSON'
            else:
                # Format with pretty printing
                formatted_json = json.dumps(parsed_json, indent=indent_size, ensure_ascii=False, sort_keys=True)
                action_name = 'Copy pretty-printed JSON'
            
            # Show the formatted result
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name=action_name,
                description=self._truncate_text(formatted_json, 100),
                on_enter=CopyToClipboardAction(formatted_json)
            ))
            
        except json.JSONDecodeError as e:
            # Show error information
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name='Invalid JSON',
                description=f'Error: {str(e)}',
                on_enter=HideWindowAction()
            ))
            
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name='Error processing input',
                description=f'Unexpected error: {str(e)}',
                on_enter=HideWindowAction()
            ))
        
        return RenderResultListAction(items)
    
    def _truncate_text(self, text: str, max_length: int) -> str:
        """Truncate text to a maximum length with ellipsis"""
        if len(text) <= max_length:
            return text
        return text[:max_length-3] + '...'


if __name__ == '__main__':
    JsonPrettyPrinterExtension().run()